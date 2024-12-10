data = []
with open('simple_example.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(':')
        if len(parts) > 1:
            key = int(parts[0].strip())
            values = list(map(int, parts[1].strip().split()))
            data.append((key, values))

for key, values in data:
    print(f"{key}: {values}")


def is_valid(goal_value, arr):
    def bfs(cur_ind, current_check_sum):
        if cur_ind == len(arr) - 1:
            if current_check_sum + arr[cur_ind] == goal_value or current_check_sum * arr[cur_ind] == goal_value:
                return True
            return False

        val_1 = bfs(cur_ind + 1, current_check_sum + arr[cur_ind])
        val_2 = bfs(cur_ind + 1, current_check_sum * arr[cur_ind])
        return val_1 or val_2

    valid = bfs(cur_ind=1, current_check_sum=arr[0])
    return valid

res = 0
for test_value, array_of_numbers in data:
    if is_valid(test_value, array_of_numbers):
        res += test_value

print(res)
