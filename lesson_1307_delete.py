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

sql = "DELETE FROM class WHERE firstName = 'Mark'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record deleted.")