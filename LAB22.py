'''
Write a menu driven program for inserting records into the MySQL table and handling
'''

import mysql.connector as m
from tabulate import tabulate
nightwing=m.connect(host="localhost",user="root",password="deens")
cursor=nightwing.cursor()

def creation():
    