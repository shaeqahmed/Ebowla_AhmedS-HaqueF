import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"
pObj = open("peeps.csv")
peeps = csv.DictReader(pObj)
cObj = open("courses.csv")
courses = csv.DictReader(cObj)

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...


q = "CREATE TABLE students (name TEXT, id INTEGER)"

c.execute(q)    #run SQL query
for v in peeps:
        q="INSERT INTO students VALUES ('" + v['name'] + "'," + v['id'] + ")"
	c.execute(q)

q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"

c.execute(q)
for v in courses:
        q="INSERT INTO courses VALUES ('" + v['code'] + "'," + v['id'] + "," + v['mark'] + ")"
	c.execute(q)


#==========================================================
db.commit() #save changes
db.close()  #close database
