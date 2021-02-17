# Insert Node to end of linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    while (head):
        print(head.data)
        head = head.next


temp = input('Please enter the first number: ')
head = Node(temp)
current = head
i = 0
while (i != 4):
    nextNum = input('Please enter a number: ')
    tempNum = Node(nextNum)
    current.next = tempNum
    current = tempNum
    i += 1
    printList(head)


# Reverse the linked list
def reverseList(head):
    prev = None
    while (head):
        current = head
        head = head.next
        current.next = prev
        prev = current

    return prev


x = reverseList(head)

print("Reversed: ")
printList(x)
