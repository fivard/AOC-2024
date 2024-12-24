

def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def find_gate(x_wire: str, y_wire: str, gate_type: str, configurations: list[str]):
    sub_str_a = f'{x_wire} {gate_type} {y_wire} -> '
    sub_str_b = f'{y_wire} {gate_type} {x_wire} -> '

    for config in configurations:
        if (sub_str_a in config) or (sub_str_b in config):
            return config.split(' -> ')[-1]


def swap_output_wires(wire_a: str, wire_b: str, configurations: list[str]):
    new_configurations = []

    for config in configurations:
        input_wires, output_wire = config.split(' -> ')

        if output_wire == wire_a:
            new_configurations.append(' -> '.join([input_wires] + [wire_b]))

        elif output_wire == wire_b:
            new_configurations.append(' -> '.join([input_wires] + [wire_a]))

        else:
            new_configurations.append(' -> '.join([input_wires] + [output_wire]))

    return new_configurations


def check_parallel_adders(configurations: list[str]):
    current_carry_wire = None
    swaps = []
    bit = 0

    while True:
        x_wire = f'x{bit:02d}'
        y_wire = f'y{bit:02d}'
        z_wire = f'z{bit:02d}'

        if bit == 0:
            current_carry_wire = find_gate(x_wire, y_wire, 'AND', configurations)
        else:
            ab_xor_gate = find_gate(x_wire, y_wire, 'XOR', configurations)
            ab_and_gate = find_gate(x_wire, y_wire, 'AND', configurations)

            cin_ab_xor_gate = find_gate(ab_xor_gate, current_carry_wire, 'XOR', configurations)
            if cin_ab_xor_gate is None:
                swaps.append(ab_xor_gate)
                swaps.append(ab_and_gate)
                configurations = swap_output_wires(ab_xor_gate, ab_and_gate, configurations)
                bit = 0
                continue

            if cin_ab_xor_gate != z_wire:
                swaps.append(cin_ab_xor_gate)
                swaps.append(z_wire)
                configurations = swap_output_wires(cin_ab_xor_gate, z_wire, configurations)
                bit = 0
                continue

            cin_ab_and_gate = find_gate(ab_xor_gate, current_carry_wire, 'AND', configurations)

            carry_wire = find_gate(ab_and_gate, cin_ab_and_gate, 'OR', configurations)
            current_carry_wire = carry_wire

        bit += 1
        if bit >= 45:
            break

    return swaps


def solution(lines: list[str]):
    divider = lines.index('')
    configurations = lines[divider + 1:]

    swaps = check_parallel_adders(configurations)
    return ','.join(sorted(swaps))


if __name__ == "__main__":
    import time
    print("Started finding solution")
    start_time = time.time()
    lines = read_input_file(file_path="example.txt")
    print("Result: ", solution(lines))
    end_time = time.time()
    elapsed_time = end_time - start_time
    # print(f"Result: {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")