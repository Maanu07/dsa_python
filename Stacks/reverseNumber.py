#Reverse a number using stack        #?time comp => O(logN) where N is the number  space comp => O(logN)

class Stack:
  def __init__(self):
    self.list=[]

  #isEmpty
  def isEmpty(self):
    if self.list == []:
      return True
    else:
      return False
  
  #push
  def push(self,val):
    self.list.append(val)

  #pop
  def pop(self):
    if self.list !=[]:
      return self.list.pop()


#1st method 
""" def reverseANumber(num):
    myStack = Stack()
    while(num!=0):
      myStack.push(num % 10)
      num = num // 10
    output = ''
    while(not myStack.isEmpty()):
      output = str(myStack.pop()) + output 
    return output """


#2nd method
""" def reverseANumber(num):
  myStack=Stack()
  output=''
  #pushing digits onto the stack
  for i in str(num):
    myStack.push(i)
  #getting digits from stack
  while(not myStack.isEmpty()):
    output+=myStack.pop()
  return int(output) """

print(reverseANumber(50458))