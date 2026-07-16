arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]
long=1
n=len(arr)
for i in range(n):
    x=arr[i]
    count=1
    while(x+1) in arr:
        x=x+1
        count+=1
        long=max(long,count)
print(long)
