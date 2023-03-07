import random


class ArrayList:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data = self.addtolist(self.data, value)

    def length(self):
        return self.getlength(self.data)

    def print_all(self):
        self.printelements(self.data)

    def addtolist(self, lst, value):
        new_list = []
        for element in lst:
            new_list.append(element)
        new_list.append(value)
        return new_list

    def getlength(self, lst):
        count = 0
        for element in lst:
            count += 1
        return count

    def printelements(self, lst):
        for element in lst:
            print(element)

if __name__ == "__main__":
    my_list = ArrayList()
    for i in range(10):
        my_list.add(random.randint(1, 100))
    print("Length of the list:", my_list.length())
    print("All elements of the list:")
    my_list.print_all()