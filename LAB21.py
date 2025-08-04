import mysql.connector as s 
from tabulate import * 
d='' 
t='' 
mydb=s.connect(host='localhost',user='root',passwd='deens') 
mycur=mydb.cursor() 
def create(): 
    global d 
    global t 
    d=input("enter name of databse: ") 
    mycur.execute("create database if not exists {};".format(d)) 
    mycur.execute('use {};'.format(d)) 
    t=input("enter name of table: ") 
    mycur.execute(" create table if not exists {}(eno int,ename char(25),dept char(25),title char(25));".format(t))   
def show(): 
    mycur.execute('use {};'.format(d)) 
    mycur.execute('show tables;') 
    o=mycur.fetchall() 
    table=tabulate(o,headers=["tables in labprog12"],tablefmt='pretty') 
    print(table) 
    print("The tables are:\n ") 
    mycur.execute('desc {};'.format(t)) 
    o=mycur.fetchall() 
    table=tabulate(o,headers=["Field",'type','null','key','default','extra'],tablefmt='pretty') 
    print(table) 
    
def add(): 
    a=input("enter column name: ") 
    b=input("enter datatype (and length if required) :") 
    mycur.execute("alter table {} add {} {};".format(t,a,b)) 
def modify(): 
    a=input("enter column name: ") 
    b=input("enter datatype (and length if required) :") 
    mycur.execute('alter table {} modify {} {};'.format(t,a,b)) 
def drop():
    a=input("enter column name: ") 
    mycur.execute('alter table {} drop {};'.format(t,a)) 
while True: 
    print('\nMenu: \n1.create databse\n2.show created database and tables\n3.add attributes to table\n4.modify attribute\n5.drop attribute\n6.exit') 
    a=int(input("\nenter choice: ")) 
    if a==1: 
        create() 
    elif a==2: 
        show() 
    elif a==3: 
        add() 
    elif a==4: 
        modify() 
    elif a==5: 
        drop() 
    else: 
        break