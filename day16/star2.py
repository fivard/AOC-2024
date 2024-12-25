import time
from collections import deque

test = False

if test:
    file_name = "simple_example.txt"
else:
    file_name = "example.txt"


def read_from_file():
    with open(file_name, 'r') as file:
        _map = [list(line.strip()) for line in file if line.strip()]
    return _map


def beautiful_print(_map):
    for row in _map:
        for column in row:
            print(column, end="")
        print()


directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def turn_right(cur_dir):
    return directions[(directions.index(cur_dir) + 1 + len(directions)) % len(directions)]


def turn_left(cur_dir):
    return directions[(directions.index(cur_dir) - 1 + len(directions)) % len(directions)]


def backwards_bfs(_map):
    queue = deque()
    res = 1
    start_1 = (1, len(_map[1]) - 2, (1, 0), _map[1][len(_map[1]) - 2])  # x, y, direction, score
    start_2 = (1, len(_map[1]) - 2, (0, -1), _map[1][len(_map[1]) - 2])  # x, y, direction, score
    queue.append(start_1)
    queue.append(start_2)
    visited = set()

    while queue:
        current = queue.popleft()
        cur_x = current[0]
        cur_y = current[1]
        cur_dir = current[2]
        cur_score = current[3]

        allowed_directions_n_score = [
            (cur_dir, cur_score - 1),
            (turn_left(cur_dir), cur_score - 1001),
            (turn_right(cur_dir), cur_score - 1001)
        ]

        for new_dir, new_score in allowed_directions_n_score:
            new_x, new_y = cur_x + new_dir[0], cur_y + new_dir[1]
            if isinstance(_map[new_x][new_y], int) and (_map[new_x][new_y] in [new_score, new_score - 1000]) and (new_x, new_y) not in visited:
                res += 1
                queue.append((new_x, new_y, new_dir, new_score))
                visited.add((new_x, new_y))

    return res

def bfs(_map):
    queue = deque()
    start = (len(_map) - 2, 1, (0, 1), 0)  # x, y, direction, score
    _map[len(_map) - 2][1] = 0
    queue.append(start)

    while queue:
        current = queue.popleft()
        cur_x = current[0]
        cur_y = current[1]
        cur_dir = current[2]
        cur_score = current[3]

        allowed_directions_n_score = [
            (cur_dir, cur_score + 1),
            (turn_left(cur_dir), cur_score + 1001),
            (turn_right(cur_dir), cur_score + 1001)
        ]

        for new_dir, new_score in allowed_directions_n_score:
            new_x, new_y = cur_x + new_dir[0], cur_y + new_dir[1]
            if _map[new_x][new_y] == "#":
                continue

            if _map[new_x][new_y] in [".", "E"] or (isinstance(_map[new_x][new_y], int) and _map[new_x][new_y] > new_score):
                _map[new_x][new_y] = new_score
                queue.append((new_x, new_y, new_dir, new_score))

    return _map[1][len(_map[1]) - 2]


def resolve():
    my_map = read_from_file()
    bfs(my_map)
    return backwards_bfs(my_map)


if __name__ == "__main__":
    start_time = time.time()
    result = resolve()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
