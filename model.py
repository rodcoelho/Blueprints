#!/usr/bin/env python3

import orm
import wrapper

def register(username, password, perm):
    insert_into_DB_attempt = orm.register(username,password,perm)
    if insert_into_DB_attempt:
        return True
    else:
        return False

def login(username, password):
    query_attemp_success, usernameindb, user_id = orm.login(username,password)
    if query_attemp_success is True:
        return True, usernameindb, user_id
    else:
        return False, False, False

def store_personal_info(user_id,first, last, dob):
    orm.store_data_informations_table(user_id,first, last, dob)

def store_phonenum(user_id,phonenumber):
    orm.store_phonenum_table(user_id,phonenumber)

def store_address(user_id, address):
    orm.store_address_table(user_id,address)

def admin(adminwords):
    orm.admin(adminwords)

def check_admin(user_id):
    admin_check = orm.check_admin(user_id)
    return admin_check