#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('master.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute("""
INSERT INTO users(username, password, balance)
VALUES ('{}','{}',1000000);
    """.format('rodrigo', 'swordfish'))

cursor.execute("""
INSERT INTO users(username, password, balance)
VALUES ('{}','{}',1000000);
    """.format('kenso', 'swordfish'))

cursor.execute("""
INSERT INTO users(username, password, balance)
VALUES ('{}','{}',1000000);
    """.format('root', 'swordfish'))

connection.commit()
cursor.close()
connection.close()
