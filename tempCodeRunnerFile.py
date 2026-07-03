#3sum closest
nums=[-1,2,1,-4]
target=1
nums.sort()
n=len(nums)
closest_s=nums[0]+nums[1]+nums[2]
min_diff=abs(closest_s-target)
for i in range(n-2):
    left=i+1
    right=n-1
    while left<right:
        curr_s=nums[i]+nums[left]+nums[right]
        diff=abs(target-curr_s)
        if diff<min_diff:
            min_diff=diff
            closest_s=curr_s
        if curr_s<target:
            left+=1
        elif curr_s>target:
            right-=1
        else:
            print(curr_s)
print(closest_s)
