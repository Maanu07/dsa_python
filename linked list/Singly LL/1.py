#LINKED LIST


class Node:
  def __init__(self,value=None):
    self.value=value
    self.next=None

class SLinkedList:
  def __init__(self):
      self.head=None
      self.tail=None

# insert into single linked list            #? time comp => O(n)
  def insertion(self,value,location):
   newNode=Node(value)
   if(self.head is None):
     self.head=newNode
     self.tail=newNode
   else:
    if (location==0):
      newNode.next=self.head
      self.head=newNode
    elif (location==1):
      newNode.next=None #optional because you already assigned next of new node to None
      self.tail.next=newNode
      self.tail=newNode
    else:
      tempNode=self.head
      index=1
      while(index < location):
        tempNode=tempNode.next
        index+=1
      nextNode=tempNode.next
      tempNode.next=newNode
      newNode.next=nextNode

# traversing the single linked list    #? time comp => O(n)
  def traversal(self):
    if self.head is None:
        print('Single Linked List does not exist!!')
    else:
        currentNode=self.head
        while(currentNode is not None):
          print(currentNode.value)
          currentNode=currentNode.next

  # Search for a node in a single linked list      #? time comp => O(n)
  def searchSLL(self,value):
    if self.head is None:
        return('Single Linked List does not exist')
    else:
        currentNode=self.head
        while(currentNode is not None):
          if(currentNode.value ==value):
            return True
          currentNode=currentNode.next
        return False

  # Delete a node from a single linked list         #? time comp => O(n)
  def deleteNode(self,location):
    if self.head is None:
        return('Single Linked List does not exist')
    else:
      if(location == 0):
        if(self.head==self.tail):
          self.head=None
          self.tail=None
        else:
          self.head=self.head.next
      elif (location==1):
        if(self.head==self.tail):
          self.head=None
          self.tail=None
        else:
          node=self.head
          while(node is not  None):
            if(node.next == self.tail):
              break
            node=node.next
          node.next=None
          self.tail=node    
      else:
        node=self.head
        index=0
        while(index<location-1):
          node=node.next
          index+=1
        nextNode=node.next
        node.next=nextNode.next


  # Delete the entire Singly Linked List     #? time comp => O(1)
  def deleteEntireSLL(self):
      if self.head is None:
        print('The Linked List does not exist')
      else:
        self.head=None
        self.tail=None


  # Reverse a singly linked list        #? time comp => O(n)
  def reverseSLL(self):
    if self.head is None:
       print('The Linked List does not exist')
    else:
      current=self.head
      prev=None
      next=None
      while(current is not None):
        next=current.next
        current.next=prev
        prev=current
        current=next
      (self.head,self.tail)=(self.tail,self.head)

singlyLinkedList=SLinkedList()
singlyLinkedList.insertion(100,1)
singlyLinkedList.insertion(200,1)
singlyLinkedList.insertion(300,1)
singlyLinkedList.insertion(400,0)
singlyLinkedList.insertion(500,2)
singlyLinkedList.traversal()
singlyLinkedList.reverseSLL()
print('---------------------')
singlyLinkedList.traversal()
# print(singlyLinkedList.searchSLL(800))
# singlyLinkedList.deleteNode(3)
# singlyLinkedList.deleteEntireSLL()
# singlyLinkedList.traversal()




