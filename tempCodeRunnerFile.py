
nums = [1, 2, 2, 4, 3, 1, 4]
XOR=0
n=len(nums)
for i in range(n):
    XOR=XOR^nums[i]
print(XOR)