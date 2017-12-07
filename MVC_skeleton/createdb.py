import sqlite3

connection = sqlite3.connect('customer.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE users(
pk INTEGER,
username VARCHAR(32),
password VARCHART(64),
admin INTEGER,
PRIMARY KEY(pk))
;""")

cursor.execute("""
CREATE TABLE informations(
pk INTEGER,
userID INTEGER,
first VARCHAR(32),
last VARCHAR(32),
dob INTEGER,
FOREIGN KEY(userID) REFERENCES users(pk),
PRIMARY KEY(pk))
;""")

cursor.execute("""
CREATE TABLE phones(
pk INTEGER,
userID INTEGER,
phone VARCHAR(32),
FOREIGN KEY(userID) REFERENCES users(pk),
PRIMARY KEY(pk))
;""")

cursor.execute("""
CREATE TABLE addresses(
pk INTEGER,
userID INTEGER,
address VARCHAR(64),
FOREIGN KEY(userID) REFERENCES users(pk),
PRIMARY KEY(pk))
;""")

connection.commit()
cursor.close()
connection.close()