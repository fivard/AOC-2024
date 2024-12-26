import time

import utils

test = False

if test:
    file_name = "simple_example.txt"
else:
    file_name = "example.txt"


def read_from_file():
    with open(file_name, 'r') as file:
        lines = file.readlines()

    matrix_lines = []
    commands_line = []
    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            matrix_lines.append(line)
        elif line:
            commands_line.append(line)

    first_matrix = [list(row) for row in matrix_lines]
    second_matrix = []
    current_row = 0
    for i in range(len(first_matrix)):
        second_matrix.append([])
        for j in range(len(first_matrix[0])):
            if first_matrix[i][j] in ["#", "."]:
                second_matrix[current_row] += [first_matrix[i][j], first_matrix[i][j]]
            if first_matrix[i][j] == "O":
                second_matrix[current_row] += ["[", "]"]
            if first_matrix[i][j] == "@":
                second_matrix[current_row] += ["@", "."]
        current_row += 1

    commands = list("".join(commands_line))

    return second_matrix, commands


def get_start_pos(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "@":
                return i, j
    return None


def move_to(current, direction, matrix, symbol):
    new_x, new_y = current[0] + direction[0], current[1] + direction[1]
    matrix[new_x][new_y] = symbol
    matrix[current[0]][current[1]] = "."


def update_cords_with_direction(cords, direction):
    return cords[0] + direction[0], cords[1] + direction[1]


def cords_of_next_containers(current, direction, matrix):
    current_x, current_y = current[0], current[1]
    if matrix[current_x + direction[0]][current_y] == "[":
        return(current_x + direction[0], current_y), (current_x + direction[0], current_y + 1)
    return (current_x + direction[0], current_y - 1), (current_x + direction[0], current_y)


def interact_with_container(current, direction, matrix):
    if direction[0] == 0:  # horizontal moving
        new_x, new_y = current[0] + direction[0], current[1] + direction[1]
        while matrix[new_x][new_y] in ["[", "]"]:
            new_x, new_y = new_x + direction[0], new_y + direction[1]
        if matrix[new_x][new_y] == "#":
            return current
        while (new_x, new_y) != current:
            new_x, new_y = new_x - direction[0], new_y - direction[1]
            move_to((new_x, new_y), direction, matrix, matrix[new_x][new_y])
        return update_cords_with_direction(current, direction)

    linked_containers = [cords_of_next_containers(current, direction, matrix)]
    index = 0

    while index < len(linked_containers):
        container = linked_containers[index]
        left_bracket, right_bracket = container[0], container[1]
        new_x_left_bracket, new_y_left_bracket = update_cords_with_direction(left_bracket, direction)
        new_x_right_bracket, new_y_right_bracket = update_cords_with_direction(right_bracket, direction)
        if (matrix[new_x_left_bracket][new_y_left_bracket] == "#"
                or matrix[new_x_right_bracket][new_y_right_bracket] == "#"):
            return current
        if matrix[new_x_left_bracket][new_y_left_bracket] in ["[", "]"]:
            linked_containers.append(cords_of_next_containers(left_bracket, direction, matrix))

        if matrix[new_x_right_bracket][new_y_right_bracket] == "[":
            linked_containers.append(cords_of_next_containers(right_bracket, direction, matrix))

        index += 1

    index -= 1
    while index >= 0:
        container = linked_containers[index]
        left_bracket, right_bracket = container[0], container[1]
        move_to(left_bracket, direction, matrix, symbol="[")
        move_to(right_bracket, direction, matrix, symbol="]")
        index -= 1
    move_to(current, direction, matrix, "@")

    return update_cords_with_direction(current, direction)


def evaluate_map(matrix, commands, start):
    current = start
    for command in commands:
        direction = utils.COMMANDS[command]
        new_x, new_y = current[0] + direction[0], current[1] + direction[1]
        if matrix[new_x][new_y] == "#":
            continue
        if matrix[new_x][new_y] == ".":
            move_to(current, direction, matrix, "@")
            current = update_cords_with_direction(current, direction)
        if matrix[new_x][new_y] in ["[", "]"]:
            current = interact_with_container(current, direction, matrix)


def calculate_result(matrix):
    _result = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if matrix[i][j] == "[":
                _result += 100 * i + j
    return _result


def resolve():
    matrix, commands = read_from_file()
    start = get_start_pos(matrix)
    evaluate_map(matrix, commands, start)
    return calculate_result(matrix)


if __name__ == "__main__":
    start_time = time.time()
    result = resolve()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
