graph = {}
lists_to_check = []

with open("example.txt", "r") as file:
    for line in file:
        if "|" in line:
            start, end = int(line[0:2]), int(line[3:5])
            try:
                graph[start].add(end)
            except KeyError:
                graph[start] = {end}
        elif "," in line:
            nums = line.strip()
            lists_to_check.append([int(x) for x in nums.split(',') if x])


def validate_update(list_to_check):
    index_to_check = len(list_to_check) - 1
    incorrect = False
    while index_to_check > 0:
        num_to_check = list_to_check[index_to_check]
        index_of_prev_number_to_check = index_to_check - 1
        min_index_to_insert = index_to_check

        while index_of_prev_number_to_check >= 0:
            prev_number_to_check = list_to_check[index_of_prev_number_to_check]
            if prev_number_to_check not in graph or num_to_check not in graph[prev_number_to_check]:
                min_index_to_insert = index_of_prev_number_to_check
                incorrect = True
            index_of_prev_number_to_check -= 1

        if index_to_check != min_index_to_insert:
            list_to_check.pop(index_to_check)
            list_to_check.insert(min_index_to_insert, num_to_check)
            index_to_check += 1
        index_to_check -= 1

    return list_to_check[len(list_to_check) // 2] if incorrect else 0


res = 0
for list_to_check in lists_to_check:
    res += validate_update(list_to_check)

print(res)
