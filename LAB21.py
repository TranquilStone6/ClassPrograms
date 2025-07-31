'''
Write a menu driven program
'''

import mysql.connector as m
from tabulate import tabulate
stu=[["Roll no","Student name","Marks"],[1,"ste",14],[2,"rte",56]]
table1=tabulate(stu)
table2=tabulate(stu, headers="firstrow",tablefmt="grid")
print(table1)
print("\n",table2)
mycon=m.connect(host='localhost',user='root',passwd='deens')
my=mycon.cursor()
def creation():
    global name
    global table_name
    name=input("Input Database name: ")
    my.execute("create table if not exists {}".format(name))
    my.execute("use{}".format(name))

    table_name=input("Enter table name: ")
    my.execute("create table if not exists {} (eno int, ename char(25), dept char(25), title char(25), salary int)".format(name))

    print()

def show():
    print("The database created:",name)
    my.execute("use()".format(name))
    my.execute("show tables")
    x=my.fetchall()
    table=tabulate(x,headers={"Tables_in_Lab21"}, tablefmt='grid')
    print(table)
    print()
    my.execute("desc()".format(table_name))
    x=my.fetchall()
    print("Structure of the table:")
    table=tabulate(x,headers=["Field","Type","Null","Key","Def"])
    print(table)
    print()

def add():
    global col
    col=input("Enter column name: ")
    col_type=input("Enter column type")
    my.execute("alter table() add column() ()".format(table_name,col,col_type))
    my.execute("desc()".format(table_name))
    x=my.fetchall()
    print("Structure of the table:")
    table=tabulate(x,headers=["Field","Type","Null","Key","Default","Extra"],tablefmt="pretty")
    print(table)
    print()

def modify():
    modify_col=input("Enter column name: ")
    modify_col_type=input("Enter column type")
    my.execute("alter table() add column() ()".format(table_name,modify_col,modify_col_type))
    my.execute("desc()".format(table_name))
    x=my.fetchall()
    print("Structure of the table:")
    table=tabulate(x,headers=["Field","Type","Null","Key","Default","Extra"],tablefmt="pretty")
    print(table)
    print()

def drop():
    drop_col=input("Enter column name: ")
    my.execute("alter table() add column() ()".format(table_name,drop_col))
    my.execute("desc()".format(table_name))
    x=my.fetchall()
    print("Structure of the table:")
    table=tabulate(x,headers=["Field","Type","Null","Key","Default","Extra"],tablefmt="pretty")
    print(table)
    print()

def input1():
    while True:
        print("1. Create Database\n2. Show created Database and Tables\n3. Add column\n4. Modify Column\n5. Drop Column\n6. Exit")
        choice=int(input("Enter choice: "))
        if choice == 1:
            creation()
        elif choice == 2:
            show()
        elif choice == 3:
            add()
        elif choice == 4:
            modify()
        elif choice == 5:
            drop()
        else:
            break
input1()