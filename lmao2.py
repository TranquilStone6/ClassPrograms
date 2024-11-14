l=[]
n=int(input("Enter number of integers: "))
print("Enter list:")
for i in range(0,n):
    l.append(int(input()))
e=9
while(e<n-1):
    temp=l[e]
    l[e]=l[e+1]
    l[e+1]=temp
    e=e+10

for i in range(0,n):
    print(l[i],end=" ")