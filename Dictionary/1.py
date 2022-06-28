#Dictionary is a built in data type in python.
#It is a collection of key:value pairs 
#We can access a value using the corresponding key

#create a empty dictionary                                      time comp => O(1)
myDict=dict()
#OR
myDict={}

#adding key value pairs to dictionary
myDict={"name":"Manas","age":21,"rollno":30,"friends":21}

#lets access any value in the dictionary                         time comp => O(1)
# print(myDict["age"])

#lets update a existing key value pair                           time comp => O(1)
myDict["name"]="Rohan"
# print(myDict["name"])

#No two duplicates key can exist in the dictionary 
secondDict={1:23,2:55,1:100}
# print(secondDict)

#lets traverse the dictionary                                  time comp => O(N)
""" for i in myDict:
  print(i)
for i in myDict.values():
  print(i) """


#search for a value in dict and return its key ,if there exists more keys for same value return them also                                                    time comp => O(N)
""" for i in myDict:
  if myDict[i] == 21:
    print(i) """

#Lets learn how memory is allocated to the dict 
#a hash table is created which is just a array, and every key is passed through the hash function to get a index and then the key:value pair is inserted at that index, in case of collision we create a linked list at that particular index 


#lets delete a existing pair from dict                      time comp => O(1)
""" del myDict['age']
myDict.pop('name')
print(myDict) """

#popitem() method for dict removes a random pair from the dict  
""" print(myDict.popitem())
print(myDict) """

#clear the entire dict
myDict.clear()
print(myDict)

#there is a difference between clearing and deleting entire dict

#lets delete the entire dict
""" del myDict
print(myDict) """