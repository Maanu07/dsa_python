#Infix expression to postfix expression

#isOperand
def isOperand(ch):
  if ch >='a' and ch <='z' or ch>='A' and ch<='Z':
    return True
  else:
    return False

#Checkprecedence 
def checkPre(ch):
  if ch =='+' or ch=='-':
    return 1
  elif ch=='*' or ch=='/':
    return 2
  elif ch =='^':
    return 3
  else:
    return 0

class Stack:
  def __init__(self):
    self.list=[]

  #push
  def push(self,ch):
    self.list.append(ch)
  #pop
  def pop(self):
    if self.list !=[]:
      return self.list.pop()
    else:
      return '%'
  #peek
  def peek(self):
    return self.list[len(self.list)-1]

  

def infixToPostfix(str):
  output=''
  myStack=Stack()
  for i in range(len(str)):
    if isOperand(str[i]):
     output+=str[i]
    elif str[i] =='(':
      myStack.push('(')
    elif str[i] ==')':
      while(myStack.list!=[] and myStack.peek()!='('):
          output+=myStack.pop()
      if myStack.list!=[] and myStack.peek()!='(':
        return -1
      else:
        myStack.pop()
    else:
      while(myStack.list!=[] and checkPre(str[i]) <= checkPre(myStack.peek())):
          output+=myStack.pop()
      myStack.push(str[i])
  
  while(myStack.list!=[]):
    output+=myStack.pop()

  return output


print(infixToPostfix('a+b*(c^d-e)^(f+g*h)-i'))
  

      
      