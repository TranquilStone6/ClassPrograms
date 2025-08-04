import mysql.connector as s 
from tabulate import * 
mydb=s.connect(host='localhost',user='root',passwd='deens123',database='labprog12', autocommit=True) 
mycur=mydb.cursor() 
def inserting_records(): 
    while True: 
        eno=int(input("enter eno: "))
        ename=input("Enter employee name: ") 
        dept=input("enter department: ") 
        title=input("enter title: ") 
        doj=input("enter date of joining: ") 
        gender=input("enter gender: ") 
        sal=int(input("enter salary: ")) 
        mycur.execute("insert into emp values({},'{}','{}','{}','{}','{}',{});".format(eno,ename,dept,title,doj,gender,sal)) 
        a=input('do you wish to continue:[y/n]') 
        if a=='n': 
            break 
def display_records(): 
    mycur.execute("select * from emp;") 
    o=mycur.fetchall() 
    
    table=tabulate(o,headers=["eno",'ename','dept','title','gender','doj','salary'],tablefmt='pretty') 
    print(table) 

def department_wise(): 
    mycur.execute("select dept,count(eno) from emp group by dept;".format(a)) 
    o=mycur.fetchall() 
    table=tabulate(o,headers=['department',"Count"],tablefmt='pretty') 
    print(table) 
def gender_wise(): 
    mycur.execute("select gender,count(eno) from emp group by gender;".format(a))