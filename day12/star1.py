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

AREA = 0
PERIMETER = 0


def dfs(_i, _j, _letter):
    global AREA, PERIMETER

    if visited[_i][_j]:
        return

    visited[_i][_j] = True
    PERIMETER += calculate_perimeter_for_a_cell(_i, _j, _letter)
    AREA += 1

    for i in range(4):
        next_i, next_j = _i + steps[i][0], _j + steps[i][1]
        if (0 <= next_i < MAX_I and 0 <= next_j < MAX_J and
                cur_map[next_i][next_j] == _letter and not visited[next_i][next_j]):
            dfs(next_i, next_j, _letter)

    return


def calculate_perimeter_for_a_cell(_i, _j, _letter):
    _perimeter = 0
    # up
    if _i - 1 < 0 or cur_map[_i-1][_j] != _letter:
        _perimeter += 1
    # left
    if _j - 1 < 0 or cur_map[_i][_j-1] != _letter:
        _perimeter += 1
    # right
    if _j + 1 >= MAX_J or cur_map[_i][_j + 1] != _letter:
        _perimeter += 1
    # down
    if _i + 1 >= MAX_I or cur_map[_i+1][_j] != _letter:
        _perimeter += 1
    return _perimeter


RESULT = 0
for i in range(MAX_I):
    for j in range(MAX_J):
        if not visited[i][j]:
            PERIMETER = 0
            AREA = 0
            dfs(i, j, cur_map[i][j])
            print(cur_map[i][j], PERIMETER, AREA)
            RESULT += PERIMETER * AREA


print(RESULT)


