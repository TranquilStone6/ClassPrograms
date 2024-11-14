n=int(input("Enter list length"))
print("Enter list")
l=[]
for i in range(0,n):
    l.append(input())

for i in range(0,n):
    print(i)
    temp=l[i]
    l[i]=l[i+1]
    l[i+1]=temp
    i=i+1

print(l)