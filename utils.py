
def beautiful_print(_map):
    for row in _map:
        for column in row:
            print(column, end="")
        print()


COMMANDS = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0)
}

COMMON_DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]