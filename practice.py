#sock pair question 
""" socks=int(input('Enter the number of '))
l=[int(input()) for i in range(0,socks)]
d={}
pairs=0

for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

for j in d.values():
  pairs+=j//2

print(pairs) """


#finding first repeating element in an array
#method 1  =>  time comp O(N*N)
""" def repeating(arr):
  for i in range(0,len(arr)):
    for j in range(1,len(arr)):
      if arr[i]==arr[j]:
        return arr[i] """
      
#method 2 => using hashing  => time comp => O(N)    space comp => O(N)
""" def repeating(arr):
  #tracking minimum index
  min=-1
  dic={}
  for i in range(len(arr)-1,-1,-1):
    if arr[i] in dic.keys():
      min=arr[i]
    else:
      dic[arr[i]]=1
  
  if (min!=-1):
    return (min)
  else:
    print('no repeating element')

print(repeating([1,2,4,5,5,2])) """


#Find the smallest positive missing number in the given array.
""" def findMissingNumber(arr):
  min=arr[0]
  max=arr[1]
  for i in arr:
    if i > max:
      max=i 
    if i < min:
      min=i
  for i in range(min+1,max):
    if i not in arr and i>0:
      return i
  return 'No such missing number' """

#method 2 => using hashing
""" def findMissingNumber(arr):
  mapSet={}
  for i in range(1,max(arr)):
    mapSet[i]=0
  for i in arr:
    mapSet[i]=1
  for i in mapSet:
     if mapSet[i]==0:
       return i


print(findMissingNumber([0, -10, 1, 3, -20])) """


#remove duplicates from string
""" l=[]
s=input('Enter string')
result=''
for i in s:
  if i not in l:
   l.append(i)

for j in l:
  result+=j
  
print(result) """


#Get the address of a variable in python 
""" a=200
memory_address=hex(id(a)) """


#Get the value stored at the address
""" import ctypes
x=200
memory_address=id(x)
print(ctypes.cast(memory_address,ctypes.py_object).value) """


#Get a random number in python
""" import random 
a=random.randrange(1,10)
print(a) """

#Dictionary in python
""" myBio={
  "name":"Manas",
  "age":21,
  "rollNo":30,
  "branch":"CSE"
} """


#Classes in python
""" class Student:
  def __init__(self,name,age,branch):
    self.sname=name
    self.sage=age
    self.sbranch=branch
  
s1=Student('Manas',21,'CSE')
print(s1.age) """


#Convert numeric words to numbers
""" help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero' : '0'
}
test_str = "zero four zero one five eight six"
result=''.join([help_dict[j] for j in test_str.split()])
print(result) """


#Word location in String
""" test_str = 'geeksforgeeks is best for geeks'
wrd = 'best'
pos=0
for word in test_str.split():
  pos+=1
  if word == wrd:
    print(pos)
    break """


""" N=int(input())
M=int(input())
X=int(input())
result=((N-1) * X )- (M*(N-1))
print(result) """



""" N=int(input())
a=[]
maxProd=0
key=None

for x in range(N):
  a.append(int(input()))

for i in range(N):
  if i ==0:
    maxProd=a[i+1] * a[N-1]
    key=a[i]
  elif i== N-1:
      prod=a[i-1] * a[0]
      if prod > maxProd:
        maxProd=prod
        key=a[i]
  else:
    prod=a[i-1] * a[i+1]
    if prod > maxProd:
      maxProd=prod 
      key=a[i]

print(key) 
 """


""" N=int(input())
arr=[]
cost=0
for i in range(N):
  arr.append(int(input()))
i=0
while(i < N):
  if i==0:
    cost+=arr[i]
    i+=2
  else:
    if arr[i] < arr[i-1]:
      cost+=arr[i]
      i+=2
    else:
      i=i-1
print(cost) """
   


# N=int(input())
# I=int(input())
# X=int(input())
# Y=int(input())
# m=1
# n=I - m
# while(X*m + Y*n != N and m<=n):
#     m+=1
#     n=I - m
# print(m)


  

  
""" M=int(input())
X=int(input())
N=int(input())
A=[int(input()) for x in range(M)]
myDict={}
flag=0

for x in A:
  if x not in myDict:
    myDict[x]=1
  else:
    myDict[x]+=1

print(myDict)
for y in myDict:
  if myDict[y]==X and A.index(y) == N:
    flag=1
    print(y)
    break

if flag == 1:
  pass
else: 
  print('Sorry') """
  

""" def abc(expr):
    stack = []
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if stack:
        return False
    return True
 

expr=input()
if abc(expr):
        print("Yes")
else:
        print("No") """
 
#Tree
#Binary Tree(atmost 2 child)
#BST 
""" class Tree:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value
    
    def insert(self,data):
        if self.data > data :
            if self.left is None:
                self.left=Tree(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right=Node(data)
            else:
                self.right.insert(data)
            
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
            
    def searchForValue(self,target):
        if self.data > target:
            if self.left is None:
                return 'Not found'
            return self.left.searchForValue(target)
        elif self.data < target:
            if self.right is None:
                return 'Not found'
            return self.right.searchForValue(target)
        else:
            return 'Found'
        
        
      
root=Tree(10)
root.insert(14)
root.insert(7)
root.insert(11)
print(root.searchForValue(8)) """



""" class Node:
  def __init__(self,data):
    self.data=data 
    self.left=None
    self.right=None 

  def insert(self,data):
    if self.data > data:
      if self.left is None:
        self.left=Node(data)
      else:
        self.left.insert(data)
    else:
      if self.right is None:
        self.right=Node(data)
      else:
        self.right.insert(data)

  def traverse(self):
      if self:
        print(self.data,end=' ')
        if self.left is not None:
          self.left.traverse()
        if self.right is not None:
          self.right.traverse()
    

root=Node(10)
root.insert(20)
root.insert(8)
root.insert(5)
root.insert(7)
root.insert(15)
root.traverse() """






#Queue 
""" class Queue:
  def __init__(self):
    self.queue=[]
    
  def enqueue(self,data):
    if data not in self.queue:
      self.queue.insert(0,data)
      return 'Added successfully'
    return 'Already Exist '

  def printQueue(self):
    for i in self.queue[::-1]:
      print(i,end=' ')

  def dequeue(self):
    if len(self.queue) > 0:
      self.queue.pop()
      return 'Deleted Succesfully '
    else:
      return 'Queue is empty'

  def sizeOfQueue(self):
    print( f"The size of queue is {len(self.queue)}")
  

  
myQueue=Queue()
print(myQueue.enqueue(10))
print(myQueue.enqueue(20))
print(myQueue.enqueue(30))
myQueue.printQueue()
print(myQueue.dequeue())
myQueue.printQueue()
myQueue.sizeOfQueue() """



#Sets 
""" A={10,20,30}
B={30,40,50}
print(A - B)
print(A | B)
print(A & B)
print(B - A) """


#Dequeue (Double  ended queue)
""" import collections 

deq=collections.deque([10,20,30])
deq.append(40)
deq.appendleft(50)
print(deq)
deq.pop()
deq.popleft
print(deq) """


#Decimal to binary  (Wipro NTH)
""" n=int(input())
l=[]
while(n>0):
  rem=n%2
  l.append(rem)
  n=n//2

for i in range(len(l)-1,-1,-1):
  print(l[i],end='') """


#Wipro NTH
""" n=int(input())
k=int(input())
l=[] 
m=[] #copy of l
s=[]  #stores index
for i in range(n):
    l.append(int(input()))
m.extend(l)
l.sort()
l.reverse()
for i in range(0,k):
   ind=m.index(l[i])
   if ind in s:
     l[ind]=-1
     ind=m.index(l[i])
   s.append(ind)
s.sort()
for j in s:
  print(m[j],end=' ') """



#Count of unique words in string (Wipro NTH)
""" s=input()
l=s.split(' ')
d={}
count=0
for i in l:
  if i not in d:
    d[i]=1
  else:
    d[i]+=1

for j in d:
  if d[j]==1:
    count+=1

print(count) """




#Max element in stack
""" class Stack:
  def __init__(self):
    self.stack=[]

  def push(self,data):
    self.stack.append(data)
    return 'Added successfully'
  
  def pop(self):
    if len(self.stack) == 0:
      return 'No element in stack'
    else:
      self.stack.pop()
      return 'Deleted successfully'

  def peek(self):
    return self.stack[-1]

  def getMax(self):
    initialMax=-1
    while(len(self.stack)!=0):
      val=self.stack.pop()
      if val > initialMax:
        initialMax=val
    return initialMax


stackX=Stack()
stackX.push(10)
stackX.push(20)
stackX.push(30)
stackX.push(40)
print(stackX.getMax()) """


#Wipro NTH
""" N=int(input())
X=int(input())
l=[]

for j in range(N):
  l.append(int(input()))

if X in l:
  print(l.index(X))
else:
  for i in l:
    if i > X:
      print(l.index(i))
      break """

#Wipro NTH 
""" N=int(input())
l=list(map(int,input().split(' ')))
prime=[]
nonPrime=[]
def isPrime(n):
  for i in range(2,n//2 + 1):
    if n % i ==0:
      return False
  return True 
for i in l:
  if isPrime(i):
    prime.append(i)
  else:
    nonPrime.append(i)
print(prime + nonPrime) """

#Wipro NTH
""" s=input()
result=''
for i in s:
  if i == ' ':
    result+=i
  elif i.isupper():
    result+=i.lower()
  elif i.islower():
    result+=i.upper()
print(result) """


#Wipro NTH
""" N=list(input().split(' '))
thousand=[]
hundred=[]
tens=[]
ones=[]
result=''
for i in N:
  thousand.append(i[0])
  hundred.append(i[1])
  tens.append(i[2])
  ones.append(i[3])

result=min(thousand) + max(hundred) + min(tens) + max(ones)
print(result) """


#Wipro NTH
""" N=int(input())
l1=list(map(int,input().split(' ')))
l2=list(map(int,input().split(' ')))
count=0
for i in l1:
  flag=len(l2)
  for j in l2:
    if j % i==0:
      flag-=1
  if flag == 0:
    count+=1

print(count) """

#missing number in an array of 1 to 100
# => sum upto 1 to 100 minus sum of array, will give us missing number 

#print duplicates numbers in an array 
""" arr=list(map(int,input('Enter the array elements ').split(' ')))
hashMap={}
for i in arr:
  if i not in hashMap:
    hashMap[i]=1
  else:
    print(i) """
    

#remove duplicate elements from array 
#else statement in python with loop does not execute when the loop is stopped using break
#you can also create a set to remove duplicates from array
#method 2 is below 
""" arr=list(map(int,input('Enter the array elements ').split(' ')))
result=set(arr)
for i in arr:
  if len(result)==0:
    result.append(i)
  else:
    for j in result:
      if j == i:
        break 
    else:
       result.append(i)
print(result) """


#largest & smallest number from a unsorted array 
""" arr=list(map(int,input('Enter the array elements ').split(' ')))
#bubble sort 
for i in range(len(arr)):
  for j in range(0,len(arr)-1):
    if arr[j] > arr[j+1]:
      temp=arr[j]
      arr[j]=arr[j+1]
      arr[j+1]=temp
def getmax(arr):
  print(arr[-1])
def getmin(arr):
  print(arr[0])
getmin(arr)
getmax(arr) """


#find all pairs whose sum is equal to given number 
# arr=list(map(int,input('Enter the array elements ').split(' ')))



#first non repeated character in a string
""" str='hello'
hashMap={}
for i in str:
   if i not in hashMap:
     hashMap[i]=1
   else:
      hashMap[i]+=1


for j in  hashMap:
  if hashMap[j]==1:
    print(j)
    break """


#first repeated character in a string 
""" s='manas'
hashMap={}
for i in s:
  if i not in hashMap:
    hashMap[i]=1
  else:
    hashMap[i]+=1
for j in hashMap:
  if hashMap[j]!=1:
    print(j)
    break """


#intersection of two sorted arrays 
""" a1=[2,4,6,8,10]
a2=[1,3,5]
result=[]
for i in a1:
  for j in a2:
    if i <= j:
      if i==j:
        result.append(i)
        break 
print(result) """


#kth smallest element in an array 
#Time comp => nlogn due to sorting 
#2. method => using min heap or max heap
""" a=list(map(int,input().split(' ')))           
k=int(input())
a.sort()
print(a[k-1]) """


#find common elements in three sorted array
""" a1=list(map(int,input().split(' ')))
a2=list(map(int,input().split(' ')))
a3=list(map(int,input().split(' ')))
result=[]
for i in a1:
  for j in a2:
    if i == j:
      for k in a3:
        if j==k:
          result.append(k)
          break

print(result) """

""" N=int(input())
K=int(input())
a1=[]
for i in range(N):
  a1.append(int(input()))
count=0
a1.sort()
j=0
for i in range(len(a1)-1,-1,-1):
  if a1[i] == K:
   count+=1
  elif a1[i] < K:
    if a1[i] + a1[j] == K:
      count+=1 
    elif a1[i] + a1[j] < K:
      dummy=[a1[i],a1[j]]
      j+=1
      dummy.append(a1[j])
      while sum(dummy) < K :
        j+=1
      count+=1
print(count) """
         








#snake and ladder game
# import time
# import random
# import sys

# # just of effects. add a delay of 1 second before performing any action
# SLEEP_BETWEEN_ACTIONS = 1
# MAX_VAL = 100
# DICE_FACE = 6

# # snake takes you down from 'key' to 'value'
# snakes = {
#     8: 4,
#     18: 1,
#     26: 10,
#     39: 5,
#     51: 6,
#     54: 36,
#     56: 1,
#     60: 23,
#     75: 28,
#     83: 45,
#     85: 59,
#     90: 48,
#     92: 25,
#     97: 87,
#     99: 63
# }

# # ladder takes you up from 'key' to 'value'
# ladders = {
#     3: 20,
#     6: 14,
#     11: 28,
#     15: 34,
#     17: 74,
#     22: 37,
#     38: 59,
#     49: 67,
#     57: 76,
#     61: 78,
#     73: 86,
#     81: 98,
#     88: 91
# }

# player_turn_text = [
#     "Your turn.",
#     "Go.",
#     "Please proceed.",
#     "Lets win this.",
#     "Are you ready?",
#     "",
# ]

# snake_bite = [
#     "boohoo",
#     "bummer",
#     "snake bite",
#     "oh no",
#     "dang"
# ]

# ladder_jump = [
#     "woohoo",
#     "woww",
#     "nailed it",
#     "oh my God...",
#     "yaayyy"
# ]


# def welcome_msg():
#     msg = """
#     Welcome to Snake and Ladder Game.
#     Version: 1.0.0
#     Developed by: https://www.pythoncircle.com

#     Rules:
#       1. Initally both the players are at starting position i.e. 0. 
#          Take it in turns to roll the dice. 
#          Move forward the number of spaces shown on the dice.
#       2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
#       3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
#       4. The first player to get to the FINAL position is the winner.
#       5. Hit enter to roll the dice.

#     """
#     print(msg)


# def get_player_names():
#     player1_name = None
#     while not player1_name:
#         player1_name = input("Please enter a valid name for first player: ").strip()

#     player2_name = None
#     while not player2_name:
#         player2_name = input("Please enter a valid name for second player: ").strip()

#     print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
#     return player1_name, player2_name


# def get_dice_value():
#     time.sleep(SLEEP_BETWEEN_ACTIONS)
#     dice_value = random.randint(1, DICE_FACE)
#     print("Its a " + str(dice_value))
#     return dice_value


# def got_snake_bite(old_value, current_value, player_name):
#     print("\n" + random.choice(snake_bite).upper() + " ~~~~>")
#     print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))


# def got_ladder_jump(old_value, current_value, player_name):
#     print("\n" + random.choice(ladder_jump).upper() + " ########")
#     print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


# def snake_ladder(player_name, current_value, dice_value):
#     time.sleep(SLEEP_BETWEEN_ACTIONS)
#     old_value = current_value
#     current_value = current_value + dice_value

#     if current_value > MAX_VAL:
#         print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
#         return old_value

#     print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
#     if current_value in snakes:
#         final_value = snakes.get(current_value)
#         got_snake_bite(current_value, final_value, player_name)

#     elif current_value in ladders:
#         final_value = ladders.get(current_value)
#         got_ladder_jump(current_value, final_value, player_name)

#     else:
#         final_value = current_value

#     return final_value


# def check_win(player_name, position):
#     time.sleep(SLEEP_BETWEEN_ACTIONS)
#     if MAX_VAL == position:
#         print("\n\n\nThats it.\n\n" + player_name + " won the game.")
#         print("Congratulations " + player_name)
#         print("\nThank you for playing the game. Please visit https://www.pythoncircle.com\n\n")
#         sys.exit(1)


# def start():
#     welcome_msg()
#     time.sleep(SLEEP_BETWEEN_ACTIONS)
#     player1_name, player2_name = get_player_names()
#     time.sleep(SLEEP_BETWEEN_ACTIONS)

#     player1_current_position = 0
#     player2_current_position = 0

#     while True:
#         time.sleep(SLEEP_BETWEEN_ACTIONS)
#         input_1 = input("\n" + player1_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
#         print("\nRolling dice...")
#         dice_value = get_dice_value()
#         time.sleep(SLEEP_BETWEEN_ACTIONS)
#         print(player1_name + " moving....")
#         player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

#         check_win(player1_name, player1_current_position)

#         input_2 = input("\n" + player2_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
#         print("\nRolling dice...")
#         dice_value = get_dice_value()
#         time.sleep(SLEEP_BETWEEN_ACTIONS)
#         print(player2_name + " moving....")
#         player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)

#         check_win(player2_name, player2_current_position)


# start()


class Node:
  def __init__(self,val):
      self.data = val 
      self.next = None

n1 = Node(23)
n2 = Node(25)
n3 = Node(27)

class SLL:

  def __init__(self):
    self.head = None

  def addNode(self,val):
    newNode = Node(val)
    if(self.head == None):
      self.head = newNode 
    else:
      temp = self.head 
      while(temp.next != None):
        temp = temp.next 
      temp.next = newNode

  def traversal(self):
    temp = self.head 
    while(temp != None):
      print(temp.data)
      temp = temp.next

l1 = SLL()
l1.addNode(33)
l1.addNode(35)
l1.traversal()
   
