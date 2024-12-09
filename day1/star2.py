first_column = []
my_hash = {}

with open("example.txt", "r") as file:
    for line in file:
        columns = line.split()
        if len(columns) == 2:
            first_number, second_number = int(columns[0]), int(columns[1])
            first_column.append(first_number)
            my_hash[second_number] = 1 if second_number not in my_hash.keys() else my_hash[second_number] + 1

result = 0
for i in range(0, len(first_column)):
    num = first_column[i]
    result += my_hash.get(num, 0) * num

print("ANSWER: ", result)
