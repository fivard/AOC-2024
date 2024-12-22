import time
from collections import deque


test = False


if test:
    size = 6
    length_of_corrupted = 12
    file_name = "simple_example.txt"
else:
    length_of_corrupted = 1024
    size = 70
    file_name = "example.txt"


def beautiful_print(_map):
    for _row in _map:
        print(''.join(_row))


with open(file_name, "r") as file:
    cords = [tuple(map(int, line.strip().split(','))) for line in file]


def create_map():
    _map = [["." for _ in range(size + 1)] for _ in range(size + 1)]
    for cord in cords:
        _map[cord[1]][cord[0]] = "#"
    # beautiful_print(_map)
    return _map


def bfs(_map):
    # matrix_of_shortest_paths = [[0 for _ in range(size + 1)] for _ in range(size + 1)]
    queue = deque()
    queue.append((0, 0, 0))
    visited = set()
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        x, y, length = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if (x, y) == (size, size):
            return length
        for move in moves:
            if 0 <= x + move[0] <= size and 0 <= y + move[1] <= size and _map[x + move[0]][y + move[1]] == ".":
                queue.append((x + move[0], y + move[1], length + 1))

    return None


def resolve():
    my_map = create_map()
    for i in range(len(cords) - 1, 1024, -1):
        new_corrupted = cords[i]
        my_map[new_corrupted[1]][new_corrupted[0]] = "."
        result = bfs(my_map)
        if result is not None:
            return cords[i]


if __name__ == "__main__":
    start_time = time.time()
    result = resolve()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")









