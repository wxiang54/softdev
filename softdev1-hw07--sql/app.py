import csv
import sqlite3

fobjp=open("peeps.csv")
dp=csv.DictReader(fobjp)
fobjc=open("courses.csv")
dc=csv.DictReader(fobjc)

f="discobandit.db"
db=sqlite3.connect(f)
c=db.cursor()

q="CREATE TABLE students(name TEXT, age INTEGER, id INTEGER);"
c.execute(q)
for k in dp:
    #values: k['name'], k['age'], k['id']
    q = "INSERT INTO students VALUES(" + "\"" + k['name'] + "\"" + "," + k['age'] + "," + k['id'] + ");"
    c.execute(q)

q="CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER);"
c.execute(q)
for k in dc:
    #values: k['code'], k['mark'], k['id']
    q = "INSERT INTO courses VALUES(" + "\"" + k['code'] + "\"" + "," + k['mark'] + "," + k['id'] + ");"
    c.execute(q)
    
db.commit()
db.close()
