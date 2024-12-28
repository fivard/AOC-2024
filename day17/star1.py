import time

test = False

if test:
    file_name = "simple_example.txt"
else:
    file_name = "example.txt"


def read_from_file():
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Initialize data structures
    registers = {}
    instructions = []

    for line in lines:
        line = line.strip()

        if line.startswith("Register"):  # Parse registers
            parts = line.split(":")
            register_name = parts[0].split()[-1]  # Extract A, B, or C
            register_value = int(parts[1].strip())  # Extract value
            registers[register_name] = register_value

        elif line.startswith("Program"):  # Parse program instructions
            instructions = list(map(int, line.split(":")[1].strip().split(",")))

    return registers, instructions


def combo_operand(num, registers):
    if 0 <= num <= 3:
        return num
    if num == 4:
        return registers["A"]
    if num == 5:
        return registers["B"]
    if num == 6:
        return registers["C"]
    if num == 7:
        raise Exception("SOMETHING WRONG")


def evaluate(registers, instructions):
    pointer = 0
    result = ""
    while pointer < len(instructions):
        # print(f"\nRegisters: {registers}")
        opcode, operand = instructions[pointer], instructions[pointer + 1]
        combo = combo_operand(operand, registers)
        # print(f"Opcode: {opcode}, operand: {operand}, combo: {combo}")
        if opcode == 0:
            registers["A"] = registers["A"] // (2 ** combo)
            pointer += 2
            continue
        if opcode == 1:
            registers["B"] = registers["B"] ^ operand
            pointer += 2
            continue
        if opcode == 2:
            registers["B"] = combo % 8
            pointer += 2
            continue
        if opcode == 3:
            if registers["A"] == 0:
                pointer += 2
                continue
            pointer = operand
            continue

        if opcode == 4:
            registers["B"] = registers["B"] ^ registers["C"]
            pointer += 2
            continue

        if opcode == 5:
            result += str(combo % 8) + ","
            pointer += 2
            continue

        if opcode == 6:
            registers["B"] = registers["A"] // (2 ** combo)
            pointer += 2
            continue

        if opcode == 7:
            registers["C"] = registers["A"] // (2 ** combo)
            pointer += 2
            continue

    return result

def resolve():
    registers, instructions = read_from_file()
    answer = evaluate(registers, instructions)

    return answer[:-1]


if __name__ == "__main__":
    start_time = time.time()
    result = resolve()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
