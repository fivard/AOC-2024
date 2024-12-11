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


def check_update(list_to_check):
    index_to_check = len(list_to_check) - 1
    while index_to_check > 0:
        index_of_set_to_check_in = index_to_check - 1
        while index_of_set_to_check_in >= 0:
            set_to_check = list_to_check[index_of_set_to_check_in]
            if set_to_check not in graph or list_to_check[index_to_check] not in graph[list_to_check[index_of_set_to_check_in]]:
                return 0
            index_of_set_to_check_in -= 1
        index_to_check -= 1
    # print(list_to_check)
    return list_to_check[len(list_to_check) // 2]


# print(graph)
res = 0
for list_to_check in lists_to_check:
    res += check_update(list_to_check)

print(res)
