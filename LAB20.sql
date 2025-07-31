create database if not exists MeWhenTest;
use Lab20;
create table Emp(empid int,Firstname varchar(20),address varchar(20),city varchar(20));
insert into Emp values(10,"Ravi","Raj Nagar","GZB");
insert into Emp values(105,"Harry","Gandhi Nagar","GZB");
insert into Emp values(152,"Sam","33 Elm St.","Paris");
insert into Emp values(215,"Sarah","440 U.S. 110","Upton");
insert into Emp values(244,"Manilla","24 Friends Street","New Delhi");
insert into Emp values(300,"Robert","9 Cross Street","Washington");
insert into Emp values(335,"Ritu","Shastri Nagar","GZB");
insert into Emp values(400,"Rachel","121 Harrison St.","New York");
insert into Emp values(441,"Peter","11 Red Road","Paris");

create table EmpD(empId int,salary int,benefits int,designation varchar(20));
insert into EmpD values(10,75000,15000,"Manager");
insert into EmpD values(105,65000,15000,"Manager");
insert into EmpD values(152,80000,25000,"Director");
insert into EmpD values(215,75000,12500,"Manager");
insert into EmpD values(244,50000,12000,"Clerk");
insert into EmpD values(300,45000,10000,"Clerk");
insert into EmpD values(335,40000,10000,"Clerk");
insert into EmpD values(400,32000,7500,"Salseman");
insert into EmpD values(441,28000,7500,"Salesman");
update EmpD set designation="Salesman" where empid=400;

select e.empid,firstname,address,city,salary,benefits,designation from Emp e,Empd ed where e.empid=ed.empid and ed.salary>40000;
select firstname,salary from emp e,empD ed where e.empid=ed.empid and designation="Salesman";
select designation,max(salary) from empd group by designation having designation in ("Manager","Clerk")