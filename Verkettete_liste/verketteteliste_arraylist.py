import copy


class ArrayList:
    def __init__(self):
        self.platz = 10
        self.position = 0
        self.data = [None] * self.platz

    def add(self, value):
        self.macheplatz()
        self.data[self.position] = value
        self.position += 1


    def macheplatz(self):
        if self.position == self.platz:
            self.platz *= 2
            neuedata = copy.deepcopy(self.data)
            for i in range(self.position, self.platz):
                neuedata += [None]
            self.data = neuedata
            return
        if self.position+1 <= self.platz//2:
            for i in range(self.platz//2, self.platz):
                self.data.remove(None)
            self.platz = self.platz // 2


    def remove(self, value):
        finderpos = 0
        while self.data[finderpos] is not value:
            finderpos += 1
        while self.data[finderpos + 1] is not None:
            self.data[finderpos] = self.data[finderpos + 1]
            finderpos += 1
        self.data[finderpos] = None
        self.position -= 1


    def __str__(self):
        return print(str(self.data))

if __name__ == '__main__':
    al = ArrayList()
    al.add(67)
    al.add(6)
    al.add(45)
    al.__str__()
    al.remove(6)
    al.__str__()
    al.add("Hallo")
    al.__str__()