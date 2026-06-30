# nums = [3, 2, 4]
# nums.sort()
# # nums becomes [2, 3, 4]

# target = 6

# i = 0
# j = len(nums) - 1

# while i < j:
#     if nums[i] + nums[j] == target:
#         print(i, j)
#         break
#     elif nums[i] + nums[j] < target:
#         i += 1
#     else:
#         j -= 1

# nums=[1,1,2]
# a=0
# n=len(nums)
# k=1
# b=1
# while(b<n):
#     if nums[b]==nums[b-1]:
#         b+=1
#         continue
#     else:
#         nums[a+1]=nums[b]
#         a+=1
#         k+=1
#         b+=1
# print(k)


# nums = [0,1,0,3,12]
# j=0
# for i in range(len(nums)):
#     if nums[i]!=0:
#         nums[j],nums[i]=nums[i],nums[j]
#         j+=1
# print(nums)

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
    

