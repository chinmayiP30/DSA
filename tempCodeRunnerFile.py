#left rotate by d elements
a=[1,2,3,4,5,6,7]
d=3
n=len(a)
temp=[]
for i in range(d):
    temp.append(a[i])
for i in range(d,n):
    a[i-d]=a[i]
j=0
for i in range(n-d,n):
    a[i]=temp[j]
    j+=1
print(a)