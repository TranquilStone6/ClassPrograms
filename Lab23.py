#Write a menu driven program

import mysql.connector as s
from tabulate import *
mycon=s.connect(host="localhost",user="root",passwd="deens123",database="labprog23")
mycur=mycon.cursor()
def update():
    s=input("Enter column to be updated: ")
    if s=="ename":
        n1=input("Enter name to be updated: ")
        n2=input("Enter new name: ")
        mycur.execute("update emp set ename='[]' where ename='[]'".format(n2,n1))
        mycon.commit()
    elif s=="dept":
        n1=input("Enter dept to be updated: ")
        n2=input("Enter new dept: ")
        mycur.execute("update emp set dept='[]' where dept='[]'".format(n2,n1))
        mycon.commit()
    elif s=="title":
        n1=input("Enter title to be updated: ")
        n2=input("Enter new title: ")
        mycur.execute("update emp set title='[]' where title='[]'".format(n2,n1))
        mycon.commit()
    elif s=="gender":
        n1=input("Enter name of person whose gender is to be updated: ")
        n2=input("Enter new gender: ")
        mycur.execute("update emp set gender='[]' where ename='[]'".format(n2,n1))
        mycon.commit()
    
    def specificUpdate():

while True:
    print("1.Update Column(ename/dept/title/gender)\n2.Update Specific Record Salary\n3.Mass Salary Update\n4.Exit")
    n=int(input("Enter choice: "))
    if n==1:
        update()
    elif n==2:

    elif n==3:

    elif n==4:
        break
    else:
        print("Invalid")