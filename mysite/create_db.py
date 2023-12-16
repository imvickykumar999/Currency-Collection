
import sqlite3 as sql

#connect to SQLite
con = sql.connect('mysite/db_web.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS users")

#Create users table  in db_web database
sql ='''CREATE TABLE "users" (
	"UID"	    INTEGER PRIMARY KEY AUTOINCREMENT,
	"UNAME"	    TEXT,
	"NAME"	    TEXT,
	"FILE"	    TEXT,
	"CONTACT"	TEXT
)'''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()
