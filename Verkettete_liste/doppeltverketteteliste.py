import random


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node

    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def display(self):
        # gibt alle Elemente der Liste aus
        # zuerst von vorn nach hinten,
        # dann mit prev von hinten nach vorne
        current = self.head
        while current is not None:
            print(current.value, end=", ")
            current = current.next
        print()
        current = self.head
        while current.next is not None:
            current = current.next
        while current is not None:
            print(current.value, end=", ")
            current = current.prev
        print()


    def display2(self):
        current = self.head

        if current is None:
            return
        while current is not None:
            print(current.value, end=", ")
            current = current.next
        print()
        current = self.head
        while current.next is not None:
            current = current.next
        while current is not None:
            print(current.value, end=", ")
            current = current.prev
        print()

    def append2(self, value):
        newval = Node(value)
        if self.head is None:
            self.head = newval
        else:
            self.tail.next = newval
            newval.prev = self.tail
        self.tail = newval

    def remove(self, value):
        current = self.head
        if current is not None and current.value == value:
            self.head = current.next
            if self.head is not None:
                self.head.prev = None
            return

        while current is not None:
            if current.value is value:
                prevnode = current.prev
                nextnode = current.next
                if prevnode is not None:
                    prevnode.next = nextnode
                if nextnode is not None:
                    nextnode.prev = prevnode
                if current is self.tail:
                    current = prevnode

            current = current.next





class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    for i in range(5):
        doubly_linked_list.append2(random.randint(1, 100))

    doubly_linked_list.append(100)
    doubly_linked_list.append(334)
    doubly_linked_list.display2()
    doubly_linked_list.remove(100)
    doubly_linked_list.display2()



    print("Länge der Datenstruktur:", doubly_linked_list.length())