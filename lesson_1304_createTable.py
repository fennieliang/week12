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
        create_table = "CREATE TABLE class(studentID int PRIMARY KEY,firstName VARCHAR(50),lastName VARCHAR(50),dateOfBirth DATE)"
        show_table = "DESCRIBE class"
        with db.cursor() as cursor:
            cursor.execute(create_table)
            db.commit()
            cursor.execute(show_table)
            result = cursor.fetchall()#fetch all table elements
            for row in result:
                 print(row)
            
except Error as e:
    print(e)

 
#Disconnecting from the server
db.close()