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


# for i in range(5):
#     for j in range(5-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     print()


# # largest of array
# a=[3,2,1,5,2]
# n=len(a)
# a.sort()
# print(a[n-1])

# a=[3,2,1,5,2]
# n=len(a)
# l=a[0]
# for i in range(n):
#     if a[i]>l:
#         l=a[i]
# print(l)

# #second largest element 
# a=[1,2,4,7,7,5]
# a.sort()
# n=len(a)
# l=a[n-1]
# s=0
# for i in range(n-2,-1,-1):
#     if a[i]!=l:
#         s=a[i]
#         break
# print(s)

# # better approach
# a=[1,2,4,7,7,5]
# n=len(a)
# l=a[0]
# for i in range(n):
#     if a[i]>l:
#         l=a[i]
# s=-1
# for i in range(n):
#     if a[i]>s and a[i]!=l:
#         s=a[i]
# print(s)

# a=[1,2,4,7,7,5]
# n=len(a)
# l=a[0]
# s=-1
# for i in range(n):
#     if a[i]>l :
#         s=l
#         l=a[i]
#     elif a[i]<l and a[i]>s:
#         s=a[i]
# print(l)
# print(s)

# a= [3,4,5,1,2]
# n=len(a)
# is_s=True
# for i in range(1,n):
#     if a[i]<a[i-1]:
#         is_s=False
#         break
# print(is_s) 

# #left rotate array by one
# a=[1,2,3,4,5]
# n=len(a)
# temp=a[0]
# for i in range(1,n):
#     a[i-1]=a[i]
# a[n-1]=temp
# print(a)

# #left rotate by d elements
# a=[1,2,3,4,5,6,7]
# d=3
# n=len(a)
# temp=[]
# for i in range(d):
#     temp.append(a[i])
# for i in range(d,n):
#     a[i-d]=a[i]
# j=0
# for i in range(n-d,n):
#     a[i]=temp[j]
#     j+=1
# print(a)

# #1st occurance of target's index
# nums = [2, 3, 4, 5, 3]
# n=len(nums)
# t=3
# for i in range(n):
#     if nums[i]==t:
#         print(i)
#         break


# #union of sorted arrays 
# nums1 = [1, 2, 3, 4, 5]
# nums2 = [1, 2, 7]
# i=0
# j=0
# res=[]
# m=len(nums1)
# n=len(nums2)
# while i<m and j<n:
#     if nums1[i]<=nums2[j]:
#         if len(res)==0 or res[-1]!=nums1[i]:
#             res.append(nums1[i])
#         i+=1

#     else:
#         if len(res)==0 or res[-1]!=nums2[j]:
#             res.append(nums2[j])
#         j+=1
# while i<m:
#     if len(res)==0 or res[-1]!=nums1[i]:
#         res.append(nums1[i])
#     i+=1
# while j<n:
#     if len(res)==0 or res[-1]!=nums2[j]:
#         res.append(nums2[j])
#     j+=1
# print(res)

# nums = [0, 2, 3, 1, 4]
# n=len(nums)
# s=sum(nums)
# e_s=n*(n+1)//2
# a_s=e_s-s
# print(a_s)

# #intersection of sorted array(brute)
# a=[1,2,2,3,3,4,5,6]
# b=[2,3,3,5,6,6,7]
# n1=len(a)
# n2=len(b)
# vis=[0]*n2
# res=[]
# for i in range(n1):
#     for j in range(n2):
#         if a[i]==b[j] and vis[j]==0:
#             res.append(a[i])
#             vis[j]=1
#             break
#         if b[j]>a[i]:
#             break
# print(res)

# #optimal sol 
# a=[1,2,2,3,3,4,5,6]
# b=[2,3,3,5,6,6,7]
# n1=len(a)
# n2=len(b)
# i=0
# j=0
# res=[]
# while i<n1 and j<n2:
#     if a[i]<b[j]:
#         i+=1
#     elif b[j]<a[i]:
#         j+=1
#     else:
#         if len(res)==0 or res[-1]!=a[i]:
#             res.append(a[i])
#         i+=1
#         j+=1
    
# print(res)


# #count of max consecutive 1s
# nums = [1, 1, 0, 0, 1, 1, 1, 0]
# n=len(nums)
# count=0
# maxi=0
# for i in range (n):
#     if nums[i]==1:
#         count+=1
#         maxi=max(count,maxi)
#     else:
#         count=0
# print(maxi)


##ingle number 
# nums = [1, 2, 2, 4, 3, 1, 4]

# n = len(nums)

# for i in range(n):
#     num = nums[i]
#     count = 0

#     for j in range(n):
#         if nums[j] == num:
#             count += 1

#     if count == 1:
#         print(num)
#         break

# nums = [1, 2, 2, 4, 3, 1, 4]
# n=len(nums)
# for i in range(n):
#     num=nums[i]
#     count=0
#     for j in range(n):
#         if nums[j]==num:
#             count+=1
#     if count==1:
#         print(num)

# #optimal sol
# nums = [1, 2, 2, 4, 3, 1, 4]
# XOR=0
# n=len(nums)
# for i in range(n):
#     XOR=XOR^nums[i]
# print(XOR)

# #longest subarray which is equal to target
# #brute force
# nums = [10, 5, 2, 7, 1, 9]
# t=15
# l=0
# n=len(nums)
# for i in range(n):
#     for j in range(i,n):
#         s=0
#         for k in range(i,j+1):
#             s+=nums[k]
#         if s==t:
#             l=max(l,j-i+1)
# print(l)

# # #sliding window 
# a=[100,200,300,400]
# k=2
# n=len(a)
# low=0
# high=k-1
# sum=0
# res=0
# for i in range(low,high+1):
#     sum+=a[i]
# while(high<n):
#     res=max(res,sum)
#     low+=1
#     high+=1
#     if(high==n):
#         break
#     sum=sum-a[low-1]+a[high]
# print(res)

##min size of subarray which is greater or equal to target
# a=[1,2,4,4]
# n=len(a)
# low=0
# high=0
# target=4
# res=float('inf')
# sum=0
# while(high<n):
#     sum=sum+a[high]
#     while(sum>=target):
#         l=high-low+1
#         res=min(res,l)
#         sum=sum-a[low]
#         low+=1
#     high+=1
# print(res)    

