import random

from ServerforSSP import databaseshit, cleardb, app, getalldata, ApiClass, api

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
    useitdaddy = False
    hard = 0
    newround = True
    while(newround):
        eingabe = str(input("Schere, Stein, Papier, Echse oder Spock? "))
        menschanalyse[eingabe] += 1
        pc = random.choice(available)
        zufall = random.randint(0,1)
        if (hard >= 3):
            if (str(input("Schwereren Modus spielen? [j/n] ")) == "j"):
                maxmensch = max(menschanalyse, key=menschanalyse.get)
                available.remove(destroy(maxmensch)[zufall])
                pc = random.choice(available)
                useitdaddy = True
            else:
                useitdaddy = False

        if pc in destroy(eingabe):
            print("PC hat gewählt: " + pc)
            print("Du hast gewonnen!")
            win["Mensch"] += 1
            stats[eingabe] += 1
            stats[pc] += 1
        elif pc == eingabe:
            print("PC hat gewählt: " + pc)
            print("Gleiche Wahl!")
            win["U"] += 1
            stats[eingabe] += 1
            stats[pc] += 1
        else:
            print("PC hat gewählt: " + pc)
            print("Du hast verloren!")
            win["PC"] += 1
            stats[eingabe] += 1
            stats[pc] += 1

        hard = hard + 1
        if (useitdaddy == True):
            available.append(destroy(maxmensch)[zufall])

        jn = str(input("Weiterspielen? [j/n]: "))
        if jn == "n":
            menu()



def menu():
    exit = False
    print()
    print("Menu:")
    databaseshit(win)
    while exit == False:
        todo = input("Auswählen: /game, /resetdb, /stats oder /exit: ")
        if todo == "/game":
            game()
            databaseshit(win)
        elif todo == "/resetdb":
            cleardb("testwin")
        elif todo == "/stats":
            print()
            print("Gesamtstats der Sitzung: " + str(stats), "Win: " + str(win), "Menschanalyse: " + str(menschanalyse))
            print("All-time Wins: " + str(getalldata()))
            print()
        elif todo == "/exit":
            exit = True
    app.run()

if __name__ == "__main__":
    menu()
