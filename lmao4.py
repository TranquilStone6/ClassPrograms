n=0
l=[[0,0],[0,0]]
l2=[[0,0],[0,0]]
while n!=5:
    print("1.Input Matrix\n2.Add Matrix\n3.Sum of row elements\n4.Transpose\n5.Exit")
    print("Enter choice",end=": ")
    n=int(input())
    if n==1:
        for i in range(0,2):
            for j in range(0,2):
                l[i][j]=int(input( ))
    if n==2:
        print("Enter matrix to add")
        for i in range(0,2):
            for j in range(0,2):
                l[i][j]+=int(input())
    if n==3:
        i=int(input("Enter row index"))
        print(l[i][0]+l[i][1])
    if n==4:
        for i in range(0,2):
            for j in range(0,2):
                l2[i][j]=l[j][i]
        print(l2)