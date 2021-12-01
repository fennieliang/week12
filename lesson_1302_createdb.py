# -*- coding: utf-8 -*-
"""
Created on Fri Jul 2 16:03:37 2021

@author: fennieliang
"""

from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as db:
        create_db = "CREATE DATABASE testdatabase"
        with db.cursor() as cursor:
            cursor.execute(create_db)
            db.commit()
            #db.commit() is to make sure the database is created
            print("database created successfully")
except Error as e:
    print(e)


#Disconnecting from the server
db.close()