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
        database="test"
    ) as db:
        drop_table = "DROP TABLE Class"

        with db.cursor() as cursor:
            cursor.execute(drop_table)
            
except Error as e:
    print(e)

 
#Disconnecting from the server
db.close()