import random as r
t=()
n=int(input("Enter length: "))
for i in range(0,n):
    t=t+(r.randint(45,60),)
print(t)
z=0
while(z!=3):
    print("1.Unpack and Pack\n2.List constructor\n3.Exit")
    z=int(input("Enter choice: "))
    if z==1:
        l=list(t)
        for i in range(0,n):
            if l[i]%2 == 1:
                l[i]+=1
        t1=tuple(l)
        print(t1)
    if z==2:
        l1=list(t)
        unique_elements=[]
        for item in l1:
            if item not in unique_elements:
                unique_elements.append(item)
        t2=tuple(unique_elements)
        print(t2)




