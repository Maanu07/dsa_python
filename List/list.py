# List  is a built in DS in python...List and array are similar with some differences

#Creating a list
fruits=['mango','orange','apple']
mixedList=['butter',1,1.5,[4,5.8,['mango','apple']]]

#Accessing list elements (similar to accessing array elements)
print(mixedList[2])

#We can access list elements using negative indexes also(negative indexing starts from -1,-2,-3,......)
print(mixedList[-1])

#Traversing the list 
for i in range(len(mixedList)):
  print(mixedList[i])

for i in mixedList:
  print(i)

#Check if a element exist in a list using 'in' operator
print('apple' in fruits) 

#Add a element to the end of the list using 'append' method
mixedList.append(500)
print(mixedList)

#Add element to a specific position in a list using 'insert' method
fruits.insert(0,'litchi')
print(fruits)

#Add a list items to another list using 'extend'
fruits.extend([10,11,12])
print(fruits)

#Deleting elements from a list using pop(index) , delete() , remove(value)
# fruits.pop(1)                          #returns the deleted element
# fruits.pop()                           #delete the lase element
# fruits.remove('mango')                 #returns none
# del fruits[1]                         #returns none
# print(fruits)

#To get particular elements from a list, we can use slicing [start:stop] operator
print(fruits[2:])

#Searching for a element in a list using 'linear search algo'
def searchList(list,value):
  for x in list :
    if x ==value:
      return list.index(value)
  return('The element does not exist in  the list')
print(searchList([100,200,300,400],500))
print(searchList([100,200,300,400],200))

#Few functions that we can apply to list ds
myIntegerList=[1,2,3,4,5,6,7,8,9]
print(sum(myIntegerList))
print(len(myIntegerList))
print(int(sum(myIntegerList)/len(myIntegerList)))
print(min(myIntegerList))
print(max(myIntegerList))


#List Comprehension
tableOfTwo=[i*2 for i in range (1,11)]
print(tableOfTwo)


#Unpacking of tuple , similar to destructuring in JS
a=100
b=99
dummyTupple=(99,100)
a,b=dummyTupple
print(a,b)

#Reverse a list
mylist=[1,2,3,4,5]
mylist=mylist[::-1]
print(mylist)

#Cloning a list
list1=[100,200,300]
list2=list1[:]      #slicing returns a new python list
print(list1,list2)
list1[0]=1000
print(list1,list2)

#Finding the count of element in a list
mylist=[100,200,50,100,566,88,100]
print(mylist.count(100))  #second method is using for loop

#Sum and average of elements in list
print(sum(mylist))
print('Average:'+str(sum(mylist)/len(mylist)))

#Sum of number digits in a list
newList=[]
for i in mylist:
  count=0
  for j in str(i):
      count+=int(j)
  newList.append(count)

print(newList)

#Delete all elements of a pyhton list or clear a list
mylist.clear()          #second method is  reinitialization to empty list
print(mylist)

#Program to print duplicates from a list of integers
newlist = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
def printDuplicates(newlist):
  size=len(newlist)
  repeated=[]
  for  i in range(size):
    for j in range(i+1,size,1):
      if(newlist[i]==newlist[j] and newlist[i] not in repeated):
        repeated.append(newlist[i])

  return repeated

print(printDuplicates(newlist))



#Python program to count positive and negative numbers in a list
posCount=0
negCount=0
for i in newlist:
  if(i >= 0):
    posCount+=1
  else:
    negCount+=1
print(negCount,posCount)

# Extract elements with Frequency greater than K
test_list=[4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
K = 2
new_list=[]
for i in test_list:
  frequency=test_list.count(i)
  if(frequency > K and i not in  new_list):
    new_list.append(i)

print(new_list)

#Create a list from a string   
str='woderland funcity corbett disneyland'
strToList=str.split()
print(strToList)

#String from list
str= '-'.join(strToList)
print(str)