import random
eingabe = str(input("Schere, Stein, Papier, Echse oder Spock?"))
pc = random.randint(1,5)
stats = {"Stein": 0, "Papier": 0, "Schere": 0, "Echse": 0, "Spock": 0}
menschanalyse = {"Stein": 0, "Papier": 0, "Schere": 0, "Echse": 0, "Spock": 0}
win = {"PC": 0, "Mensch": 0, "U": 0}

def checkwinner(pc, e):
    if pc == 1:
        pc = "Schere"
    elif pc == 2:
        pc == "Stein"
    elif pc == 3:
        pc == "Papier"
    elif pc == 4:
        pc == "Echse"
    elif pc == 5:
        pc == "Spock"

    #Check for winner
    if e == pc:
        print("Draw")
        stats["U"] += 1
        return
    if e == "Schere":
        menschanalyse["Schere"] += 1
        if pc == "Papier":
            print("Schere schneidet Papier")
            stats["Schere"] += 1
            return
        elif pc == "Stein":
            print("Stein schlägt Schere")
            stats["Stein"] += 1
        elif pc == "Vollkatastrophe":
            pass



if __name__ == "__main__":
    pass