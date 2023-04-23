import random

words = ["Hallo", "Welt", "Python", "Liste", "Programmieren", "Computer"]

def getUserWord(words):
    underscore = ""
    save =[]
    word = random.choice(words)
    print("The length of the picked word by the pc is: " + str(len(word)))
    for i in range(len(word)):
        underscore = underscore + "_"


    while(underscore != word):
        inpu = input("Guess a letter: ")

        while inpu in save:
            inpu = input("Already guessed! Guess another letter: ")
        save.append(inpu)

        for i in range(len(word)):
            if inpu == word[i]:
                underscore = underscore[:i] + inpu + underscore[i+1:]
        print(underscore)

    print("That is correct, the word was " + word + "!")


def check(inpu, word, underscore):
    pass


if __name__ == '__main__':
    getUserWord(words)