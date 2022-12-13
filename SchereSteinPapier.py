import random
import mysql.connector
from flask import Flask
import json

db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="statistikaustria"
    )

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
        print("Gesamtstats: " + str(stats), "Win/Loss/Draw: " + str(win), "Menschanalyse: " + str(menschanalyse))


def databaseshit():
    mycurs = db.cursor()
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in win.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in win.values())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('testwin', columns, values)
    mycurs.execute(sql)
    db.commit()
    print(sql)


def getdata():
    mycurs = db.cursor()
    mycurs.execute("SELECT * FROM testwin")
    result = mycurs.fetchall()
    field_names = [i[0] for i in mycurs.description]

    mycurs.execute(f'SELECT {gew} FROM testwin where name = "Mensch"')
    selectionplayer = [int(record[0]) for record in mycurs.fetchall()]
    selectionplayer = selectionplayer[0]
    mycurs.execute(f'SELECT {gewcom} FROM testwin where name = "PC"')
    selectioncomp = [int(record[0]) for record in mycurs.fetchall()]
    selectioncomp = selectioncomp[0]
    return field_names + result + selectioncomp + selectionplayer


app = Flask(__name__)
@app.route('/')
def home():
    return getdata()


if __name__ == "__main__":
    game()
    databaseshit()
    app.run()