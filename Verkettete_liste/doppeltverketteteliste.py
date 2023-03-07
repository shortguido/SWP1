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

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    for i in range(5):
        doubly_linked_list.append(random.randint(1, 100))

    doubly_linked_list.display()
    print("Länge der Datenstruktur:", doubly_linked_list.length())