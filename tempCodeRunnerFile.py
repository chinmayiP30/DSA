
a=[1,2,4,4]
n=len(a)
low=0
high=0
target=5
res=float('inf')
sum=0
while(high<n):
    sum=sum+a[high]
    while(sum>=target):
        l=high-low+1
        res=min(res,l)
        sum=sum-a[low]
        low+=1
    high+=1
print(res)    

