import random
pc = random.choice(["Stein","Schere","Papier","Echse","Spock"])
stats = {"Stein": 0, "Papier": 0, "Schere": 0, "Echse": 0, "Spock": 0}
menschanalyse = {"Stein": 0, "Papier": 0, "Schere": 0, "Echse": 0, "Spock": 0}
win = {"PC": 0, "Mensch": 0, "U": 0}

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
    if pc in destroy(eingabe):
        print("PC hat gewählt: " + pc)
        print("Du hast gewonnen!")
    elif pc == eingabe:
        print("PC hat gewählt: " + pc)
        print("Gleiche Wahl!")
    else:
        print("PC hat gewählt: " + pc)
        print("Du hast verloren!")

    jn = str(input("Weiterspielen? [j/n]: "))
    if jn == "j":
        game()
    else:
        exit()



if __name__ == "__main__":
    game()
