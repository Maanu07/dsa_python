#Find minimum element in the stack in constant time   #?time comp => O(1) and space comp => O(n)

""" class Stack:
  def __init__(self):
    self.main=[]
    self.aux=[]

  #isEmpty
  def isEmpty(self):
    if self.main == []:
      return True
    else:
      return False

  #peek
  def peek(self):
    if self.main != []:
      return self.main[-1]

  #push 
  def push(self,value):
    self.main.append(value)
    if self.aux ==[]:
      self.aux.append(value)
    elif value < self.aux[-1]:
      self.aux.append(value)

  #pop
  def pop(self):
    if self.isEmpty():
      print('Stack underflow')
      return -1
    top=self.main.pop()
    if top == self.aux[-1]:
      self.aux.pop()
    return top

  #getMin
  def getMin(self):
    if not self.aux:
        print('Stack underflow')
        return -1
    return self.aux[-1]
  
customStack=Stack()
customStack.push(6)
customStack.push(7)
customStack.push(8)
customStack.push(5)
customStack.push(3)
customStack.pop()
customStack.push(10)
customStack.pop()
customStack.pop()
print(customStack.getMin()) """


#Find minimum element in the stack in constant time and O(1) space comp   #?time comp => O(1) and space comp => O(1)


""" class Stack:
  def __init__(self):
    self.main=[]
    self.min=None

  #isEmpty
  def isEmpty(self):
    if self.main == []:
      return True
    else:
      return False

  #peek
  def peek(self):
    if self.main != []:
      return self.main[-1]

  #push 
  def push(self,value):
    if self.main == []:
      self.main.append(value)
      self.min=value
    else:
      if value > self.min:
        self.main.append(value)
      else:
        self.main.append(2*value-self.min)
        self.min=value

  #pop
  def pop(self):
    if self.isEmpty():
      print('Stack underflow')
      return -1
    curr=self.main.pop()
    if curr < self.min:
        self.min=2*self.min - curr
    

  #getMin
  def getMin(self):
    if not self.main:
        print('Stack underflow')
        return -1
    return self.min
 """

customStack=Stack()
customStack.push(6)
customStack.push(7)
customStack.push(8)
customStack.push(5)
customStack.push(3)
customStack.pop()
customStack.push(10)
customStack.pop()
customStack.pop()
print(customStack.getMin())