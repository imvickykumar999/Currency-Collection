
import sqlite3 as sql3

con = sql3.connect('mysite/db_web.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS users")

sql ='''CREATE TABLE "users" (
	"UID"	    INTEGER PRIMARY KEY AUTOINCREMENT,
	"UNAME"	    TEXT,
	"NAME"	    TEXT,
	"FILE"	    TEXT,
	"CONTACT"	TEXT
)'''

cur.execute(sql)
con.commit()
con.close()

# ------------ Authentication -----------------

con = sql3.connect('mysite/db_sample.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS users")

sql ='''CREATE TABLE "users" (
  "UID"   INTEGER PRIMARY KEY AUTOINCREMENT,
  "UNAME" varchar(50) NOT NULL,
  "EMAIL" varchar(50) NOT NULL,
  "UPASS" varchar(50) NOT NULL
);
'''

cur.execute(sql)
con.commit()
con.close()
