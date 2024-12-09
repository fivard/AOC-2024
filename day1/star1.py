first_column = []
second_column = []

with open("example.txt", "r") as file:
    for line in file:
        columns = line.split()
        if len(columns) == 2:
            first_column.append(int(columns[0]))
            second_column.append(int(columns[1]))


sorted_first_column = sorted(first_column)
sorted_second_column = sorted(second_column)

result = 0
for i in range(0, len(sorted_first_column)):
    result += abs((sorted_second_column[i] - sorted_first_column[i]))

print("ANSWER: ", result)
