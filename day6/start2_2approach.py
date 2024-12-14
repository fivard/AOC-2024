# 1688
# 47 82
with open("example.txt", "r") as file:
    matrix = [list(line.strip()) for line in file if line.strip()]

MAX_I = len(matrix)
MAX_J = len(matrix[0])


def beautiful_print():
    print("\n-----------------------------------")
    for row in matrix:
        print(''.join(row))


def get_next_cords(_i, _j, given_direction) -> (int, int):
    return _i + given_direction[0], _j + given_direction[1]


def make_step(given_i, given_j, _direction) -> (int, int, (int, int)):
    _next_i, _next_j = get_next_cords(given_i, given_j, _direction)

    while 0 <= _next_i < MAX_I and 0 <= _next_j < MAX_J and matrix[_next_i][_next_j] == "#":
        _direction = turn_right(_direction)
        _next_i, _next_j = get_next_cords(given_i, given_j, _direction)

    return _next_i, _next_j, _direction


def turn_right(given_direction):
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]
    return directions[(directions.index(given_direction) + 1) % 4]


def check_loop(_i, _j, given_direction):
    visited_cell = set()
    temp_i, temp_j, _direction = _i, _j, given_direction

    while 0 <= temp_i < MAX_I and 0 <= temp_j < MAX_J:
        if (temp_i, temp_j, _direction) in visited_cell:
            return True
        visited_cell.add((temp_i, temp_j, _direction))
        temp_i, temp_j, _direction = make_step(temp_i, temp_j, _direction)

    return False


def is_next_cell_can_be_an_obstl(given_i, given_j, given_direction):
    # get cords for the next step - cords for obstcl
    _next_i, _next_j = get_next_cords(given_i, given_j, given_direction)

    if _next_i == 24 and _next_j == 36:
        a = 1
    # check if NEXT cords are in bounds and if there is no an obstcl
    if (_next_i < 0 or _next_i >= MAX_I or _next_j < 0 or _next_j >= MAX_J or
            matrix[_next_i][_next_j] == "#" or (_next_i, _next_j) in cords_for_obstcl):
        # no space for a new obstcl
        return False

    if (_next_i, _next_j) not in trace:
        print("NOT IN TRACE PATH: ", (_next_i, _next_j))

    # set new temp obstcl
    matrix[_next_i][_next_j] = "#"
    is_loop = check_loop(given_i, given_j, given_direction)
    if is_loop:
        print(f"({_next_i}, {_next_j}), ")

    # remove new temp obstcl
    matrix[_next_i][_next_j] = "."
    return is_loop


if __name__ == "__main__":
    cur_i, cur_j = 0, 0
    cords_for_obstcl = set()

    res = 0
    trace = set()
    direction = (-1, 0)

    for i in range(MAX_I):
        for j in range(MAX_J):
            if matrix[i][j] == '^':
                cur_i = i
                cur_j = j
                saved_i, saved_j = i, j
                cords_for_obstcl.add((cur_i, cur_j))
                break

    while 0 <= cur_i < MAX_I and 0 <= cur_j < MAX_J:
        if (cur_i, cur_j) not in trace:
            trace.add((cur_i, cur_j))

        cur_i, cur_j, direction = make_step(cur_i, cur_j, direction)

    print((46, 78) in trace)
    print("Trace long: ", len(trace))

    trace.remove((saved_i, saved_j))
    while trace:
        visited_cell = set()
        cur_i, cur_j, direction = saved_i, saved_j, (-1, 0)
        obstcl_cords = trace.pop()
        matrix[obstcl_cords[0]][obstcl_cords[1]] = "#"

        while 0 <= cur_i < MAX_I and 0 <= cur_j < MAX_J:
            if (cur_i, cur_j, direction) in visited_cell:
                res += 1
                break
            visited_cell.add((cur_i, cur_j, direction))
            cur_i, cur_j, direction = make_step(cur_i, cur_j, direction)

        matrix[obstcl_cords[0]][obstcl_cords[1]] = "."

    print("RES: ", res)

