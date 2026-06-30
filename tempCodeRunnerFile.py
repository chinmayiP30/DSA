#removing duplicants from sorted array
a=[1,1,2]
i=0
j=1
k=1
n=len(a)
while(j<n):
    if a[j-1]==a[j]:
        j+=1
        continue
    else:
        a[i+1]=a[j]
        j+=1
        i+=1
        k+=1
        print(k)
    