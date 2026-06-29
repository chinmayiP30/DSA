
nums=[1,1,2]
a=0
n=len(nums)
k=1
b=1
while(b<n):
    if nums[b]==nums[b-1]:
        b+=1
        continue
    else:
        nums[a+1]=nums[b]
        a+=1
        k+=1
        b+=1
print(k)

