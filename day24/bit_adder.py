
a = "1101"
b = "1111"


def binary_addition(_a, _b):
    result = ""
    a_reversed, b_reversed = _a[::-1], _b[::-1]
    cin = 0
    for i in range(len(a_reversed)):
        a_i, b_i = int(a_reversed[i]), int(b_reversed[i])
        result += str((a_i ^ b_i) ^ cin)
        cin = a_i & b_i | cin & (a_i ^ b_i)
    result += str(cin)
    return result[::-1]


print(f"Adding {int(a, 2)} and {int(b, 2)} = {int(binary_addition(a, b), 2)}")
