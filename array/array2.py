# PYTHON DOES NOT HAVE ARRAY AS A BUILT IN DATA STRUCTURE INSTEAD PYTHON HAS LIST WHICH IS SIMILAR TO ARRAY WITH SOME DIFFERENCES 

# TO CREATE A ARRAY IN PYTHON, ONE MUST USE A ARRAY MODULE

from array import *

#CREATING ARRAY
arr1=array('i',[1,2,3,])

#TRAVERSING ARRAY
for i in arr1:
  print(i)

#ACCESSING ARRAY ELEMENT USING INDEX
print(arr1[2])

#INSERTING ELEMENT AT THE END OF ARRAY
arr1.append(100)

#INSERTING ELEMENT INTO ARRAY 
# array.insert(index,value) 
arr1.insert(2,99)

#DELETING LAST ELEMENT FROM ARRAY
arr1.pop()

#DELETING  ELEMENT FROM ARRAY(removes only first occurence of a number)
arr1.remove(99)

#GETTING INDEX OF ELEMENT IN AN ARRAY
print(arr1.index(1))

#REVERSE ARRAY IN PYTHON
arr1.reverse()

#EXTEND PYTHON ARRAY USING extend METHOD
arr2=array('i',[200,400,500])
arr1.extend(arr2)
print(arr1)

#GET ARRAY BUFFER INFORMATION USING buffer_info METHOD
print(arr1.buffer_info())

#CONVERT ARRAY TO PYTHON LIST WITH SAME ELEMENTS
print(arr1.tolist())

# SEARCH A ELEMENT IN A ARRAY
""" def searchArray(array,num):
  for i in array:
    if i==num:
      return array.index(num)

  return 'Number does not exist in the array'

print(searchArray(arr1,8))
 """

# DELETING A ELEMENT FROM A ARRAY
""" def deleteFromArray(array,num):
  for i in array:
    if i==num:
      array.remove(num)
      return array

    
  return 'Number you want to delete does not exist in the array'

print(deleteFromArray(arr1,3))
 """