with open("example.txt", "r") as file:
    matrix = [list(line.strip()) for line in file if line.strip()]

MAX_I = len(matrix)
MAX_J = len(matrix[0])


def beautiful_print():
    for row in matrix:
        print(''.join(row))


def verify_x_max(cur_i, cur_j):
    shift = [[-1, -1], [-1, 1], [1, 1], [1, -1]]
    letters = "SSMM"

    for rotation in range(4):
        for order in range(4):
            _shift = shift[(rotation + order) % 4]
            _i = cur_i + _shift[0]
            _j = cur_j + _shift[1]
            if 0 <= _i < MAX_I and 0 <= _j < MAX_J and letters[order] == matrix[_i][_j]:
                if order == 3:
                    return 1
            else:
                break
    return 0


RESULT = 0
for i in range(MAX_I):
    for j in range(MAX_J):
        RESULT += verify_x_max(i, j) if matrix[i][j] == "A" else 0

print(RESULT)
