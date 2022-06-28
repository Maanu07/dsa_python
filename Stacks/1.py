#STACK USING PYTHON LIST (no size restriction)

class Stack:
  def __init__(self):
    self.list=[]    #global variable of this class

  #check stack is empty or not
  def isEmpty(self):
    if len(self.list) ==0:
      return True
    else:
      return False

  #add element to the stack
  def push(self,value):
    self.list.append(value)
    return 'The element is successfully inserted'

  #remove element from the stack
  def pop(self):
    if self.isEmpty():
      return 'There is no element is the stack'
    else:
      return self.list.pop()
    
  
  #get the top element of the stack
  def peek(self):
    if self.isEmpty():
      return 'There is no element in the stack'
    else:
      return self.list[len(self.list)-1]

  #delete the stack
  def deleteStack(self):
    self.list=None

  #traversing the stack
  def traversal(self):
    if self.isEmpty():
        return 'There is no element in the stack'
    else:
      for i in range(len(self.list)-1,-1,-1):
        print(self.list[i])

  #update stack element 
  def update(self,value,index):
     if self.isEmpty():
        return 'There is no element in the stack'
     else:
      for i in range(len(self.list)-1,-1,-1):
        if i ==index:
          self.list[i]=value
          return 'Updated successfully'
      


customStack=Stack()
# print(customStack.isEmpty())
print(customStack.push(1))
print(customStack.push(2))
print(customStack.push(3))
# print(customStack.peek())
# print(customStack.pop())
# print(customStack.peek())
print(customStack.update(20,1))
customStack.traversal()

