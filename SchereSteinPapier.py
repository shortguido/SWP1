import random

from ServerforSSP import databaseshit, cleardb

available = ["Stein","Schere","Papier","Echse","Spock"]
stats = {"Stein": 0, "Papier": 0, "Schere": 0, "Echse": 0, "Spock": 0}
menschanalyse = {"Stein": 0, "Papier": 0, "Schere": 0, "Echse": 0, "Spock": 0}
win = {"PC": 0, "Mensch": 0, "U": 0}
eingabe = None

def destroy(e):
    if e == "Schere":
        return "Papier","Echse"
    elif e == "Papier":
        return "Stein", "Spock"
    elif e == "Stein":
        return "Echse", "Schere"
    elif e == "Echse":
        return "Spock", "Papier"
    elif e == "Spock":
        return "Stein", "Schere"

def game():
    eingabe = str(input("Schere, Stein, Papier, Echse oder Spock? "))
    pc = random.choice(available)
    if pc in destroy(eingabe):
        print("PC hat gewählt: " + pc)
        print("Du hast gewonnen!")
        win["Mensch"] += 1
        stats[eingabe] += 1
        stats[pc] += 1
        menschanalyse[eingabe] += 1
    elif pc == eingabe:
        print("PC hat gewählt: " + pc)
        print("Gleiche Wahl!")
        win["U"] += 1
        stats[eingabe] += 1
        stats[pc] += 1
        menschanalyse[eingabe] += 1
    else:
        print("PC hat gewählt: " + pc)
        print("Du hast verloren!")
        win["PC"] += 1
        stats[eingabe] += 1
        stats[pc] += 1
        menschanalyse[eingabe] += 1


    jn = str(input("Weiterspielen? [j/n]: "))
    if jn == "j":
        game()
    else:
        menu()


def menu():
    exit = False
    print()
    print("Menu:")
    databaseshit(win)
    while exit == False:
        todo = input("Auswählen: /game, /resetdb, /stats or /exit: ")
        if todo == "/game":
            game()
            databaseshit(win)
        elif todo == "/resetdb":
            cleardb("testwin")
        elif todo == "/stats":
            print("Gesamtstats der Sitzung: " + str(stats), "Win: " + str(win), "Menschanalyse: " + str(menschanalyse))
        elif todo == "/exit":
            exit = True


if __name__ == "__main__":
    menu()
