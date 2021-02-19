class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        iterator = self.head
        llstring = ''

        while iterator:
            llstring += str(iterator.data) + '---> '
            iterator = iterator.next

        print(llstring)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_elmnt(self, index):
        # >= because indexes start at 0, so if is = length == 1 & index is 1, error because length of 1 only index would be [0]
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:  # remove head
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:  # stop at node prior to index
                itr.next = itr.next.next  # point to deleted elements.next
                break
            itr = itr.next
            count += 1

    def insert_at_nth(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)

            itr = itr.next
            count += 1


if __name__ == '__main__':
    list = LinkedList()
    list.insert_at_beginning(5)
    list.insert_at_beginning(89)
    list.insert_at_end(79)
    list.insert_at_end(1)
    list.print()
    list.insert_values(['hello', 'world', 'my', 'name', 'is', 'ming'])
    list.print()
    list.remove_elmnt(2)
    list.insert_at_nth(3, 'inserted_at_nth')
    list.print()
