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
for line in lines:
    line = line.strip()
    parts = line.split(" ")
    p = tuple(map(int, parts[0][2:].split(",")))
    v = tuple(map(int, parts[1][2:].split(",")))
    data.append([p, v])


def print_data(_data):
    for item in _data:
        print(item)


def beautiful_print(_map):
    for _row in _map:
        print(''.join(_row))


def get_final_cords(robot_values):
    current_Y, current_X, step_Y, step_X = robot_values[0][0], robot_values[0][1], robot_values[1][0], robot_values[1][1]
    visited_cell = [(current_X, current_Y)]

    for i in range(100):
        current_X, current_Y = (current_X + step_X + border_X) % border_X, (current_Y + step_Y + border_Y) % border_Y
        # we reached the start point
        if (current_X, current_Y) == visited_cell[0]:
            return visited_cell[(100 - i - 1) % len(visited_cell)]
        visited_cell.append((current_X, current_Y))

    return current_X, current_Y


# print_data(data)
left_up_res, left_down_res, right_up_res, right_down_res = 0, 0, 0, 0
exampl_matrix = [["." for _ in range(border_Y)] for _ in range(border_X)]
for robot in data:
    final_cords = get_final_cords(robot)
    # print(final_cords)
    # exampl_matrix[final_cords[0]][final_cords[1]] = "1" if exampl_matrix[final_cords[0]][final_cords[1]] == '.' else str(int(exampl_matrix[final_cords[0]][final_cords[1]]) + 1)
    if final_cords[0] < border_X // 2 and final_cords[1] < border_Y // 2:
        left_up_res += 1
    if final_cords[0] < border_X // 2 and final_cords[1] > border_Y // 2:
        right_up_res += 1
    if final_cords[0] > border_X // 2 and final_cords[1] < border_Y // 2:
        left_down_res += 1
    if final_cords[0] > border_X // 2 and final_cords[1] > border_Y // 2:
        right_down_res += 1

# beautiful_print(exampl_matrix)
print(left_up_res * left_down_res * right_up_res * right_down_res)



