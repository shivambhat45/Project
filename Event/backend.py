import sqlite3

def studentdata():
	con=sqlite3.connect("student.db")
	cur=con.cursor()
	cur.execute('''CREATE TABLE IF NOT EXISTS student(Admissionnumber text,Firstname text,Lastname text,Class text,Rollno text)''')
	con.commit()
	con.close()

def submit(Admissionnumber,Firstname,Lastname,Class,Rollno):
	con=sqlite3.connect("student.db")
	cur=con.cursor()
	cur.execute("INSERT INTO student(Admissionnumber,Firstname,Lastname,Class,Rollno) VALUES(?,?,?,?,?)",(Admissionnumber,Firstname,Lastname,Class,Rollno))
	con.commit()
	con.close()

def viewdata():
	con=sqlite3.connect("student.db")
	cur=con.cursor()
	cur.execute("SELECT * FROM student")
	row=cur.fetchall()
	con.commit()
	con.close()
	return row

studentdata()