import sqlite3

conn = sqlite3.connect('mysqlite.db')
c = conn.cursor()

#create table
c.execute('''CREATE TABLE IF NOT EXISTS students
             (rollno real, name text, class real)''')
			
#commit the changes to db			
conn.commit()
#close the connection
conn.close()
