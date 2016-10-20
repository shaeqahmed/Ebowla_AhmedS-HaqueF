import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops


q = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id"
stats = c.execute(q)

# 0 = student name
# 1 = student id
# 2 = student grade

avgs = {}

for s in stats:
	name = s[0]
	id = s[1]
	grade = s[2]
	if name in avgs:
		sum = avgs[name][1]*ctr
		sum += grade
		ctr += 1.0
		avgs[name][1] = sum/ctr
	else:
		avgs[name] = [id,grade]
		ctr = 1.0

for stud in avgs:
	print "student: %s, id: %d, average: %f"%(stud,avgs[stud][0],avgs[stud][1])

db.commit() #save changes
db.close()  #close database
