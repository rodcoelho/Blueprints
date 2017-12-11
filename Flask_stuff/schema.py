#!/usr/bin/env python3

import sqlite3

print("Entering schema.py...")

connection = sqlite3.connect('master.db', check_same_thread= False)
cursor = connection.cursor()

cursor.execute('DROP TABLE users;')
cursor.execute(
    """CREATE TABLE users(
        pk INTEGER,
        username VARCHAR(32),
        password VARCHAR(64),
        PRIMARY KEY(pk)
    );"""
)

connection.commit()
cursor.close()
connection.close()

print("Exiting schema.py...")
