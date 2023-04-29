def returnSumOfEvenNums(list):
    result = []
    for i in list:
        if isEven(i) == 0:
            result.append(i)

    return sum(result)


isEven = lambda num: num % 2

if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7, 8]
    print(returnSumOfEvenNums(list))
