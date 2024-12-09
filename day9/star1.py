with open('example.txt', 'r') as file:
    NUMBER = file.read()

print(NUMBER)

# we gonna do it in 2 * O(N)= O(N)
main_hash_id_with_count = {i: int(NUMBER[i*2]) for i in range(0, len(NUMBER)//2 + 1)}
print(main_hash_id_with_count)


def calculate_sum_of_mult(temp_id_to_calculate, start, count):
    temp_result = 0
    for i in range(start, start+count):
        temp_result += i * temp_id_to_calculate
    main_hash_id_with_count[temp_id_to_calculate] -= count
    return temp_result


def get_max_id_to_calculate():
    for key in sorted(main_hash_id_with_count.keys(), reverse=True):
        if main_hash_id_with_count[key] > 0:
            return key
    raise Exception


RESULT = 0
main_index = 0
for i in range(0, len(NUMBER)):
    if i % 2 == 0:
        id_to_calculate = i//2
        number_of_additions = main_hash_id_with_count[id_to_calculate]
        if number_of_additions == 0:
            continue
        RESULT += calculate_sum_of_mult(id_to_calculate, main_index, number_of_additions)
        main_index += number_of_additions
    elif i % 2 == 1:
        count_of_free_space = int(NUMBER[i])
        while count_of_free_space > 0:
            try:
                id_to_calculate = get_max_id_to_calculate()
            except:
                break
            number_of_additions = min(count_of_free_space, main_hash_id_with_count[id_to_calculate])
            count_of_free_space -= number_of_additions
            RESULT += calculate_sum_of_mult(id_to_calculate, main_index, number_of_additions)
            main_index += number_of_additions

print(RESULT)