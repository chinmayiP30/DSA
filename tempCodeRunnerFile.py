nums = [-1,0,3,5,9,12]
target = 3
low=0
n=len(nums)
high=n-1
mid=(low+high)//2
while(low<=high):
    if nums[mid]==target:
        print(mid)
        break
    elif nums[mid]>target:
        high=mid-1
    else:
        low=mid+1
else:
    print(-1)