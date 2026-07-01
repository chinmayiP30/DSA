
main=[-4,-1,0,3,10]
a=[]
b=[]
for i in range (len(main)):
    if main[i]>=0:
        b.append(main[i])
    else:
        a.append(main[i])
if len(a)!=0:
    for i in range(len(a)):
        a[i]=a[i]*a[i]
    a.reverse()
if len(b)!=0:
    for i in range (len(b)):
        b[i]=b[i]*b[i]
i=0
j=0
m=len(a)
n=len(b)
res=[0]*(m+n)
k=0
while i<m and j<n:
    if a[i]<=b[j]:
        res[k]=a[i]
        i+=1
        k+=1
    else:
        res[k]=b[j]
        j+=1
        k+=1
while i<m:
    res[k]=a[i]
    i+=1
    k+=1
while j<n:
    res[k]=b[j]
    j+=1
    k+=1
print(res)
