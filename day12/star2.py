from collections import deque

with open("example.txt", "r") as file:
    cur_map = [list(line.strip()) for line in file if line.strip()]

MAX_I = len(cur_map)
MAX_J = len(cur_map[0])


visited = [[False for _ in range(MAX_J)] for _ in range(MAX_I)]


def beautiful_print():
    for _row in cur_map:
        print(''.join(_row))


steps = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
]


def bfs(_i, _j, _letter):
    queue = deque()
    queue.append((_i, _j, ""))
    sides_count = 0
    area = 0
    sides = set()

    while queue:
        cur = queue.popleft()
        cur_i, cur_j, cur_direction = cur[0], cur[1], cur[2]
        if (cur_i < 0 or cur_i >= MAX_I or cur_j < 0 or cur_j >= MAX_J or
                cur_map[cur_i][cur_j] != _letter):
            if not (
                    (cur_i + 1, cur_j, cur_direction) in sides or
                    (cur_i - 1, cur_j, cur_direction) in sides or
                    (cur_i, cur_j + 1, cur_direction) in sides or
                    (cur_i, cur_j - 1, cur_direction) in sides
            ):
                sides_count += 1

            if (((cur_i + 1, cur_j, cur_direction) in sides and
                (cur_i - 1, cur_j, cur_direction) in sides) or
                    ((cur_i, cur_j + 1, cur_direction) in sides and
                     (cur_i, cur_j - 1, cur_direction) in sides)):
                sides_count -= 1
            sides.add((cur_i, cur_j, cur_direction))
            continue

        if visited[cur_i][cur_j]:
            continue

        visited[cur_i][cur_j] = True
        area += 1

        queue.append((cur_i - 1, cur_j, "u"))
        queue.append((cur_i, cur_j + 1, "r"))
        queue.append((cur_i + 1, cur_j, "d"))
        queue.append((cur_i, cur_j - 1, "l"))
    return sides_count, area


RESULT = 0
for i in range(MAX_I):
    for j in range(MAX_J):
        if not visited[i][j]:
            sides_count, area = bfs(i, j, cur_map[i][j])
            RESULT += sides_count * area


print(RESULT)


