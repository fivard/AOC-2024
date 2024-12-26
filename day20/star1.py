import time
from collections import deque, defaultdict

test = False


if test:
    file_name = "simple_example.txt"
else:
    file_name = "example.txt"


def read_from_file():
    with open(file_name, 'r') as file:
        data = [list(line.strip()) for line in file]

    return data


def find_start_and_end(_map):
    start, end = (None, None), (None, None)

    for i in range(len(_map)):
        for j in range(len(_map[i])):
            if _map[i][j] == "S":
                start = (i, j)
            if _map[i][j] == "E":
                end = (i, j)

    return start, end


def beautiful_print(_map):
    for row in _map:
        for column in row:
            print(column, end="\t")
        print()


def find_cheats(_map, cur_x, cur_y, cur_score, result):
    possible_dir_for_cheats = [[-2, 0], [0, -2], [2, 0], [0, 2], [-1, 1], [1, -1], [-1, -1], [1, 1]]

    for dir in possible_dir_for_cheats:
        new_x, new_y = cur_x + dir[0], cur_y + dir[1]
        if (0 <= new_x < len(_map) and 0 <= new_y < len(_map[0])
                and isinstance(_map[new_x][new_y], int) and _map[new_x][new_y] + 2 < cur_score):
            new_score = _map[new_x][new_y]
            result[cur_score - new_score - 2] += 1


def bfs(_map, start):
    queue = deque()
    _map[start[0]][start[1]] = 0
    queue.append((start[0], start[1], 0))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cur_x, cur_y, cur_score = queue.popleft()

        for direction in directions:
            new_x, new_y, new_score = cur_x + direction[0], cur_y + direction[1], cur_score + 1

            if _map[new_x][new_y] == "#":
                continue
            if _map[new_x][new_y] in [".", "E"]:
                _map[new_x][new_y] = new_score
                queue.append((new_x, new_y, new_score))

            if  isinstance(_map[new_x][new_y], int) and _map[new_x][new_y] > new_score:
                _map[new_x][new_y] = new_score
                queue.append((new_x, new_y, new_score))


def backwards_bfs(_map, end):
    queue = deque()
    result = defaultdict(int)
    queue.append((end[0], end[1], _map[end[0]][end[1]]))    # x, y, score

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cur_x, cur_y, cur_score = queue.popleft()

        find_cheats(_map, cur_x, cur_y, cur_score, result)

        for direction in directions:
            new_x, new_y, new_score = cur_x + direction[0], cur_y + direction[1], cur_score - 1

            if isinstance(_map[new_x][new_y], int) and _map[new_x][new_y] == new_score:
                queue.append((new_x, new_y, new_score))
    return result


def resolve():
    my_map = read_from_file()
    start, end = find_start_and_end(my_map)
    bfs(my_map, start)
    result = backwards_bfs(my_map, end)
    return sum([count_of_cheats for saved_seconds, count_of_cheats in result.items() if saved_seconds >= 100])


if __name__ == "__main__":
    start_time = time.time()
    result = resolve()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")





