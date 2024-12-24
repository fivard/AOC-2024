import time


test = False


if test:
    file_name = "simple_example.txt"
else:
    file_name = "example.txt"


def read_from_file():
    data = {}
    operations = []
    with open(file_name, "r") as file:
        for line in file:
            # Clean and skip empty lines
            line = line.strip()
            if not line:
                continue

            # Split into key-value or operation
            if ":" in line:  # Key-value pair
                key, value = line.split(":")
                data[key.strip()] = int(value.strip())
            else:  # Operation line
                operations.append(line.split())

    return data, sorted(operations, key=lambda x: x[0], reverse=True)

wires = []


def get_answers(operations, data):
    unresolved_operations = []

    for operation in operations:
        operand1 = operation[0]
        operand2 = operation[2]
        target = operation[4]
        operator = operation[1]

        if operand1 not in data.keys() or operand2 not in data.keys():
            unresolved_operations.append(operation)
            continue

        if "OR" == operator:
            data[target] = data[operand1] | data[operand2]
        elif "AND" == operator:
            data[target] = data[operand1] & data[operand2]
        elif "XOR" == operator:
            data[target] = data[operand1] ^ data[operand2]

    if unresolved_operations:
        return get_answers(unresolved_operations, data)
    return data


def resolve():
    data, operations = read_from_file()
    sorted_x = sorted({key: value for key, value in data.items() if key.startswith("x")}.items(), reverse=True)
    binary_x = "".join([str(num[1]) for num in sorted_x])
    sorted_y = sorted({key: value for key, value in data.items() if key.startswith("y")}.items(), reverse=True)
    binary_y = "".join([str(num[1]) for num in sorted_y])
    data.update(get_answers(operations, data))
    sorted_z = sorted({key: value for key, value in data.items() if key.startswith("z")}.items(), reverse=True)
    binary_z = "".join([str(num[1]) for num in sorted_z])
    print("X:\t", binary_x, "\t", int(binary_x, 2))
    print("Y:\t", binary_y, "\t", int(binary_y, 2))
    print("X+Y:", bin(int(binary_x, 2) + int(binary_y, 2))[2:], "\t", int(binary_x, 2) + int(binary_y, 2))
    print("Z:\t", binary_z, "\t", int(binary_z, 2))
    return int(binary_z, 2)

if __name__ == "__main__":
    start_time = time.time()
    result = resolve()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")





