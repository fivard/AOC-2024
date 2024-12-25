import time


test = False


if test:
    file_name = "simple_example.txt"
else:
    file_name = "example.txt"


def read_from_file():
    with open(file_name, 'r') as file:
        data = file.read().strip().split('\n\n')

    locks = []
    keys = []

    for rect in data:
        lines = rect.split('\n')
        columns = len(lines[0])

        column_heights = [sum(1 for row in lines if row[col] == '#') - 1 for col in range(columns)]

        if lines[0].count('#') > 0:
            locks.append(column_heights)
        if lines[-1].count('#') > 0:
            keys.append(column_heights)

    return locks, keys

def matches(lock, key):
    for i in range(len(lock)):
        if lock[i] + key[i] > 5:
            return False

    return True


def resolve():
    locks, keys = read_from_file()
    unique_pair = set()
    for lock_id in range(len(locks)):
        for key_id in range(len(keys)):
            if matches(locks[lock_id], keys[key_id]) and (lock_id, key_id) not in unique_pair:
                unique_pair.add((lock_id, key_id))

    return len(unique_pair)


if __name__ == "__main__":
    start_time = time.time()
    result = resolve()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")





