#STACK USING PYTHON LIST (with a fixed size)

class Stack:
  def __init__(self,maxSize):
    #maxSize = number of elements that i want in the stack
    self.maxSize=maxSize
    self.list=[]

  #isEmpty                                      #? time comp => O(1)  space comp => O(1)
  def isEmpty(self):  
    if self.list==[] or len(self.list)==0:
      return True
    else:
      return False

  #isFull                                      #? time comp => O(1)  space comp => O(1)
  def isFull(self):
     if len(self.list)==self.maxSize:
       return True
     else:
       return False

  #push                                        #? time comp => O(1)/O(N)  space comp => O(1)
  def push(self,value):
    if self.isFull():
      return 'The stack is full'
    else:
      self.list.append(value)
      return 'The element is inserted successfully'

  #pop                                        #? time comp => O(1)  space comp => O(1)
  def pop(self):
    if self.isEmpty():
      return 'There is no element in the stack'
    else:
      return self.list.pop()
  
  #peek                                       #? time comp => O(1)  space comp => O(1)
  def peek(self):
    if self.isEmpty():
      return 'There is no element in the stack'
    else:
      return self.list[len(self.list)-1]

  #delete entire stack                        #? time comp => O(1)  space comp => O(1)
  def deleteStack(self):
    self.list=None


  #traverse                                    #? time comp => O(n)  space comp => O(1)
  def traversal(self):
    if self.isEmpty():
      print('The stack is empty')
    else:
      for i in range(len(self.list)-1,-1,-1):
        print(self.list[i])
      
customStack=Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
print(customStack.push(1))
print(customStack.push(2))
print(customStack.push(3))
print(customStack.push(4))
print(customStack.push(5))
print(customStack.peek())
print(customStack.pop())
customStack.traversal()