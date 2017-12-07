#!/usr/bin/env python3
import time
import model
import view

def menu_after_login(username, user_id):
    running = True
    while running:
        user_input = view.display_menu()
        acceptable_inputs = ['1', '2', '3', '4','A']
        if user_input.upper() in acceptable_inputs:
            # EXIT option
            if user_input.upper() == "4":
                print("\nThank you for using our services!\n")
                running = False

            # Add / Edit Personal Info
            elif user_input.upper() == "1":
                # view - get info
                first, last, dob = view.get_personal_info()
                # model - put into db
                model.store_personal_info(user_id,first, last, dob)

            # Add Phone Number
            elif user_input.upper() == "2":
                # view - get phone nums
                phonenumber = view.get_phone_num()
                # model - put into db
                model.store_phonenum(user_id,phonenumber)

            # Add Address
            elif user_input.upper() == "3":
                # view - get address input
                address = view.get_address_info()
                # model - put into db
                model.store_address(user_id, address)

            # Admin
            elif user_input.upper() == "A":
                # check db if user is admin
                admin_check = model.check_admin(user_id)
                if admin_check is True:
                    adminwords = view.get_adminwords()
                    model.admin(adminwords)
                else:
                    print("You don't have Admin authority! Flee!")

            else:
                print("Something is broken")
        else:
            print("Hmm.. That is not acceptable input")

def login_or_register():
    bad_input = True
    while bad_input:
        user_input = view.login_or_register()
        acceptable_inputs = ['L','R']
        if user_input.upper() in acceptable_inputs:
            if user_input.upper() == 'L':
                login_username, login_password = view.login()
                if login_username is False or login_password is False:
                    print("Your login attempt failed. The username/password is not up to par...")
                    break
                login_attempt_return_message, username_in_db, user_id = model.login(login_username, login_password)
                if login_attempt_return_message is not False:
                    print("Welcome '{}', you are logged in!".format(username_in_db))
                    menu_after_login(login_username, user_id)
                    break
                else:
                    print("Your login attempt failed. The username/password does not exist...")
                    break

            elif user_input.upper() == 'R':
                register_username, register_password = view.register()
                if register_username is False or register_password is False:
                    print("Your registration attempt failed. The username/password is not up to par...")
                    break
                perm = view.admin_perm()
                register_attempt = model.register(register_username,register_password,perm)
                if register_attempt:
                    print("\nRegistration successful!")
                    continue
                else:
                    print('Registration attempt broken')
            else:
                print('login/register question broken')
        else:
            print('Hmm.. Invalid option')


if __name__ == "__main__":
    login_or_register()