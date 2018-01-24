#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('master.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE positions(
pk INTEGER,
userID INTEGER,
symbol VARCHAR(32),
quantity INTEGER,
VWAP INTEGER,
FOREIGN KEY(userID) REFERENCES users(pk),
PRIMARY KEY(pk))
;""")

cursor.execute("""
CREATE TABLE transactions(
pk INTEGER,
userID INTEGER,
symbol VARCHAR(32),
unixtime TEXT,
lastprice INTEGER,
quantity INTEGER,
buysell VARCHAR(32),
FOREIGN KEY(userID) REFERENCES users(pk),
PRIMARY KEY(pk))
;""")

cursor.close()
connection.close()