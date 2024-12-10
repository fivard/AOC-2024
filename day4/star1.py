with open("example.txt", "r") as file:
    matrix = [list(line.strip()) for line in file if line.strip()]

MAX_I = len(matrix)
MAX_J = len(matrix[0])


def beautiful_print():
    for row in matrix:
        print(''.join(row))


def find_all_ocurs(cur_i, cur_j):
    letters = "XMAS"
    res = 0
    steps = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

    for step in steps:
        index = 1
        while (0 <= cur_i + step[0] * index < MAX_I and
               0 <= cur_j + step[1] * index < MAX_J and
               matrix[cur_i + step[0] * index][cur_j + step[1] * index] == letters[index]):
            index += 1
            if index == len(letters):
                res += 1
                break

    return res




RESULT = 0
for i in range(MAX_I):
    for j in range(MAX_J):
        RESULT += find_all_ocurs(i, j) if matrix[i][j] == "X" else 0

print(RESULT)
