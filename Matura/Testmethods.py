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
        list3.sort(key=getTup, reverse=True)
        list2.clear()
    print(list3)
    list3.sort()
    return list3


def multiply(f, num):
    return f(num)

def getTup(tup):
    return tup[1]


if __name__ == '__main__':
    nums = [2, 3, 4, 5]
    f = lambda x: x * x
    list = ['Python', 'ist', 'eine', 'tolle', 'Programmiersprache']
    getLetterCount(list)
    print(multiply(f, 5))
