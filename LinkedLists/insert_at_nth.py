
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def Insert(value, position, head):
    newNode = Node(value)

    if (position == 1):
        newNode.next = head
        head = newNode
        return head

    current = head
    i = 0
    while (i < position-2):
        current = current.next
        i += 1
    newNode.next = current.next
    current.next = newNode

    return


def printList(head):
    while (head):
        print(head.data)
        head = head.next


head = None
while True:
    head = Insert(1, 1, head)
    Insert(2, 2, head)
    Insert(3, 3, head)
    head = Insert(4, 1, head)
    Insert(5, 3, head)
    printList(head)
    break
