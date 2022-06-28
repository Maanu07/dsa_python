#EVALUATION OF POSTFIX EXPRESSION

class Stack:
  def __init__(self):
    self.list=[]

  #isEmpty
  def isEmpty(self):
    if self.list == []:
      return True
    else:
      return False

  #peek
  def peek(self):
    if self.list != []:
      return self.list[-1]
    
  #push
  def push(self,val):
    self.list.append(val)

  #pop
  def pop(self):
    if self.list!=[]:
      return self.list.pop()

def isOperand(ch):
  if ch >='0' and ch <='9':
    return True
  else:
    return False

def result(ch,opr1,opr2):
  if ch == '*':
    return (opr2 * opr1)
  elif ch=='/':
    return opr2 / opr1
  elif ch=='+':
    return opr2 + opr1
  elif ch=='-':
    return  opr2 - opr1
    

def evalPostfix(exp):
  myStack=Stack()
  for i in exp:
    if isOperand(i):
      myStack.push(int(i))
    else:
      opr1=myStack.pop()
      opr2=myStack.pop()
      myStack.push(result(i,opr1,opr2))
    

  return myStack.peek()


print(evalPostfix('246*+1-'))