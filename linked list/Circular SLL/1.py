#CIRCULAR SINGLY LINKED LIST



from typing import NoReturn


class Node:
  def __init__(self,value=None):
    self.value=value
    self.next=None

class CircularSLL:
  def __init__(self):
      self.head=None
      self.tail=None

  # Create a circular SLL
  def create(self,value):
    node=Node(value)
    node.next=node
    self.head=node
    self.tail=node
    print('The CSLL has been created')

  # Insert  into circular SLL                      #? time comp => O(n)
  def insert(self,value,location):
    if(self.head is None):
        print('The Circular SLL does not exist')  
    else:
        newNode=Node(value)
        if location==0:
          newNode.next=self.head
          self.head=newNode
          self.tail.next=self.head
        elif location == 1:
          self.tail.next=newNode
          self.tail=newNode
          newNode.next=self.head
        else:
          index=0
          tempNode=self.head
          while(index < location-1):
            tempNode=tempNode.next
            index+=1
          nextNode=tempNode.next
          tempNode.next=newNode
          newNode.next=nextNode
        return 'The node has been successfully inserted'

  # Traversing the Circular SLL                #? time comp => O(n)
  def traversal(self):
    if self.head is None:
      print('No Circular SLL exist')
    else:
      tempNode=self.head
      while(tempNode):
        print(tempNode.value)
        tempNode=tempNode.next
        if(tempNode==self.tail.next):
          break
      
  # Searching for a node in circular SLL      #? time comp => O(n)
  def search(self,value):
    if self.head is None:
      print('No Circular SLL exist')
    else:
      tempNode=self.head
      while(tempNode):
       if(tempNode.value == value):
         print('Value exist in the cicular SLL')
         break
       tempNode=tempNode.next
       if(tempNode==self.tail.next):
         print('Value does not exist in the circular SLL')
         break
    
  # Delete a node from a cicular SLL        #? time comp => O(n)
  def delete(self,location):
    if self.head is None:
         print('No Circular SLL exist')
    else:
      if location == 0:
        if(self.head == self.tail):
          self.head.next=None
          self.head=None
          self.tail=None
        else:
          self.head=self.head.next
          self.tail.next=self.head
      elif location == 1:
        if(self.head==self.tail):
          self.head.next=None
          self.head=None
          self.tail=None
        else:
          tempNode=self.head
          while(tempNode.next!=self.tail):
            tempNode=tempNode.next
          tempNode.next=self.head
          self.tail=tempNode
      else:
         index=0
         tempNode=self.head
         while(index < location - 1):
           tempNode=tempNode.next
           index+=1
         nextNode=tempNode.next
         tempNode.next=nextNode.next

  # Delete the entire Cicular SLL     #? time comp => O(1)
  def clear(self):
    if self.head is None:
      print('No Circular SLL exist')
    else:
      self.tail.next=None
      self.tail=None
      self.head=None

CircularSinglyLinkedList=CircularSLL()
CircularSinglyLinkedList.create(50)
CircularSinglyLinkedList.insert(100,0)
CircularSinglyLinkedList.insert(200,0)
CircularSinglyLinkedList.insert(300,1)
CircularSinglyLinkedList.insert(400,1)
CircularSinglyLinkedList.insert(500,2)
CircularSinglyLinkedList.traversal()
CircularSinglyLinkedList.search(800)
CircularSinglyLinkedList.delete(3)
CircularSinglyLinkedList.traversal()
CircularSinglyLinkedList.clear()
CircularSinglyLinkedList.traversal()
