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

    matrix = [list(row) for row in matrix_lines]
    commands = list("".join(commands_line))

    return matrix, commands


def get_start_pos(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "@":
                return i, j
    return None


def move_to(current, direction, matrix):
    new_x, new_y = current[0] + direction[0], current[1] + direction[1]
    matrix[new_x][new_y] = matrix[current[0]][current[1]]
    matrix[current[0]][current[1]] = "."


def update_current(current, direction):
    return current[0] + direction[0], current[1] + direction[1]


def evaluate_map(matrix, commands, start):
    current = start
    for command in commands:
        direction = utils.COMMANDS[command]
        new_x, new_y = current[0] + direction[0], current[1] + direction[1]
        if matrix[new_x][new_y] == "#":
            continue
        if matrix[new_x][new_y] == ".":
            move_to(current, direction, matrix)
            current = update_current(current, direction)
        if matrix[new_x][new_y] == "O":
            while matrix[new_x][new_y] == "O":
                new_x, new_y = new_x + direction[0], new_y + direction[1]
            if matrix[new_x][new_y] == "#":
                continue
            while (new_x, new_y) != current:
                new_x, new_y = new_x - direction[0], new_y - direction[1]
                move_to((new_x, new_y), direction, matrix)
            current = update_current(current, direction)


def calculate_result(matrix):
    result = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if matrix[i][j] == "O":
                result += 100*i + j
    return result


def resolve():
    matrix, commands = read_from_file()
    start = get_start_pos(matrix)
    # utils.beautiful_print(matrix)
    evaluate_map(matrix, commands, start)
    # utils.beautiful_print(matrix)
    return calculate_result(matrix)


if __name__ == "__main__":
    start_time = time.time()
    result = resolve()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")





