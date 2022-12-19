from flask_restful import Api, Resource
import mysql.connector
from flask import Flask


db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="statistikaustria"
    )
#First db INSERT
mycurs = db.cursor()

def databaseshit(win):

    values = ','.join("'" + str(x).replace('/', '_') + "'" for x in win.values())
    wm = getdatafromrow()[1] + int(values[1])
    wc = getdatafromrow()[0] + int(values[5])
    draw = getdatafromrow()[2] + int(values[9])
    sql = f"UPDATE testwin SET Mensch = {wm}"
    sql2 = "UPDATE testwin SET PC = %s" % (wc)
    sql3 = "UPDATE testwin SET U = %s" % (draw)
    mycurs.execute(sql)
    mycurs.execute(sql2)
    mycurs.execute(sql3)
    db.commit()


def getdatafromrow():
    mycurs.execute('SELECT Mensch FROM testwin;')
    wm = [int(record[0]) for record in mycurs.fetchall()]
    wm = wm[0]
    mycurs.execute('SELECT PC from testwin;')
    wc = [int(record[0]) for record in mycurs.fetchall()]
    wc = wc[0]
    mycurs.execute('SELECT U FROM testwin;')
    draw = [int(record[0]) for record in mycurs.fetchall()]
    draw = draw[0]
    #print(str(wm) + str(wc) + str(draw))
    return wm, wc, draw


def getalldata():
    mycurs = db.cursor()
    mycurs.execute("SELECT * FROM testwin;")
    result = mycurs.fetchall()
    dict = {"Mensch": getdatafromrow()[1], "PC": getdatafromrow()[0], "Draw": getdatafromrow()[2]}
    return dict

def cleardb(dict1):
    sqlclear = "DELETE from %s;" % (dict1)
    mycurs.execute(sqlclear)
    sqlfirst = "INSERT INTO testwin VALUES (0,0,0);"
    mycurs.execute(sqlfirst)
    db.commit()

app = Flask(__name__)
api = Api(app)

class ApiClass(Resource):
    def get(self):
        data = getalldata()
        return data

api.add_resource(ApiClass, '/')
