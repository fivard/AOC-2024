import time
from collections import defaultdict, deque


test = False


if test:
    file_name = "simple_example.txt"
else:
    file_name = "example.txt"

with open(file_name, "r") as file:
    list_of_given_secrets_number = [int(line.strip()) for line in file]


result = []
result_2 = defaultdict(int)
start_time = time.time()

for secret_number in list_of_given_secrets_number:
    num = secret_number
    last_digit, changes = num % 10, deque(maxlen=4)
    consecutives = {}

    for _ in range(3):
        num = (num ^ (num << 6)) & 16777215
        num = (num ^ (num >> 5)) & 16777215
        num = (num ^ (num << 11)) & 16777215
        changes.append(num % 10 - last_digit)
        last_digit = num % 10

    for _ in range(1997):
        num = (num ^ (num << 6)) & 16777215
        num = (num ^ (num >> 5)) & 16777215
        num = (num ^ (num << 11)) & 16777215
        changes.append(num % 10 - last_digit)
        last_digit = num % 10
        if tuple(changes) not in consecutives:
            consecutives[tuple(changes)] = last_digit

    result.append(num)
    for four_tuple, banana in consecutives.items():
        result_2[four_tuple] += banana


print(sum(result))
print(max(result_2.values()))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")







