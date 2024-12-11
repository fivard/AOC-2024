
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def append(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.next
        self.next = new_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
