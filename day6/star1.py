with open("example.txt", "r") as file:
    matrix = [list(line.strip()) for line in file if line.strip()]

MAX_I = len(matrix)
MAX_J = len(matrix[0])
cur_i, cur_j = 0, 0


def beautiful_print():
    for row in matrix:
        print(''.join(row))


def make_step(i, j, given_direction):
    return i + given_direction[0], j + given_direction[1]


def turn_right(given_direction):
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]
    return directions[(directions.index(given_direction) + 1) % 4]


for i in range(MAX_I):
    for j in range(MAX_J):
        if matrix[i][j] == '^':
            cur_i = i
            cur_j = j

res = 0
direction = (-1, 0)
while 0 <= cur_i < MAX_I and 0 <= cur_j < MAX_J:
    if matrix[cur_i][cur_j] != "X":
        res += 1
        matrix[cur_i][cur_j] = "X"

    next_i, next_j = make_step(cur_i, cur_j, direction)
    while 0 <= next_i < MAX_I and 0 <= next_j < MAX_J and matrix[next_i][next_j] == "#":
        direction = turn_right(direction)
        next_i, next_j = make_step(cur_i, cur_j, direction)

    cur_i, cur_j = make_step(cur_i, cur_j, direction)

print(res)

