n=0
t=()
while n!=4:
    print("1.Create Fibonacci Series\n2.Identify the value for the index\n3.Identify the index for the given value\n4.Exit")
    n=int(input("Enter choice:"))
    if n==1:
        t=()
        a=0
        b=1
        n1=int(input("Enter length"))
        for i in range(0,n1):
            t=t+(a,)
            a,b=b,a+b
        print(t)
    if n==2:
        i1=int(input("Enter index"))
        print("Value:",t[i1])
    if n==3:
        v=int(input("Input value: "))
        for i in range(0,len(t)):
            if t[i]==v:
                print("Index: ",i)