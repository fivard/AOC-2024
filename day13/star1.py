import math


data = []
with open("example.txt", "r") as file:
    for line in file:
        if line.strip():
            key, value = line.strip().split(":")
            if key.strip() == "Button A":
                A = tuple(map(int, value.strip().replace("X+", "").replace("Y+", "").split(", ")))
            elif key.strip() == "Button B":
                B = tuple(map(int, value.strip().replace("X+", "").replace("Y+", "").split(", ")))
            elif key.strip() == "Prize":
                prize = tuple(map(int, value.strip().replace("X=", "").replace("Y=", "").split(", ")))
                data.append(
                    [
                        [A[0], B[0], prize[0]],     # A_x * x + B_x * y = C1
                        [A[1], B[1], prize[1]],     # A_y * x + B_y * y = C2
                     ]
                )


def is_equal(first_float, second_float):
    return abs(first_float - second_float) < 1e-6


def is_effectively_integer(num, tol=1e-9):
    return math.isclose(num, round(num), abs_tol=tol) or math.isclose(num, round(num+1), abs_tol=tol)


def beautiful_print(matrix):
    print("\n--------------------------\n")
    for row in matrix:
        print(''.join(str(row)))
    print("\n--------------------------\n")


def gaus_method(temp_matrix):
    A_x = temp_matrix[0][0]
    for i in range(3):
        temp_matrix[0][i] /= A_x

    A_y = temp_matrix[1][0]
    for i in range(3):
        temp_matrix[1][i] -= temp_matrix[0][i] * A_y

    B_y = temp_matrix[1][1]
    for i in range(3):
        temp_matrix[1][i] /= B_y

    B_x = temp_matrix[0][1]
    for i in range(3):
        temp_matrix[0][i] -= temp_matrix[1][i] * B_x

    if is_effectively_integer(temp_matrix[0][2]) and is_effectively_integer(temp_matrix[1][2]):
        return 3*round(temp_matrix[0][2]) + round(temp_matrix[1][2])
    return 0


res = 0
for i in range(len(data)):
    res += gaus_method(data[i])

print(res)
