import sqlite3

connection = sqlite3.connect('master.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE users(
pk INTEGER,
username VARCHAR(32),
password VARCHART(64),
PRIMARY KEY(pk))
;""")

connection.commit()
cursor.close()
connection.close()