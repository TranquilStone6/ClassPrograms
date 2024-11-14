import statistics as st
n=0
l=[]
while n!=5:
    print("1.Add item\n2.Maximum\n3.Minimum\n4.Highest Frequency\n5.Exit")
    print("Enter choice",end=": ")
    n=int(input())
    if n==1:
        l.append(input())
    if n==2:
        print(max(l))
    if n==3:
        print(min(l))
    if n==4:
        print(st.mode(l))