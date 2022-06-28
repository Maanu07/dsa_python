#STRINGS => string is a sequence of characters , a character is a string with length of 1
# In python  strings can be declared using single , double , triple quotes
#String with triple quotes allows multi line string

# Creating a string
para='''This is first line 
This is second line
And this is third line'''
print(para)

#  Accessing characters in Python is done using indexes (negative + positive indexing)
print(para[10])

# String Slicing (To access a range of characters in the String, method of slicing is used)
print(para[10:15:1])

#TODO : In Python, Updation or deletion of characters from a String is not allowed.Strings are immutable ,  we can either delete the entire string or reassign the entire string
myString='Hey my name is manas joshi and i am 20 years old.'
del myString           #deletes string 
myString='New String'  #updates string or resassignment

# Escape Sequencing in Python
myString='I\'m a senior manager in my department'
myString="I'm a senior manager in my department"   #alternative to escape character

# Formatting of Strings
print('{1} {0} {2}'.format('first',25,[1,2,3]))

# Logical Operators on String in Python

