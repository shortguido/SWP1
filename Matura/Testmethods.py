def getLetterCount(list):
    count = 0
    list2 = []
    list3 = []
    for i in range(len(list)):
        word = list[i]
        for i in range(len(word)):
            count += 1

        list2.append(word)
        list2.append(count)
        count = 0
        tup = tuple(list2)

        list3.append(tup)
        list3.sort(key=tup[1], reverse=True)
        list2.clear()
    print(list3)
    list3.sort()
    return list3


def multiply(f, num):
    return f(num)


def sortInts(li):
    countitems = len(li)
    mean = 0
    li.sort(reverse=True)
    print("List: " + str(li))

    # Median
    if countitems % 2 == 0:
        a = str((li[int(countitems / 2)] + li[int((countitems / 2) - 1)]) / 2)
        print("Median " + a)
    else:
        a = str(li[int(countitems / 2)])
        print("Median: " + a)

    # Mean
    for i in li:
        mean = mean + i
    print("Mean: " + str(mean / countitems))

    # Range
    print("Range: " + str(li[0] - li[countitems - 1]))

    # Frequency
    dict = {}
    for i in li:
        dict[i] = 0

    for i in li:
        dict[i] += 1
    print("Frequency " + str(dict))


class LinkedList:

    def __init__(self):
        self.head = None

    def length(self):
        lencounter = 0
        current = self.head
        while current is not None:
            lencounter += 1
            current = current.next
        return lencounter

    def add(self, value):
        current = self.head
        if current is None:
            self.head = Node(value)
            return
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def display(self):
        current = self.head
        if current is None:
            return 0
        while current is not None:
            print(current.value, end=", ")
            current = current.next
        print()

    def remove(self, position):
        current = self.head
        if current is None:
            return
        if position == 0:
            self.head = current.next
        for i in range(position - 1):
            if current.next is None:
                return
            current = current.next

        if current.next is None:
            return
        current.next = current.next.next


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Person:
    def __init__(self, name, geschlecht):
        self.name = name
        self.geschlecht = geschlecht


class Mitarbeiter(Person):
    def __init__(self, name, geschlecht, abteilung):
        super().__init__(name, geschlecht)
        self.abteilung = abteilung


class Gruppenleiter(Mitarbeiter):
    def __init__(self, name, geschlecht, abteilung, leiten):
        super().__init__(name, geschlecht, abteilung)
        self.leiten = leiten


class Abteilung:
    def __int__(self, name):
        self.name = name


class Firma:
    def __init__(self):
        self.li_mi = []
        self.li_abt = []
        self.li_gl = []

    def countma(self, mi, gl):
        return len(mi) + len(gl)

    def percentage(self, mi, gl):
        malecount = 0
        femcount = 0
        for elm in mi:
            if elm.geschlecht == 1:
                malecount += 1
            else:
                femcount += 1

        for elm in gl:
            if elm.geschlecht == 1:
                malecount += 1
            else:
                femcount += 1

        all = femcount + malecount
        femper = femcount / all
        maleper = malecount / all
        return "Female Percentage: " + str(femper * 100) + ", Male Percentage: " + str(maleper * 100)




if __name__ == '__main__':
    nums = [2, 3, 4, 5, 5, 7, 8, 5, 32, 3, 5, 6, 4, 3, 2, 6, ]
    sortInts(nums)

    ll = LinkedList()
    ll.add(4)
    ll.add(1)
    ll.add(5)
    ll.add(7)
    ll.add(9)
    ll.add(10)
    ll.remove(3)

    a1 = Abteilung
    m1 = Mitarbeiter("Hannes", 1, a1)
    m2 = Mitarbeiter("Jürgen", 1, a1)
    g1 = Gruppenleiter("Andi", 0, a1, True)

    firma = Firma()
    firma.li_gl.append(g1)
    firma.li_mi.append(m1)
    firma.li_mi.append(m2)
    firma.li_abt.append(a1)

    # Wv MA:
    print("MACount: " + str(firma.countma(firma.li_mi, firma.li_gl)))

    # Wv Abteilungen:
    print("AbtCount: " + str(len(firma.li_abt)))

    # Prozentanteil männer frauen
    print("Prozentanteil: " + firma.percentage(firma.li_mi, firma.li_gl))

    # ll.display()
# print(ll.length())
