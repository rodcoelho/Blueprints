#!/usr/bin/env python3

def login_or_register():
    user_input = input("""\n
Welcome to _______!
Would you like to Login or Register? (L or R)
    \n"""
    )
    return user_input

def login():
    user_name_input = input("""\n
What is your username?
\n"""
    )
    user_password_input = input("""\n
What is your password?
\n"""
                            )
    if len(user_password_input) < 3 or len(user_password_input) < 3:
        return False, False
    else:
        return user_name_input, user_password_input


def register():
    user_name_reg_input = input("""\n
    What would you like as a username?
    \n"""
                            )
    user_password_reg_input = input("""\n
    What password do you prefer?
    \n"""
                                )
    if len(user_name_reg_input) < 3 or len(user_password_reg_input) <3:
        return False, False
    else:
        return user_name_reg_input, user_password_reg_input

def display_menu():
    user_input = input(
"""\n Customer Info Platform
Select an option:
(1) Add/Edit Personal Info
(2) Add Phone Number
(3) Add Address
(4) Exit Services
(A) Admin Access \n"""
)
    return str(user_input)

def get_personal_info():
    user_name_input = input(
        """\n 
        What is your FIRST name? 
        \n"""
    )
    user_last_input = input(
        """\n 
        What is your LAST name? 
        \n"""
    )
    user_dob_input = input(
        """\n 
        When is your birthday? Format: YYYYMMDD
        \n"""
    )
    if len(user_name_input) < 3 or len(user_last_input) < 3 or len(user_dob_input) < 3:
        print("Your inputs are too short")
    else:
        return user_name_input, user_last_input, user_dob_input

def get_phone_num():
    user_phone_input = input(
        """\n 
        What is your phone number? 
        \n"""
    )
    if len(user_phone_input) > 6:
        return user_phone_input
    else:
        print("Your phone number is not long enough.")

def get_address_info():
    user_address_input = input(
"""\n 
What is your address?
\n"""
)
    if len(user_address_input) < 3:
        print("Your address is too short")
    else:
        return user_address_input

def get_adminwords():
    user_input = input(
        """\n Type SQLite command here:\n"""
    )
    return str(user_input)

def admin_perm():
    user_input = input(
        """\n Are you a user(0) or admin(1)?\n"""
    )
    return str(user_input)