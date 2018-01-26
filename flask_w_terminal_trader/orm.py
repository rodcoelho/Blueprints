#!/usr/bin/env python3

import sqlite3
import datetime


def check_username_password(submitted_username, submitted_password):
    connection = sqlite3.connect('master.db', check_same_thread=False)
    cursor = connection.cursor()
    try:
        cursor.execute("""
    SELECT username, password, balance
    FROM users
    WHERE username = '{}' AND password = '{}';
        """.format(submitted_username, submitted_password))
        fetch = cursor.fetchall()
        try:
            return fetch
        except:
            return "ERROR"
    except:
        return "ERROR"
