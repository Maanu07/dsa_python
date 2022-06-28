class Node:
  def __init__(self,value=None):
    self.value=value
    self.prev=None
    self.next=None

class CircularDoublyLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None

  #Create a circular DLL                     #? time comp => O(1)
  def createCDLL(self,value):
    node=Node(value)
    node.prev=node
    node.next=node
    self.head=node
    self.tail=node
    return 'You just added first node to CDLL'

   #Insert a node into circular DLL         #? time comp => O(1)
  def insert(self,value,location):
     if self.head is None:
       return 'There is no CDLL to add node'
     node=Node(value)
     if location == 0:
        node.next=self.head
        node.prev=self.tail
        self.head.prev=node
        self.head=node
        self.tail.next=node
     elif location == 1:
       node.prev=self.tail
       node.next=self.head
       self.tail.next=node
       self.head.prev=node
       self.tail=node
     else:
      index=0
      tempNode=self.head
      while(index < location - 1):
        tempNode=tempNode.next
        index+=1
      node.prev=tempNode
      node.next=tempNode.next
      tempNode.next.prev=node
      tempNode.next=node
     return 'Node inserted successfully'

  #Delete a node from a circular DLL        #? time comp => O(n)
  def delete(self,location):  
    if self.head is None:
      return 'There is no node to delete'
    if location == 0:
      if self.head == self.tail:
        self.head.next=None
        self.head.prev=None
        self.head=None
        self.tail=None
      else:
        self.head.next.prev=self.head.prev
        self.tail.next=self.head.next
        self.head=self.head.next
    elif location == 1:
        if self.head == self.tail:
          self.head.next=None
          self.head.prev=None
          self.head=None
          self.tail=None
        else:
          self.tail.prev.next=self.head
          self.head.prev=self.tail.prev
          self.tail=self.tail.prev
    else:
        index=0
        tempNode=self.head
        while(index < location - 1):
          tempNode=tempNode.next
          index+=1
        tempNode.next.next.prev=tempNode
        tempNode.next=tempNode.next.next
    return 'Node deleted successfully'

#Delete the entire circular DLL 
  def clearCDLL(self):
    tempNode=self.head
    while(tempNode):
      if(tempNode.next==self.tail.next):
        break
      tempNode.prev=None
      tempNode=tempNode.next
    self.head=None
    self.tail=None
    return 'The Cicular DLL has been cleared successfully'
    

#Search a node in Circular DLL          #? time comp => O(n)
  def search(self,value):
    if self.head is None:
      return 'There is no node to search '
    tempNode=self.head
    while(tempNode):
      if(tempNode.value == value):
        return 'The node exist in the CDLL'
      if(tempNode == self.tail):
        return 'The node does not exist in the CDLL'
      

  #Traversal of Circular DLL            #? time comp => O(n)
  def traverseCDLL(self):
    if self.head is None:
      return 'There is no node to traverse'
    tempNode=self.head
    while(tempNode):
      print(tempNode.value)
      if(tempNode==self.tail):
        break
      tempNode=tempNode.next

  #Reverse Traversal of Circular DLL            #? time comp => O(n)
  def reverseTraverseCDLL(self):
    if self.head is None:
      return 'There is no node to traverse'
    tempNode=self.tail
    while(tempNode):
      print(tempNode.value)
      if(tempNode==self.head):
        break
      tempNode=tempNode.prev

  

circularDLL=CircularDoublyLinkedList()
print(circularDLL.createCDLL(1))
print(circularDLL.insert(2,1))
print(circularDLL.insert(3,0))
print(circularDLL.insert(4,2))
circularDLL.traverseCDLL()
# print(circularDLL.delete(2))
# circularDLL.traverseCDLL()
print(circularDLL.clearCDLL())
print(circularDLL.traverseCDLL())
# print(circularDLL.search(8))



    