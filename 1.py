# #2sum
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


##removing duplicants 
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


# # moving zeros
# nums = [0,1,0,3,12]
# pointer=0
# for i in range(len(nums)):
#     if nums[i]!=0:
#         nums[pointer],nums[i]=nums[i],nums[pointer]
#         pointer+=1
# print(nums)



# #removing duplicants from sorted array
# a=[1,1,2]
# i=0
# j=1
# k=1
# n=len(a)
# while(j<n):
#     if a[j-1]==a[j]:
#         j+=1
#         continue
#     else:
#         a[i+1]=a[j]
#         j+=1
#         i+=1
#         k+=1
#         print(k)
    

# #merging of two sorted arrays
# a = [1,2,8]
# m= 3
# b = [2,5,6]
# n = 3
# i=0
# j=0
# res=[0]*(m+n)
# k=0
# while i<m and j<n:
#     if a[i]<=b[j]:
#         res[k]=a[i]
#         i+=1
#         k+=1
#     else:
#         res[k]=b[j]
#         j+=1
#         k+=1
# while i<m:
#     res[k]=a[i]
#     i+=1
#     k+=1
# while j<n:
#     res[k]=b[j]
#     j+=1
#     k+=1
# print(res)

# #squaring of sorted array
# a=[-4,-2,1,4,6]
# n=len(a)
# res=[]
# for i in a:
#     res.append(i**2)
#     i+=1
# res.sort()
# print(res)


# #squaring of sorted array without sort function
# main=[-4,-1,0,3,10]
# a=[]
# b=[]
# for i in range (len(main)):
#     if main[i]>=0:
#         b.append(main[i])
#     else:
#         a.append(main[i])
# if len(a)!=0:
#     for i in range(len(a)):
#         a[i]=a[i]*a[i]
#     a.reverse()
# if len(b)!=0:
#     for i in range (len(b)):
#         b[i]=b[i]*b[i]
# i=0
# j=0
# m=len(a)
# n=len(b)
# res=[0]*(m+n)
# k=0
# while i<m and j<n:
#     if a[i]<=b[j]:
#         res[k]=a[i]
#         i+=1
#         k+=1
#     else:
#         res[k]=b[j]
#         j+=1
#         k+=1
# while i<m:
#     res[k]=a[i]
#     i+=1
#     k+=1
# while j<n:
#     res[k]=b[j]
#     j+=1
#     k+=1
# print(res)



# #3 sum equal to zero
# nums=[-1,0,1,2,-1,-4]
# nums.sort()
# n=len(nums)
# res=[]
# for i in range(n-2):
#     if i>0 and nums[i]==nums[i-1]:
#         continue
#     left=i+1
#     right=n-1
#     target=-nums[i]
#     while left<right:
#         s=nums[left]+nums[right]
#         if s==target:
#             res.append([nums[i],nums[left],nums[right]])
#             left+=1
#             right-=1
#             while left<right and nums[left]==nums[left-1]:
#                 left+=1
#             while left<right and nums[right]==nums[right+1]:
#                 right-=1
#         elif s<target:
#             left+=1
#         else:
#              right-=1
# print(res)

# #3sum closest
# nums=[-1,2,1,-4]
# target=1
# nums.sort()
# n=len(nums)
# closest_s=nums[0]+nums[1]+nums[2]
# min_diff=abs(closest_s-target)
# for i in range(n-2):
#     left=i+1
#     right=n-1
#     while left<right:
#         curr_s=nums[i]+nums[left]+nums[right]
#         diff=abs(target-curr_s)
#         if diff<min_diff:
#             min_diff=diff
#             closest_s=curr_s
#         if curr_s<target:
#             left+=1
#         elif curr_s>target:
#             right-=1
#         else:
#             print(curr_s)
# print(closest_s)


# #sorting colors the better sol
# nums = [2,0,2,1,1,0]
# c0=0
# c1=0
# c2=0
# for i in nums:
#     if i==0:
#         c0+=1
#     elif i==1:
#         c1+=1
#     else:
#         c2+=1
# for i in range(c0):
#     nums[i]=0
# for i in range(c0,c0+c1):
#     nums[i]=1
# for i in range(c0+c1,len(nums)):
#     nums[i]=2
# print(nums)

# #optimal sol for sort colors using dutch national flag alg
# nums = [2,0,2,1,1,0]
# n=len(nums)
# low=0
# mid=0
# high=n-1
# while mid<=high:
#     if nums[mid]==0:
#         nums[mid],nums[low]=nums[low],nums[mid]
#         mid+=1
#         low+=1
#     elif nums[mid]==1:
#         mid+=1
#     else:
#         nums[mid],nums[high]=nums[high],nums[mid]
#         high-=1
# print(nums)

# #removing duplicants
# nums=[1,1,2,2,3,3]
# i=0
# for j in range(1,len(nums)):
#     if nums[j]!=nums[i]:
#         nums[i+1]=nums[j]
#         i+=1
# print(nums[:i+1])

# #patterns
# for i in range(4):
#     for j in range(4):
#         print("*",end="")
#     print()

 
# for i in range(5):
#     for j in range(i):
#         print("*",end="")
#     print()


# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

# for i in range(1,6):
#     for j in range(6-i):
#         print("*",end="")
#     print()