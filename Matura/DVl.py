class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DVl:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        current = self.head
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        while current.next is not None:
            current = current.next
        current.next = Node(value)
        self.tail = current.next
        self.tail.prev = current

    def display(self):
        if self.head is None:
            return print("[]")
        current = self.head
        s = "["
        while current is not None:
            s = s + str(current.value) + ", "
            current = current.next
        print(s[:-2] + "]")
        s = "["
        current = self.tail
        while current is not None:
            s = s + str(current.value) + ", "
            current = current.prev
        return print(s[:-2] + "]")
        print()

if __name__ == '__main__':
    lst = DVl()
    lst.append(67)
    lst.append(436)
    lst.append(23)
    lst.append(3)

    lst.display()


