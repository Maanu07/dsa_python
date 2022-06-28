#string concatenation 

#? Method 1
# print("manas" + " " + "joshi")

#? Method 2
# print("My name is manas {}".format("joshi."))

#? Method 3
# a='Joshi'
# print(f"My name is manas {a}")  #fstring for concatenation of string 




def madlib():
  word1=input('Enter word 1: ')
  word2=input('Enter word 2: ')
  word3=input('Enter word 3: ')
  word4=input('Enter word 4: ')
  word5=input('Enter word 5: ')
  para=f"Hey do you know {word1} is my {word2}. We both often meet {word3} at new york city. I once hold {word4} hammer and kick {word5} ass."
  
  print(para)



def printName():
  print('From another file')