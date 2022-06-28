# 2D array is a collection of multiple 1D array
# To target any element in a 2D array we need 2 indexes

import numpy as np
from numpy.lib.function_base import average

# Creating 2D array in python
twoDArray=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
#twoDArray=np.zeros((4,3),dtype=int)
print(twoDArray)

#? Time Complexity Of Creating 2D array is O(1) by above method
#? If we individually assign value to 2D array elements it will take O(m*n)
#? Space complexity for creating 2D array is O(m*n)

#Inserting new data into 2D array     #?O(m*n)
new2DArray=np.insert(twoDArray,0,[[97,98,99,100]],axis=1)
print(new2DArray)

#Inserting elements to the end of 2D array      #?O(1)
new2DArray=np.append(twoDArray,[[101,102,103]],axis=0)
print(new2DArray)

#Traversing 2D array                #?O(m*n)
for x in new2DArray :
  print(x)
  for y in x:
    print(y)

#Using indexes to get an element     #?O(1)
print(new2DArray[1][2])   

#Get the number of rows in a 2D array
print(len(new2DArray))

#Get the number of columns in a 2D array
print(len(new2DArray[0]))

#Total elements in an 2D array
print(len(new2DArray) * len(new2DArray[0]))

#Searching for a element in 2D array       #?O(m*n)
def searchElement(array,value):
  for i in range(len(array)):
    for j in range(len(array[0])):
      if(array[i][j]==value):
        return 'Element is present at row '+str(i)+' column '+str(j)
  return 'Element does not found in the array'

print(searchElement(new2DArray,102))

#Deleting an row/column in a 2D array       #?O(m*n)
print(np.delete(twoDArray,0,axis=1))



myarray=[-12, 11, -13, -5, 6, -7, 5, -3, -6]
i=0
j=len(myarray)-1
while(j>i):
  if(myarray[i]<0 and myarray[j]>0):
    i+=1
    j-=1
  elif (myarray[i]>0 and myarray[j]<0):
    (myarray[i],myarray[j])=(myarray[j],myarray[i])
  elif (myarray[i]<0 and myarray[j])