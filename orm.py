import sqlite3

connection = sqlite3.connect('customer.db')
cursor = connection.cursor()

def register(username,password,perm):
    connection = sqlite3.connect('customer.db')
    cursor = connection.cursor()
    try:
        cursor.execute("""
INSERT INTO users(username, password, admin)
VALUES (?,?,?);
    """, (username,password,perm))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except:
        connection.commit()
        cursor.close()
        connection.close()
        return False

def login(username,password):
    connection = sqlite3.connect('customer.db')
    cursor = connection.cursor()
    try:
        cursor.execute("""
    SELECT username, password
    FROM users
    WHERE username = ? AND password = ?;
        """,(username, password))
        fetch = cursor.fetchall()

        cursor.execute("""
            SELECT pk
            FROM users
            WHERE username = ? AND password = ?;
                """,(username, password))
        fetch_id = cursor.fetchone()[0]

        if len(fetch) < 1:
            return False, False, False
        else:
            return True, username, fetch_id
    except:
        connection.commit()
        cursor.close()
        connection.close()
        return False, False, False

def store_data_informations_table(user_id,first, last, dob):
    connection = sqlite3.connect('customer.db')
    cursor = connection.cursor()

    try:
        # check if information table already holds info. If so UPDATE. Else ADD.
        cursor.execute("""
                    SELECT userID, first, last
                    FROM informations
                    WHERE userID = ?;
                                """,(user_id))
        query = cursor.fetchall()

        # if query doesn't exist in table then ADD to table
        if len(query) == 0:
            # if query of element doesn't exist, ADD to table
            cursor.execute("""
                INSERT INTO informations(userID, first, last, dob)
                VALUES (?,?,?,?);
                    """,(user_id, first, last, dob))
            connection.commit()
            cursor.close()
            connection.close()
        else:
            # ELSE if informations for userID  exists in table - adjust to reflect changes from controller

            # update FIRST
            cursor.execute("""
                UPDATE informations
                SET first = ?
                WHERE userID = ?
                ;""",(first, user_id))
            # save changes
            connection.commit()

            # update LAST
            cursor.execute("""
                UPDATE informations
                SET last = ?
                WHERE userID = ?
                ;""",(last, user_id))
            # save changes
            connection.commit()

            # update dob
            cursor.execute("""
                UPDATE informations
                SET dob = ?
                WHERE userID = ?
                ;""",(dob, user_id))
            # save changes
            connection.commit()

            print("Your name has been updated to {} {}".format(first, last))
            print("Your DOB is now {}".format(dob))

            connection.commit()
            cursor.close()
            connection.close()
    except:
        print("Error occured")

        connection.commit()
        cursor.close()
        connection.close()

def store_phonenum_table(user_id,phonenumber):
    connection = sqlite3.connect('customer.db')
    cursor = connection.cursor()

    try:
        cursor.execute("""
                INSERT INTO phones(userID, phone)
                VALUES (?,?);
                    """,(user_id, phonenumber))

        print("Your phone number {} has been added to your profile".format(phonenumber))
        connection.commit()
        cursor.close()
        connection.close()

    except:
        print("Phone number was not added. Error occurred.")
        connection.commit()
        cursor.close()
        connection.close()

def store_address_table(user_id,address):
    connection = sqlite3.connect('customer.db')
    cursor = connection.cursor()

    try:
        cursor.execute("""
                    INSERT INTO addresses(userID, address)
                    VALUES (?,?);
                        """,(user_id, address))

        print("Your address {} has been added to your profile".format(address))
        connection.commit()
        cursor.close()
        connection.close()

    except:
        print("Address was not added. Error occurred.")
        connection.commit()
        cursor.close()
        connection.close()

def admin(adminwords):
    connection = sqlite3.connect('customer.db')
    cursor = connection.cursor()
    try:
        cursor.execute("""
                    ?
                        """,(adminwords))

        print("Your Admin command has been executed")
        connection.commit()
        cursor.close()
        connection.close()

    except:
        print("There was an error in your SQL statement")
        connection.commit()
        cursor.close()
        connection.close()

def check_admin(user_id):
    connection = sqlite3.connect('customer.db')
    cursor = connection.cursor()
    try:
        cursor.execute("""
        SELECT admin
        FROM users
        WHERE pk = ?;
            """,(user_id))
        fetch = cursor.fetchall()[0]

        if fetch[0] == 0:
            connection.commit()
            cursor.close()
            connection.close()
            return False
        else:
            connection.commit()
            cursor.close()
            connection.close()
            return True
    except:
        connection.commit()
        cursor.close()
        connection.close()
        return False