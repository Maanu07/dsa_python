# Reverse a string
# => Method 1
""" myStr='Hey this is a string'
def reverseStr():
  output=''
  for i in range(len(myStr)-1,-1,-1):
    output+=myStr[i]  
  return output

print(reverseStr()) """

# => Method 2
""" myStr='Hey this is a string'
def reverseStr():
  output=''
  for i in myStr:
    output= i + output
  return output

print(reverseStr()) """

# => Method 3 (recursion)
""" myStr='manas'
def reverseStr(s):
  if len(s)==0:
    return s
  else:
    return reverseStr(s[1:]) + s[0]
print(reverseStr(myStr)) """

# Print duplicate characters from a string
# Method 1 (using hashing)          #? time comp => O(n)  space comp => O(n)
""" myStr='sadlnajsd nsj sadasdk'
def printDuplicates():
    NO_OF_CHARS=256
    count=[0]*NO_OF_CHARS  #array with a length of 256 and each element as  0
    for i in myStr:
      count[ord(i)]+=1
    for i in range(0,len(count)):
      if count[i] > 1:
        print(chr(i))
printDuplicates() """


#How do you check if two strings are anagrams of each other?  
#Method 1              #? time comp => O(n)  space comp => O(2*NO_OF_CHARS)                      
""" def isAnagram(str1,str2):
  NO_OF_CHARS=256
  m,n=(len(str1),len(str2))
  if(m==n):
    hashTable1=[0]*NO_OF_CHARS
    hashTable2=[0]*NO_OF_CHARS
    for i in str1:
      hashTable1[ord(i)]+=1
    for j in str2:
      hashTable2[ord(j)]+=1
    if(hashTable2==hashTable1):
      return 'Strings are anagram'
    else:
       return 'Strings are no anagram'
  else:
    return 'Strings are no anagram' """

#TODO => The above implementation can be further to use only one count array instead of two. We can increment the value in count array for characters in str1 and decrement for characters in str2. Finally, if all count values are 0, then the two strings are anagram of each other.


#Method 2 (using sorting)  #? time comp => O(nlogn)    
""" def isAnagram(str1,str2):
   m,n=(len(str1),len(str2))
   if(m==n):
    str1=sorted(str1)  #sorted function in python returns a list of sorted elements
    str2=sorted(str2)  #O(nlogn)
    if(str1==str2):
      return 'Strings are anagram'
    else:
      return 'Strings are not anagram'
   else:
    return 'Strings are not anagram'

print(isAnagram('manas','sanam')) """

#How do you check if a string contains only digits?
#Method 1           #? time comp => O(n)
""" def onlyDigits(str1):
  for i in str1:
    if (i>='0' and i <='9'):
      continue
    else:
      return False
  return True
 """


#Method 2          #? time comp => O(n)
""" def onlyDigits(str1):
  for i in str1:
    if i.isdigit():
      continue
    else:
      return False
  return True

print(onlyDigits('59887'))
 """

#How do you count a number of vowels and consonants in a given string?   #? time comp => O(n)
""" def countVowels(str1):
  vowels=0
  consonants=0
  for i in str1:
    if i =='a' or i=='e' or i=='i' or i=='o' or i=='u':
      vowels+=1
    else:
      consonants+=1
  return (vowels,consonants)

print(countVowels('permutations'))
 """

##Function to reverse words in a given string.
""" def reverseWords(S):
        # code here 
        output=''
        word=''
        for i in range(len(S)-1,-1,-1):
            if(S[i]!='.'):
                word=S[i]+word
            else:
                word+='.'
                output+=word
                word=''
                
        output+=word
        return output """


#A Program to check if strings are rotations of each other or not
""" def rotationStrings(str1,str2):
      if len(str1) == len(str2):
        temp=str1+str1
        if temp.count(str2) > 0:
          return True
        else:
          return False
      else:
        return False


print(rotationStrings('manas','asman')) """

#A program to reverse each words in a string
""" def reverseWords(mystr):
    st=list();   #st=stack
    for i in range(0,len(mystr)):
        if mystr[i] !=' ':
            st.append(mystr[i]);
        else:
            while(len(st)>0):
                print(st.pop(),end='');
            print(' ',end='')
    while(len(st)>0):
        print(st.pop(),end='');
                        
reverseWords('manas joshi')
 """

#Check whether the String is a palindrome or not.
#Solution => reverse the string and compare them.. (you can also try solving using recursion)
""" def palindrone(mystr,i,j):
  if i>=j:
    return True
  elif mystr[i]!=mystr[j]:
    return False
  return palindrone(mystr,i+1,j-1)

print(palindrone('nitin',0,len('nitin')-1)) """


# print the first non repeating character from the string 
myStr='adadall'
alpha=[0]*26           #hash table (you can also take 256 character array)
for char in myStr:
    alpha[ord(char)-ord('a')]+=1
    
for char in myStr:
    if alpha[ord(char)-ord('a')]==1:
        print(char) 
        break
else:
    print('no non repeating character found')