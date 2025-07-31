#Write a menu driven program for deleting records from the mysql table using python-mysql interface with the following menu: 
#1. Deletd Specific Record
#2. Delete records between given dates
#3. Exit

import mysql.connector as s
from tabulate import *
mycon=s.connect(host="localhost",user="root",passwd="deens123",database="labprog23")
mycur=mycon.cursor()