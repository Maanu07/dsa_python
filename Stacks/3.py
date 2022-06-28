#STACK USING LINKED LIST
#Using linked list i can implement stack in  2 ways :
# 1. inserting and deleting from end
# 2. inserting and deleting from front

class Node:
  def __init__(self,value=None):
    self.value=value
    self.next=None

class Stack:
  def __init__(self):
    self.head=None

  #isEmpty                                   #? time comp => O(1)  space comp => O(1)
  def isEmpty(self):           
    if self.head is None:
      return True
    else:
      return False

  #push                                     #? time comp => O(1)  space comp => O(1)
  def push(self,value):
      myNode=Node(value)
      myNode.next=self.head
      self.head=myNode
      return 'The element is added successfully'

  #pop                                        #? time comp => O(1)  space comp => O(1)
  def pop(self):  
    if self.isEmpty():
      return 'There is no element in the stack'
    else:
      popElem=self.head.value
      self.head=self.head.next
      return popElem

  #peek                                         #? time comp => O(1)  space comp => O(1)
  def peek(self):
    if self.head is None:
      return 'The stack is empty'
    else:
      return self.head.value


  #delete entire stack                          #? time comp => O(1)  space comp => O(1)
  def deleteStack(self):
    self.head=None

  #traverse the stack                           #? time comp => O(N)  space comp => O(1)
  def traversal(self):
    tempNode=self.head
    while(tempNode != None):
      print(tempNode.value)
      tempNode=tempNode.next

customStack=Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.traversal()
customStack.pop()
customStack.traversal()
