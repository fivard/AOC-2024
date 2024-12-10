with open("example.txt", "r") as file:
    matrix = [list(map(int, line.strip())) for line in file]

for row in matrix:
    print(row)

ROW_LENGTH = len(matrix[0])
FOUND_TRAIL = 0


def find_all_trail(i, j, cur_num=0, visited_9=None):
    global FOUND_TRAIL

    if visited_9 is None:
        visited_9 = {}

    # if cur_num == 9 and f"{i},{j}" not in visited_9.keys():
    if cur_num == 9:
        # visited_9[f"{i},{j}"] = True
        FOUND_TRAIL += 1
        return

    if i-1 >= 0 and matrix[i-1][j] == cur_num + 1:
        find_all_trail(i-1, j, cur_num+1, visited_9)

    if i+1 < ROW_LENGTH and matrix[i+1][j] == cur_num + 1:
        find_all_trail(i+1, j, cur_num + 1, visited_9)

    if j-1 >= 0 and matrix[i][j-1] == cur_num + 1:
        find_all_trail(i, j-1, cur_num + 1, visited_9)

    if j+1 < ROW_LENGTH and matrix[i][j+1] == cur_num + 1:
        find_all_trail(i, j+1, cur_num + 1, visited_9)

    if cur_num == 0:
        print("RES: ", FOUND_TRAIL)
        return FOUND_TRAIL

result = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            print("-----------------------------------------")
            print(i, j)
            result += find_all_trail(i, j)
            print("-----------------------------------------")
            FOUND_TRAIL = 0

print(result)