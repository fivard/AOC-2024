from linked_list import LinkedList

with open('example.txt', 'r') as file:
    content = file.read()
    stones = list(map(int, content.split()))
    link_list = LinkedList()
    for stone in stones:
        link_list.append(stone)

link_list.display()


def number_of_digits(node):
    return len(str(abs(node.value)))


def split_into_2_numbs(node):
    number_str = str(node.value)
    mid = len(number_str) // 2
    first_half = int(number_str[:mid])
    second_half = int(number_str[mid:])
    node.value = first_half
    node.append(second_half)
    return node.next


def arrange_stones(_length):
    current_node = link_list.head
    while current_node is not None:
        if current_node.value == 0:
            current_node.value = 1
        elif number_of_digits(current_node) % 2 == 0:
            current_node = split_into_2_numbs(current_node)
            _length += 1
        else:
            current_node.value *= 2024
        current_node = current_node.next
    return _length
    # link_list.display()
    # print(len(link_list))


length = len(stones)
for i in range(75):
    print(i, length)
    length = arrange_stones(length)

print(len(link_list))
