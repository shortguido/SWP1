import random


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def countobjs(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count


    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    def all(self):
        if self.head is None:
            print("None")
        else:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next


class Howara:
    def __init__(self, name):
        self.name = name

    def hallo(self):
        print("Hallo")

class Howara2(Howara):
    def __init__(self, name, figgn):
        super().__init__(name)
        self.figgn = figgn

    def hi(self):
        print("hi")

class ABC(Howara2, Howara):
    def __init__(self, name, figgn, habidäri):
        super().__init__(name, figgn)
        self.habidäri = habidäri


if __name__ == '__main__':
    list1 = LinkedList()
    for i in range(10):
        list1.append(random.randint(1, 10))
    #list1.all()
    h2 = Howara2("Hitler", 0)
    print(h2.figgn)
    h = ABC("Heil", 0, "Drei")
    print(h.hallo())
    print(h.hi())

