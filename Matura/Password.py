import random
import string


def getPWD(length):
    pwd = ""
    sonderzeichen = ['!', '@', '#', '$', '%', '&', '*', "+", "-", "#"]
    for i in range(length):
        noe = random.randrange(0, 3)
        if (noe == 0):
            rsl = random.choice(string.ascii_letters)
            pwd = pwd + rsl
        elif (noe == 1):
            s = random.choice(sonderzeichen)
            pwd = pwd + s
        else:
            rn = random.randrange(0, 10)
            pwd = pwd + str(rn)

    return pwd


if __name__ == '__main__':
    length = int(input("How long should the pwd be? "))
    print("Your generated Password is: " + getPWD(length))
