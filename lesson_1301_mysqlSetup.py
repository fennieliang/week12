# -*- coding: utf-8 -*-
"""
Created on Fri Jul 2 16:03:37 2021

@author: fennieliang
"""
'''
***** for staring database connection ***
1. go to https://dev.mysql.com/downloads/
   for windows: click on MySQL Installer 
               and follow the installation guide

   for MacOS: click on MySQL Community Server
   download the most recent version >> 
   macOS 11 (x86, 64-bit), DMG Archive
   follow the installation guide 
   and give a password for root access 
   before completing the installtation
   note your user name and password in case you forgot
       

***** check if the mysql server is installed successfully *****
1. open terminal type /usr/local/mysql/bin/mysql -u root -p

2. enter your password and click enter

3. if mysql> appears then you are fine


***** install MySQL Workbench *****
1. go back to the same download page 
    https://dev.mysql.com/downloads/
    
2. click on MySQL Workbench 
   select operating then click download

***** starting the workbench *****
1. if not working the reason can be because 
    the user you specified needs to be changed 
    as % as the hostname, otherwise the user will only 
    be able to connect from the localhost not remotely.
2. for solving it, 
    open terminal then start mysql by typing 
    /usr/local/mysql/bin/mysql -u root -p
    then type UPDATE mysql.user SET host='%' WHERE user='root';"

***** using mysql in python program *****    
1. open anaconda and select your Virture Environment
   open terminal then pip install mysql-connector-python 
   
'''

from getpass import getpass
#getpass will make user's input invisible 
#but not in the spyder console
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        #never hard code your user name and password 
        #in python
        
    ) as db:
        print(db)
except Error as e:
    print(e)
    
 
#Disconnecting from the server
db.close()