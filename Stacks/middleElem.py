class Stack:
  def __init__(self):
      self.stack=[]

  def push(self,value):
    self.stack.append(value)

  def pop(self):
    return self.stack.pop()

  def traversal(self):
    if len(self.stack) > 0:
      for x in self.stack:
        print(x)

  def middle(self):
    if len(self.stack) == 1:
      return self.stack[0]
    elif len(self.stack) > 1:
      mid=len(self.stack) //2
      return self.stack[mid]



s1=Stack()
s1.push(100)
s1.push(200)
s1.push(300)
s1.push(400)
s1.push(500)
s1.push(600)
# s1.traversal()
print(s1.middle()) 



  

