with open("example.txt", "r") as file:
    matrix = [list(line.strip()) for line in file if line.strip()]

MAX_I = len(matrix)
MAX_J = len(matrix[0])
unique_antinode = {}


def beautiful_print():
    for row in matrix:
        print(''.join(row))


def number_of_antinodes(main_i, main_j, number):
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == number and i != main_i and j != main_j:
                dist_i = abs(i - main_i)
                dist_j = abs(j - main_j)
                antinode1_i = i - dist_i if i < main_i else i + dist_i
                antinode1_j = j - dist_j if j < main_j else j + dist_j
                antinode2_i = main_i + dist_i if main_i > i else main_i - dist_i
                antinode2_j = main_j + dist_j if main_j > j else main_j - dist_j

                print(unique_antinode.keys())
                if 0 <= antinode1_i < MAX_I and 0 <= antinode1_j < MAX_J and f"{antinode1_i},{antinode1_j}" not in unique_antinode.keys():
                    unique_antinode[f"{antinode1_i},{antinode1_j}"] = True
                    print(f"{antinode1_i},{antinode1_j}")
                    if matrix[antinode1_i][antinode1_j] == ".":
                        matrix[antinode1_i][antinode1_j] = "#"
                    res += 1
                if 0 <= antinode2_i < MAX_I and 0 <= antinode2_j < MAX_J and f"{antinode2_i},{antinode2_j}" not in unique_antinode.keys():
                    unique_antinode[f"{antinode2_i},{antinode2_j}"] = True
                    print(f"{antinode2_i},{antinode2_j}")
                    if matrix[antinode2_i][antinode2_j] == '.':
                        matrix[antinode2_i][antinode2_j] = "#"
                    res += 1

                beautiful_print()
                print(res)
                print()
                print("----------------------------------------------------")
                print()

    return res


result = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != "." and matrix[i][j] != "#":
            print(f"FOUND {matrix[i][j]}, {i}, {j}")
            result += number_of_antinodes(i, j, matrix[i][j])


print(result)