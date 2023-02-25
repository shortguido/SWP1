import random


class LinkedList:
    def __init__(self):  # wird automatisch aufgerufen, wenn eine instanz in der klasse erstellt wird
        self.head = None  # head speichert den anfangswert liste

    def append(self, value):
        # fügt einen Wert am ende der liste hinzu
        if self.head is None:  # falls anfangswert null, wird der head auf eine neue instanz von Node gesetzt die den wert value übergeben bekommt
            self.head = Node(value)
            return
        current = self.head
        while current.next is not None:  # current so lange durch liste bis current.next auf none zeigt
            current = current.next
        current.next = Node(value)  # dann auf neue instanz von node setzen

    def length(self):
        # gitb länge von liste zurück
        count = 0
        current = self.head
        while current is not None:  # jedes element in der liste zählen -> falls current 0 count = 0
            count += 1
            current = current.next
        return count

    def display(self):
        # gibt alle elemente der liste aus
        current = self.head
        while current is not None:
            print(current.value, end=", ")
            current = current.next
        print()


class Node:  # eigene Klasse die jedes Element der verketteten Liste darstellt
    def __init__(self, value):  # speichert value als instanzvariable
        self.value = value
        self.next = None  # next verweist auf das nächste objekt in der liste


def decorator(func):
    def wrapper(*args,**kwargs):
        print(f"Folgende funktion {func} zweimal ausgeführt:")
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@decorator
def hallo():
    print("Hallo")


if __name__ == '__main__':
    hallo()
    # linked_list = LinkedList()
    # for i in range(5):
    #    linked_list.append(random.randint(1, 100))

    # linked_list.display()
    # print("Länge der Datenstruktur:", linked_list.length())
