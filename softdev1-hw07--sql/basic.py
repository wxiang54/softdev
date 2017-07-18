import csv
import sqlite3

fobjp=open("peeps.csv")
dp=csv.DictReader(fobjp)
fobjc=open("courses.csv")
dc=csv.DictReader(fobjc)

f="discobandit.db"
db=sqlite3.connect(f)
c=db.cursor()

q = "SELECT name, students.id, mark FROM students, courses WHERE students.id=courses.id"
c.execute(q)
listMark = c.fetchall()

dictAverages = []
for k in dp:
    dict = {}
    dict["name"] = k["name"]
    dict["id"] = k["id"]
    dict["average"] = 0
    dictAverages.append( dict )

id1 = listMark[0][1]
total = 0
numValues = 0
inc = 0
for k in listMark:
    id2 = k[1]
    if id1 == id2:
        total += k[2]
        numValues += 1
    else:
        avg = total / numValues
        dictAverages[inc]["average"] = avg
        id1 = id2
        total = k[2]
        numValues = 1
        inc += 1

avg = total / numValues
dictAverages[inc]["average"] = avg

for k in dictAverages:
    print k

db.commit()
db.close()
