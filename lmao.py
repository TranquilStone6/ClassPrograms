n=0
l=[]
while n!=5:
    print("1.Add item\n2.View item\n3.Delete Item\n4.Modify item\n5.Exit")
    print("Enter choice",end=": ")
    n=int(input())
    if n==1:
        l.append(input())
    if n==2:
        i=int(input("Enter element number"))
        print(l[i-1])
    if n==3:
        i=int(input("Enter element number to be deleted"))
    if n==4:
        i=int(input("Enter element number to be modified"))
        l[i]=input("Enter element")