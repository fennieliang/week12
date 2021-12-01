#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 16:16:56 2021

@author: fennieliang
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root_admin",
  database="test"
)

mycursor = mydb.cursor()

sql = "INSERT INTO class (studentID, firstName, lastName, dateOfBirth) VALUES (%s, %s, %s, %s)"
val = [
            ('4','Mark', 'L','2000/09/01'),
            ('5','Alex', 'T','2000/04/01'),
            ('6','Jane', 'U','2000/11/01'),
            ('7','Lili', 'A','2000/06/01'),
            ('8','Tom', 'B','2000/03/01'),
            ('9','Mike', 'M','2000/02/01')
            ]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")