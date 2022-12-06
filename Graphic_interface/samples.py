import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata(
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)


""")

username1,password1 = "user1", hashlib.sha256("password".encode()).hexdigest()
username2,password2 = "user2", hashlib.sha256("yo".encode()).hexdigest()
username3,password3 = "user3", hashlib.sha256("da".encode()).hexdigest()
username4,password4 = "user4", hashlib.sha256("es".encode()).hexdigest()
cur.execute("INSERT INTO userdata (username,password) VALUES (?,?)", (username1,password1))
cur.execute("INSERT INTO userdata (username,password) VALUES (?,?)", (username2,password2))
cur.execute("INSERT INTO userdata (username,password) VALUES (?,?)", (username3,password3))
cur.execute("INSERT INTO userdata (username,password) VALUES (?,?)", (username4,password4))


conn.commit()
