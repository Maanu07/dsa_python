import numpy as np


#Reverse an array using recursion
""" def reverse(arr,start,end):
    if start >= end:
      return arr
    arr[start],arr[end]=arr[end],arr[start]
    return reverse(arr,start+1,end-1)

    
print(reverse([1,2,3,4,5],0,4)) """


#Maximum and minimum of an array using minimum number of comparisons
#method 1 => sort the array and then return the first and last index (nlogn)
#method 2 => take a min and max variable and compare the array elements (linear search)
#method 3 => compare in pairs (best approach ) NOC for odd => 3*(n-1)/2  & NOC for even => 3*(n-2)/2 + 1     time comp => O(N)
""" def minMax(arr,n):
  #if lenght of array is  1
  if n==1:
    min=max=arr[0]
  #if length of array is 2
  elif n==2:
    if arr[0] > arr[1]:
      min=arr[1]
      max=arr[0]
    else:
      min=arr[1]
      max=arr[0]
  #if lenght of array is more than 2
  else:
    #if even number of elements in array
    if n%2 == 0:
      if arr[0] > arr[1]:
        min=arr[1]
        max=arr[0]
      else:
        min=arr[1]
        max=arr[0]
      i=2
    #if number of elements are odd
    else:
      min=max=arr[0]
      i=1
    while(i <= n-2):
      if arr[i] > arr[i+1]:
        if arr[i] > max:
          max=arr[i]
        if arr[i+1] < min:
          min=arr[i+1]
      else:
        if arr[i+1] > max:
          max=arr[i+1]
        if arr[i] < min:
          min=arr[1]
      i+=2
  return (min,max)
      
print(minMax([1000,11,445,1,330,660],6)) """


#Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
#method 1 => space comp => O(3) for hash table and space comp => O(N)  
""" l=[0,1,2,0,0,1,2,2]
def sortFunction(arr):
  myHash={0:0,1:0,2:0} 
  for i in arr:
    if i==0:
      myHash[i]+=1
    elif i==1:
      myHash[i]+=1
    else:
      myHash[i]+=1
  arr=[]
  for i in myHash:
      arr.extend([i for x in range(myHash[i])])
  return arr

print(sortFunction(l)) """
     

#Move all negative numbers to beginning and positive to end with constant extra space
#method 1 = > two pointer approach  time comp => O(N) and space comp => O(1)
""" def moveNegativeToFront(arr):
  start=0
  end=len(arr)-1
  while(start<=end):
    #both negative
    if arr[start] <0 and arr[end] <0:
      start+=1
    #if left positive and right negative then swap them
    elif arr[start] >0 and arr[end] <0:
      arr[start],arr[end]=arr[end],arr[start]
      start+=1
      end-=1
    #if left positive and right also positve
    elif arr[start] > 0 and arr[end] > 0:
      end-=1
    #left negative and right positive
    elif arr[start] < 0 and arr[end] > 0:
      start+=1
      end-=1
  return arr

print(moveNegativeToFront([-12, 11, -13, -5, 6, -7, 5, -3, -6]))  #Output: -12 -13 -5 -7 -3 -6 11 6 5  order is not necessary here  """

#Find the Union and Intersection of the two sorted arrays
#method  1 => but this method does not return the sorted array and not valid for duplicates value
# a = [1, 2, 4, 5, 6]
# b = [2, 3, 5, 7]
a=[1, 2, 2, 2, 3]
b=[2, 3, 4, 5]
""" def union(arr1,arr2):
  n1=len(arr1)
  n2=len(arr2)
  if n1 > n2:
    for i in arr2:
      if i not in arr1:
        arr1.append(i)
    return arr1
  else:
    for i in arr1:
      if i not in arr2:
        arr2.append(i)
    return arr2 """
#method 2 => does not work for duplicate values
""" def union(arr1,arr2):
   i=j=0
   while(i < len(arr1) and j < len(arr2)):
     if arr1[i] > arr2[j]:
       print(arr2[j])
       j+=1
     elif arr1[i] < arr2[j]:
        print(arr1[i])
        i+=1
     elif arr1[i] == arr2[j]:
        print(arr1[i])
        i+=1
        j+=1
   while(i < len(arr1)):
     print(arr1[i])
     i+=1
   while(j < len(arr2)):
     print(arr2[j])
     j+=1
       
union(a,b) """
  
#intersecton 
#method 1   time comp => O(m*n)
""" def intersection(arr1,arr2):
  i=j=0
  m=len(arr1)
  n=len(arr2)
  result=[]
  if m > n :
    for i in arr2:
      for j in arr1:
        if i==j:
          result.append(i)
          break
  else:
    for i in arr1:
      for j in arr2:
        if i==j:
          result.append(i)
          break

  return result """
#method 2 time comp => O(m+n)
""" def intersection(arr1,arr2):
  i=j=0
  m=len(arr1)
  n=len(arr2)
  result=[]
  while( i < m and j < n):
    if arr1[i] == arr2[j]:
      if a[i] not in result:
        result.append(arr1[i])
      i+=1
      j+=1
    elif arr1[i] > arr2[j]:
      j+=1
    else:
      i+=1
  return result

print(intersection(a,b)) """


#take temp of day's and display count of days with temp above avg temp
""" nod=int(input('Enter the number of days? '))
tempList=[float(input("Day "+str(x)+" temp? ")) for x in range(1,nod+1)] #list comprehension, it is a shorthand for list
 
avgTemp=round(sum(tempList)/nod,2)
print('Average: ',avgTemp)
count=0

for i in tempList:
  if i > avgTemp:
    count+=1

print(count, 'Day(s) with above avg temp.') """


#two sum 
#method 1 => nested loop   => time comp => O(n*n)
#method 2 => using hashing => time comp => 0(N) and space comp => O(N)
""" def twoSum(arr,target):
   myHash={}
   total=0
   for i in range(len(arr)):
     total=target - arr[i]
     print(myHash)
     if total in myHash:
       return [i,myHash[total]]
     else:
       myHash[arr[i]]=i

print(twoSum([3,1,2],5)) """



#find the max product of two integers in an array where all elements are +ve
#method 1 => using nested loop   => time comp => O(N*N)
""" def findMaxProduct(arr):
  result=0
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] * arr[j] > result :
          result = arr[i] * arr[j]

  return result """
#method 2 => sorting the array in ascending order and returing product of last two elements
""" def findMaxProduct(arr):
   arr=sorted(arr)   # nlogn
   l=len(arr)
   return arr[l-1] * arr[l-2]

print(findMaxProduct([5,3,2,1,6,4])) """


#check if the array has unique elements or not 
""" def checkForUnique(arr):
  mySet=[]
  for i in arr:
    if i not in mySet:
      mySet.append(i)
    else:
      return 0
  return 1

print(checkForUnique([1,2,3,4,5,1])) """

#Find the missing number from int 1 to 100
""" def missingNumber(list,n):
  sum1=n*(n+1)/2
  sum2=sum(list)
  return int(sum1-sum2)

print(missingNumber([i for i in range(1,100)],100))
 """


#Find the max product of pairs in an array
""" myArray=np.array([20,11,15,17,18,19,23,45])
def findMaxProd(myArray):
    mult=0
    for i in range(len(myArray)):
      for j in range(i+1,len(myArray)):
        prod=myArray[i]*myArray[j]
        if(prod>mult):
          mult=prod
          n1,n2=(i,j)
    return (mult,n1,n2)

print(findMaxProd(myArray)) """

#Calculate the count of distinct element in array
""" myArray=[5,12,4,7,5,4,12]
mySet=set()
print(mySet)
for i in range(len(myArray)):
  mySet.add(myArray[i])

print(mySet,len(mySet))  """

#Get the union of two unsorted arrays     #? => time comp O(m+n)  space comp => O(m+n)
""" array1=[8,4,9,6,5,8,9]
array2=[1,3,4,8,7,9,6]
mySet=set()
for i in range(len(array1)):
  mySet.add(array1[i])
for i in range(len(array2)):
  mySet.add(array2[i])

print(mySet) """

#Get the union of two sorted arrays with duplicate values
""" array1=[2,2,2,3,3,4,2,8]
array2=[1,2,4,4,6,6,7,8,10]
result=[]
i=0
j=0
while(i<len(array1) and j<len(array2)):
  while(array1[i]==array1[i+1]):
    i+=1
  while(array2[j]==array2[j+1]):
    j+=1
  if(array1[i]>array2[j]):
    result.append(array2[j])
    j+=1
    break
  elif (array1[i]<array2[j]):
    result.append(array1[i])
    i+=1
    break
  else :
    result.append(array1[i])
    i+=1
    j+=1
    break

print(result) """

#Range and Coefficient of range of Array
""" myArray=[5,12,4,7,5,4,12]
def findMax(arr):
  Max=arr[0]
  for i in range(1,len(arr)):
    Max=max(arr[i],Max)
  return Max
def findMin(arr):
  Min=arr[0]
  for i in range(1,len(arr)):
    Min=min(arr[i],Min)
  return Min

min=findMin(myArray)
max=findMax(myArray)
range=max-min
coeffOfRange=range/(max+min)
print('Range:'+str(range)+' and Coefficent of range is:'+str(coeffOfRange)) """

#sort arrays of 0's 1's and 2's                             #? time comp => O(n)
#this problem is variation of Dutch national flag problem
# myArray=[ 0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1 ]
""" def sortArray(arr):
  low=0
  mid=0
  high=len(arr)-1
  while(mid<=high):
    if(arr[mid]==0):
      arr[low],arr[mid]=(arr[mid],arr[low])
      low+=1
      mid+=1
    elif arr[mid]==1:
      mid+=1
    elif arr[mid]==2:
      arr[high],arr[mid]=(arr[mid],arr[high])
      high-=1

  return arr
print(sortArray(myArray))
 """
 
#Permutation
#method 1 Sorting  => time comp => O(nlogn)
""" def permutation(arr1,arr2):
  if(len(arr1)!=len(arr2)):
    return False
  arr1.sort()   
  arr2.sort()
  if(arr1==arr2):
    return True
  else:
    return False """
#method 2 => using a map  => time comp => O(N)  space comp => O(256)
""" def permutation(arr1,arr2):
  if len(arr1)!=len(arr2):
    return False
  else:
    #lets create a array of 256 characters
    myChars=[0 for i in range(0,255)]
    for i in arr1:
      myChars[ord(i)]+=1
    for i in arr2:
      myChars[ord(i)]-=1
    for i in range(len(myChars)):
        if myChars[i] !=0:
          print(chr(i))
          return False
    return True
  
print(permutation(['m','a','n','a','s'],['s','a','n','a'])) """

#Find whether an array is subset of another array
# TODO => METHOD 1                   time comp => O(m*n)
arr1=[11, 1, 13, 21, 3, 7]
arr2=[11, 3, 7, 1,]
""" def isSubset(arr1,arr2):
  count=0
  for i in arr2:
    for j in arr1:
      if i==j:
        count+=1
  if count == len(arr2):
    return 'It is a subset'
  else:
    return 'It is not a subset' """

# TODO => METHOD 2
""" def isSubset(arr1,arr2):
  hashSet=set()
  for i in arr1:
    hashSet.add(i)
  for i in arr2:
    if i in hashSet:
      continue
    else:
      return False
  return True """
    
""" print(isSubset(arr1,arr2)) """



#Find common elements in three sorted arrays                  #? time comp => O(n1+n2+n3)
""" ar1 = [1, 5, 10, 20, 40, 80] 
ar2 = [6, 7, 20, 80, 100] 
ar3= [3, 4, 15, 20, 30, 70, 80, 120]

def commonElem():
  i=j=k=0
  comElem=[]
  while(i<len(ar1) and j< len(ar2) and k <len(ar3)):
    if(ar1[i] == ar2[j] and ar2[j]== ar3[k]):
      comElem.append(ar1[i])
      i+=1
      j+=1
      k+=1
    elif (ar1[i] < ar2[j]):
      i+=1
    elif (ar2[j] < ar3[k]):
      j+=1
    else:
      k+=1
  return comElem

print(commonElem()) """
    