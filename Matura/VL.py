class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Vl:
    def __init__(self):
        self.head = None

    def append(self, value):
        current = self.head
        if self.head is None:
            self.head = Node(value)
            return
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def length(self):
        counter = 0
        current = self.head
        if current is None:
            return 0
        while current.next is not None:
            current = current.next
            counter += 1
        return counter

    def display(self):
        current = self.head
        s = "["
        if current is None:
            return print("[]")
        while current is not None:
            s = s + str(current.value) + ", "
            current = current.next
        return print(s[:-2] + "]")
        print()

    def remove(self, value):
        current = self.head
        if current.value == value:
            current.next = current.next.next
            return
        while current.next is not None and current.next.value != value:
            current = current.next
        current.next = current.next.next


if __name__ == '__main__':
    list = Vl()
    list.append(8)
    list.append(8)
    list.append(9)
    list.append(8)
    list.display()
    list.remove(9)
    list.display()
