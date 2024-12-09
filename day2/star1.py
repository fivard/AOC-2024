result = 0


def have_same_sign(num1, num2):
    return num1 * num2 > 0


def more_than_allowed_diff(num1, num2):
    return abs(num1 - num2) > 3


with open("example.txt", "r") as file:
    for report in file:
        levels = report.split()
        sign = int(levels[1]) - int(levels[0])
        unsafe = False
        for i in range(1, len(levels)):
            num1 = int(levels[i - 1])
            num2 = int(levels[i])
            if more_than_allowed_diff(num1, num2) or not have_same_sign(sign, num2 - num1):
                print(levels, more_than_allowed_diff(num1, num2), have_same_sign(sign, num2 - num1), sign, num2 - num1)
                unsafe = True
                break

        if not unsafe:
            print(levels)
            result += 1



print("ANSWER: ", result)
