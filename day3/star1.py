def check_and_mult(index_of_m_letter):
    if content[index_of_m_letter:index_of_m_letter+4] != "mul(":
        return False, 0
    str_to_check = content[index_of_m_letter+4:index_of_m_letter+12]
    print(str_to_check)
    ind_of_coma = str_to_check.find(",")
    ind_of_close = str_to_check.find(")")
    print(ind_of_coma, ind_of_close)
    if ind_of_coma > ind_of_close:
        return False, 0
    first_num = str_to_check[0:ind_of_coma]
    second_num = str_to_check[ind_of_coma+1:ind_of_close]

    print(f"First:{first_num}, second:{second_num}")
    if len(first_num) > 3 or len(second_num) > 3:
        return False, 0

    for char in first_num:
        if not char.isdigit():
            return False, 0

    first_num = int(first_num)

    for char in second_num:
        if not char.isdigit():
            return False, 0

    second_num = int(second_num)

    return True, first_num * second_num


with open('example.txt', 'r') as file:
    content = file.read()

result = 0
for i in range(0, len(content)):
    if content[i] == 'm':
        is_valid, mult = check_and_mult(i)
        if is_valid:
            result += mult

print("ANSWER: ", result)

