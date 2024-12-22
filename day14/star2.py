test = False

if test:
    border_X = 7
    border_Y = 11
    file_name = "simple_example.txt"
else:
    border_X = 103
    border_Y = 101
    file_name = "example.txt"

with open(file_name, 'r') as file:
    lines = file.readlines()

data = []
cur_pos = []
for line in lines:
    line = line.strip()
    parts = line.split(" ")
    p = tuple(map(int, parts[0][2:].split(",")))
    v = tuple(map(int, parts[1][2:].split(",")))
    data.append([p, v])
    cur_pos.appe


def print_data(_data):
    for item in _data:
        print(item)


def beautiful_print(_map):
    for _row in _map:
        print(''.join(_row))


exampl_matrix = [["." for _ in range(border_Y)] for _ in range(border_X)]
cur_pos = []
for i in range(100):
    for robot in data:
        current_Y, current_X, step_Y, step_X = robot[0][0], robot[0][1], robot[1][0], robot[1][1]
        current_X, current_Y = (current_X + step_X + border_X) % border_X, (current_Y + step_Y + border_Y) % border_Y
        # print(final_cords)
        exampl_matrix[current_X][current_Y] = "1" if exampl_matrix[final_cords[0]][final_cords[1]] == '.' else str(int(exampl_matrix[final_cords[0]][final_cords[1]]) + 1)
        beautiful_print(exampl_matrix)
# beautiful_print(exampl_matrix)
print(left_up_res * left_down_res * right_up_res * right_down_res)



