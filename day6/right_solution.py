import numpy as np


import sys
import time
from contextlib import contextmanager
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


def read_input(day: int) -> str:
    with open(f"example.txt", encoding="utf-8") as f:
        return f.read()


@contextmanager
def timer():
    time_start = time.perf_counter()
    try:
        yield
    finally:
        duration = time.perf_counter() - time_start
        print(f"[{duration:.3f} seconds]", file=sys.stderr)

Loc = tuple[int, int]
Direction = tuple[int, int]

InputData = tuple[np.ndarray, Loc]

START_MARKER = "^"
WALL = "#"
OPEN = "."

DIRECTIONS = [  # order matters
    (-1, 0),  # up
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
]


def get_parsed_input() -> InputData:
    input_raw = read_input(6)
    input_lines = input_raw.strip().splitlines()
    grid = np.array([
        [char != WALL for char in line]
        for line in input_lines
    ])
    for i, line in enumerate(input_lines):
        for j, char in enumerate(line):
            if char == START_MARKER:
                start_loc = (i, j)
                return grid, start_loc
    else:
        raise ValueError(f"start marker {START_MARKER!r} not found")


class OffGrid(Exception):
    """raised when the guard goes off the grid"""


class InfiniteLoop(Exception):
    """raised when the guard stays on the grid infinitely"""


class GuardSim:
    def __init__(self, grid: np.ndarray, start_loc: Loc):
        super().__init__()
        if len(grid.shape) != 2:
            raise ValueError("grid must be 2-dimensional")
        if grid.dtype != np.bool:
            raise TypeError("grid must contain booleans")
        self.grid = grid
        self.start_loc = start_loc
        self.current_loc = self.start_loc
        self._direction_index = 0  # up

    @property
    def n_rows(self) -> int:
        return self.grid.shape[0]

    @property
    def n_cols(self) -> int:
        return self.grid.shape[1]

    def direction(self) -> Direction:
        return DIRECTIONS[self._direction_index]

    def turn_right(self):
        self._direction_index = (self._direction_index + 1) % len(DIRECTIONS)

    def step_forward(self) -> bool:
        direction = self.direction()
        next_loc = self.current_loc[0] + direction[0], self.current_loc[1] + direction[1]
        if not (0 <= next_loc[0] < self.n_rows and 0 <= next_loc[1] < self.n_cols):  # out of bounds
            raise OffGrid
        if self.grid[next_loc]:  # can step forward
            self.current_loc = next_loc
            return True
        else:  # wall
            return False

    def walk(self) -> set[Loc]:
        history: set[tuple[Loc, Direction]] = set()
        history.add((self.current_loc, self.direction()))
        while True:
            try:
                could_step = self.step_forward()
            except OffGrid:
                return {loc for loc, _ in history}
            if not could_step:  # hit a wall
                self.turn_right()
            new_history_entry = (self.current_loc, self.direction())
            if new_history_entry in history:  # doomed to repeat itself, as they say
                raise InfiniteLoop
            history.add(new_history_entry)


def main(input_parsed: InputData):
    grid, start_loc = input_parsed
    # part 1
    initial_guard_sim = GuardSim(grid, start_loc)
    locs_visited = initial_guard_sim.walk()
    print(f"{len(locs_visited) = }")
    # part 2
    locs_to_modify = locs_visited - {start_loc}
    infinite_loops_count = 0
    for loc_modification in locs_to_modify:  # could run these in parallel if we have appropriate hardware
        grid_modified = grid.copy()
        grid_modified[loc_modification] = False  # place an obstacle
        modified_guard_sim = GuardSim(grid_modified, start_loc)
        try:
            modified_guard_sim.walk()
        except InfiniteLoop:
            print(loc_modification)
            infinite_loops_count += 1
    print(f"{infinite_loops_count = }")


if __name__ == "__main__":
    with timer():
        main(get_parsed_input())