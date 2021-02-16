# Basic implementation of singly-linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

head.next = second
second.next = third
third.next = fourth

temp = head
while (temp):
    print(temp.data)
    temp = temp.next
