class Person:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class Schüler(Person):
    def __init__(self, name, isschüler=True):
        super().__init__(name)
        self.isschüler = isschüler

    def getSchüler(self):
        return self.isschüler


class Lehrer(Schüler):
    instanzcounter = 0
    def __init__(self, name, isschüler=False):
        super().__init__(name, isschüler)
        Lehrer.instanzcounter += 1
        self.counter = Lehrer.instanzcounter

    def aresomeLehrersAssholes(self):
        return True

    def getInstances(self):
        return self.counter


class Schule:
    def __init__(self, name):
        self.name = name
        self.schüler = []
        self.lehrer = []
        self.abtvorstand =[]

    def countLehrers(self):
        counter = len(self.lehrer)
        return counter


if __name__ == '__main__':
    htl = Schule("HTL")
    s1 = Schüler("Marcel")
    s2 = Schüler("Noah")
    l1 = Lehrer("Wixaning")
    l2 = Lehrer("Drurensohn")
    htl.schüler.append(s1)
    htl.schüler.append(s2)
    htl.lehrer.append(l1)

    print(htl.countLehrers())
    print(l2.getInstances())
    print(len(htl.schüler))