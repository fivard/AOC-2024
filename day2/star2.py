def have_same_sign(num1, num2):
    return num1 * num2 > 0


def more_than_allowed_diff(num1, num2):
    return abs(num1 - num2) > 3 or abs(num1 - num2) < 1


def is_report_safe(levels, second_try=False):
    sign = int(levels[1]) - int(levels[0])
    for i in range(1, len(levels)):
        num1 = int(levels[i - 1])
        num2 = int(levels[i])
        if more_than_allowed_diff(num1, num2) or not have_same_sign(sign, num2 - num1):
            if second_try:
                return False
            levels_copy_1 = levels.copy()
            levels_copy_1.pop(i)
            safe_1 = is_report_safe(levels_copy_1, second_try=True)

            levels_copy_2 = levels.copy()
            levels_copy_2.pop(i - 1)
            safe_2 = is_report_safe(levels_copy_2, second_try=True)

            safe_3 = False
            if i == 2:
                levels_copy_3 = levels.copy()
                levels_copy_3.pop(0)
                safe_3 = is_report_safe(levels_copy_3, second_try=True)

            return safe_1 or safe_2 or safe_3

    return True


with open("example.txt", "r") as file:
    result = 0
    for report in file:
        levels = report.split()
        safe = is_report_safe(levels)
        if safe:
            result += 1

print("ANSWER: ", result)
