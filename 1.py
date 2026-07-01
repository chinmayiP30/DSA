#2sum
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


#removing duplicants 
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


#moving zeros
# nums = [0,1,0,3,12]
# j=0
# for i in range(len(nums)):
#     if nums[i]!=0:
#         nums[j],nums[i]=nums[i],nums[j]
#         j+=1
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
    

#merging of two sorted arrays
a = [1,2,8]
m= 3
b = [2,5,6]
n = 3
i=0
j=0
res=[0]*(m+n)
k=0
while i<m and j<n:
    if a[i]<=b[j]:
        res[k]=a[i]
        i+=1
        k+=1
    else:
        res[k]=b[j]
        j+=1
        k+=1
while i<m:
    res[k]=a[i]
    i+=1
    k+=1
while j<n:
    res[k]=b[j]
    j+=1
    k+=1
print(res)

#squaring of sorted array
a=[-4,-2,1,4,6]
n=len(a)
res=[]
for i in a:
    res.append(i**2)
    i+=1
res.sort()
print(res)


#squaring of sorted array without sort function
main=[-4,-1,0,3,10]
a=[]
b=[]
for i in range (len(main)):
    if main[i]>=0:
        b.append(main[i])
    else:
        a.append(main[i])
if len(a)!=0:
    for i in range(len(a)):
        a[i]=a[i]*a[i]
    a.reverse()
if len(b)!=0:
    for i in range (len(b)):
        b[i]=b[i]*b[i]
i=0
j=0
m=len(a)
n=len(b)
res=[0]*(m+n)
k=0
while i<m and j<n:
    if a[i]<=b[j]:
        res[k]=a[i]
        i+=1
        k+=1
    else:
        res[k]=b[j]
        j+=1
        k+=1
while i<m:
    res[k]=a[i]
    i+=1
    k+=1
while j<n:
    res[k]=b[j]
    j+=1
    k+=1
print(res)



