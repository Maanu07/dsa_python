#INCEREASE THE SIZE OF STACK MEMORY 
import sys
# print(sys.getrecursionlimit())  #return 1000 
sys.setrecursionlimit(2000)  #modified my stack memory from 1000 to 2000

#Write a recursive function that takes a number and returns the sum of all the numbers from zero to that number.
""" def sum(n):
  if(n==0):
      return 0
  else:
      return n + sum(n-1)

print(sum(5)) """


#Write a recursive function that takes a number as an input and returns the factorial of that number.
""" def factorial(n):
  assert n>=0 and int(n)==n, 'enter a positive integer number'
  if n in [0,1]:
    return 1
  else :
    return n * factorial(n-1)

print(factorial(-5))
print(factorial(5.2))
print(factorial(5)) """


#Write a recursive function that takes a list of numbers as an input and returns the product of all the numbers in the list.
""" def product(array,n):
    if(n==1):
      return array[0]
    
    return array[n-1]*product(array,n-1)

print(product([5,4,9],3))
     """


#Write a recursive function that takes an array and a callback function and returns True if any value of that array returns True from that callback function otherwise returns False.
""" def isEven(num):
    if num%2==0:
        return True
    else:
        return False

def recursion(array,n):
  if(n<0):
    return False
  if(isEven(array[n])):
    return True
  else: 
    return recursion(array,n-1)

print(recursion([7,3,5,8],3)) """


#Write a recursive function that takes an array of words and returns an array that contains all the words capitalized.
""" def recursion(array):
  if(len(array)>=1):
    return( [array[0].upper()] + recursion(array[1:]))
  else:
    return []

print(recursion(['manas','mansi','suman']))
   """

#Write a recursive function that takes a string and reverse the string.
""" def reverse(text):
  if(len(text)==0):
    return ''
  else:
    return text[len(text)-1] + reverse(text[0:len(text)-1])

print(reverse('change'))
 """



# get the sum of digits of a positive number
""" def sumOfDigits(n):
  assert n>=0 and int(n)==n, 'enter a positive integer number' 
  if(n!=0):
      return n%10 + sumOfDigits(int(n/10))
  else:
    return 0
  

print(sumOfDigits(0)) """

#calculate the power of a number using recursion
""" def powerOfANumber(n,pow):
  assert pow >=0 and int(pow)==pow, 'enter a positive number with power >= 0'
  if(pow==0):
    return 1
  if (pow==1):
    return n
  else:
    return n * powerOfANumber(n,pow-1)

print(powerOfANumber(2,-5)) """

#gcd of 2 numbers using recursion
""" def gcd(a,b):
  assert int(a)==a and int(b)==b, 'enter integer value only'
  if(a<0):
    a=-1*a
  if(b<0):
    b=-1*b
  if (b==0):
    return a
  return gcd(b,a%b)

print(gcd(24,32)) """


#! maximum recursion depth exceeded while calling a Python object
#whenever recursion is working, there exists a call stack which has a fixed size and if our program exceeds the size of stack it raises the above error
""" def display():
  print('manas')
  display()

display() """


#decimal to binary number using recursion
""" def decimalToBinary(num):
  #base condition
  if num == 0:
    return ''
  #work to done in each iteration 
  return str(decimalToBinary(num//2)) + str(num%2)

print(decimalToBinary(23)) """

#sum of first n natural numbers
#method 1 => using iterative approach
""" def sum(n):
  sum=0
  for i in range(1,n+1):
    sum+=i
  return sum """
#method 2 => using recursion
""" def sum(n):
  #base condition 
  if n <= 1:
    return 1
  return n + sum(n-1)
print(sum(10)) """


#Binary search is one of the searching technique , lets implement binary search using recursion
""" def binarySearch(arr,start,end,target):
  #base conditions
  #if value doest not exist in the array
  if start > end :
    return -1
  mid=(start + end )//2
  #comparing with mid element of array
  if target == arr[mid]:
    return mid
  if target > arr[mid]:
    return binarySearch(arr,mid+1,end,target)
  if target < arr[mid]:
    return binarySearch(arr,start,mid-1,target)

print(binarySearch([1,4,5,8,9,15,20],0,6,20)) """

    
#Fibonaci series using recursion  (non optimized solution, we can optimized using memoization)
""" def fibo(n):
  if n<=1:
    return n
  return fibo(n-1) + fibo(n-2)
  
print(fibo(5)) """