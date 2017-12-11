#!/usr/bin/env python3

import sqlite3

print("Entering seed.py...")

connection = sqlite3.connect('master.db', check_same_thread= False)
cursor = connection.cursor()

def add_users(username, password):
    cursor.execute(
        """INSERT INTO users(
            username,
            password
        ) VALUES(
            '{}',
            '{}'
        );""".format(username, password)
    )
    print("...adding " + str(username) + "...")

add_users('Rod',"swordfish")
add_users('Jason',"swordfish")
add_users('Nobu',"swordfish")
add_users('Jimmie',"swordfish")
add_users('Sue',"swordfish")
add_users('Rak',"swordfish")
add_users('Andrew',"swordfish")
add_users('Kenso',"swordfish")
add_users('Kai',"swordfish")
add_users('Priya',"swordfish")
add_users('Emily',"swordfish")
add_users('Devarsh',"swordfish")
add_users('Jenna',"swordfish")

connection.commit()
cursor.close()
connection.close()

print("Exiting seed.py...")
