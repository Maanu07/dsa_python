#  Array in python can be implemented using the 'array' module in python .
# List in python can store data of different types , but array stores data of same type in it .

import array
import time
import math

# marks=array.array('i',[2,16,34]);
# fruits=array.array('u','mango orange grapes')

# * traversing array
# for mark in marks:
#   print(mark)


# * append to array 
# marks.append(23)
# print(marks)

# * pop from array
# result=marks.pop()
# print(result,marks)

# * get index of any element in array
# result=marks.index(58)
# print(result)

# * occurence of a element in array 
# result=marks.count(34)
# print(result)

# * reverse the order of items in array
# result=marks.reverse()
# print(result,marks)


# * program for rotation of a array 
# * nums=[2,5,9,6,4,7] n=size of array d=rotate array by 
# def rotateArray(nums,n,d):
#     dumArray=[]
#     newArray=[]
#     for i in range(0,d):
#       dumArray.append(nums[i])
#     for y in range(d,n):
#         newArray.append(nums[y])
#     newArray+=dumArray
#     return newArray
    

# print(rotateArray([2,5,9,6,4,7],len([2,5,9,6,4,7]),2))


# * linear search on array 
# myArray=[5,4,9,6,25,21]

# def linearSearch(arr,search):
#     for x in arr:
#       if(x==search):
#         return 'result found'
#       else:
#         continue
#     print('result not found')

# print(linearSearch(myArray,100))

# * Reverse algo for araay rotation 
# nums=[2,5,9,6,4,7]
# d=2
# n=len(nums)
# def reverseArray(arr,start,end):
#   for x in range(start,end):
#     nums

# reverseArray(nums,start,end)

# * Reverse a array
# nums=[2,5,9,6,4,7]
# n=len(nums)
# def reverseArray(arr):
#   for i in range(0,int(n/2)):
#       temp=nums[i]
#       nums[i]=nums[(n-1)-i]
#       nums[(n-1)-i]=temp
#   return arr

# print(reverseArray(nums))

# * Python built in reverse() method
# nums=[2,5,9,6,4]
# nums.reverse()
# print(nums)



# * Trapping Rainwater Problem 

# arr=[2,0,2]
# arr=[3,0,2,0,4]
# arr=[3,4,7,5,2]
# totalVolume=0

# for i in range(1,len(arr)-1): #? O(n)
#   leftMaxBoundary=0
#   rightMaxBoundary=0
#   #getting left max boundary
#   for j in range (0,i):   #? O(n)
#       if (arr[j]>leftMaxBoundary):
#         leftMaxBoundary=arr[j]
#   #getting right max boundary(we can also use built in max() function)
#   for j in range (i+1,len(arr)):  #? O(n)
#      rightMaxBoundary=max(rightMaxBoundary,arr[j])
#   #getting min of the two boundaries
#   if(leftMaxBoundary>rightMaxBoundary):
#     if(rightMaxBoundary-arr[i]>0):
#       totalVolume+=rightMaxBoundary-arr[i]
#   else: 
#     if(leftMaxBoundary-arr[i]>0):
#       totalVolume+=leftMaxBoundary-arr[i]

# print(totalVolume)

#?  time complexity is => O(n*n)



# * Count the number of digit in a given number

# n=int(input())
# count=0
# while(n!=0):
#   n=abs(n)//10
#   count+=1

# print(count)

# ? time colmplexity => O(count)


# * Wave Array question (gfg) (a1>=a2<=a3>=a4<=a5>=a6)
# * A is sorted array , N is the size of array
# def convertToWave(self,A,N):
#         #Your code here
#         if(N%2!=0):
#             for i in range(0,N-1,2):
#                 temp=A[i]
#                 A[i]=A[i+1]
#                 A[i+1]=temp
               
#         else:
#             for i in range(0,N,2):
#                 temp=A[i]
#                 A[i]=A[i+1]
#                 A[i+1]=temp
               
#         return A

# ? time complexity =>  O(N)


# * Laregest and Smallest number in a array 
# ? => time complexity O(N)


# * Bitwise OR operator 
# def game_with_number (arr,  n) : 
#     #Complete the function
#     newarr=[]
    
#     for x in range(0,n):
#         if(x!= n-1):
#             newarr.append(arr[x]|arr[x+1])
#         else:
#             newarr.append(arr[x])
            
#     arr=newarr
#     return arr

# ? => time complexity O(N)


# * Multiply the left and right array sum

# def multiply (arr, n) : 
#     #Complete the function
#     leftArraySum=0
#     rightArraySum=0

#     for x in range(0,n):
#         if(x < n//2):
#             leftArraySum+=arr[x]
#         else:
#             rightArraySum+=arr[x]
#     return leftArraySum * rightArraySum

# ? => time complexity O(N)

# * Form a number divisible by 3 using array digits

# * Check for prime number

# n=int(input())

# def primeNumber(n):
#   count=0
#   for i in range(2,n//2+1):
#     if(n%i==0):
#       count+=1
#   if(count==1):
#     return ('it is a prime number')
#   else:
#     return ('it is not a prime number')

# print(primeNumber(n))
# ? time complexity => O(n/2)    [O(n/2)< O(n)]


# def primeNumber(n):
#   count=0
#   for i in range(2,math.ceil(math.sqrt(n))):
#     if(n%i==0):
#       count+=1
#   if(count==1):
#     return ('it is a prime number')
#   else:
#     return ('it is not a prime number')

# print(primeNumber(n))
# ? time complexity => O(sqrt(n))   


# * print all the prime number from 1 to n
# * print all the substring of a given string

# * Intersection of two arrays

#Check if a key is present in every segment of size k in an array
# arr = array.array('i',[21, 23, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25]) 
# x = 23 
# k = 5 
# for i in range(len(arr)):
#   segmentArray=[]
#   if i+1%k!=0:
#     segmentArray.append(arr[i])
#   else:
#     if x not in segmentArray:
#          print(False)
#          break

  

x  = 10 
print(id(x))
y = x 
print(id(y))
z = 10 
print(id(z))

