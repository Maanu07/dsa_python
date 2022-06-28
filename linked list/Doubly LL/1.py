#DOUBLY LINKED LIST

class Node:
  def __init__(self,value=None):
    self.prev=None
    self.next=None
    self.value=value

class DoublyLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None

  #Create a doubly LL                                 #? time comp => O(1)
  def createDLL(self,value):
    node=Node(value)
    node.prev=None
    node.next=None
    self.head=node
    self.tail=node
    return 'The DLL has been created successfully'

  #Insert a new node into DLL                        #? time comp => O(n)
  def insertInDLL(self,value,location):
    if self.head is None:
      return 'DLL has no node in it'
    else:
      node=Node(value)
      if location ==0:
        node.prev=None
        node.next=self.head
        self.head.prev=node
        self.head=node
      elif location ==1:
        node.next=None
        self.tail.next=node
        node.prev=self.tail
        self.tail=node
      else:
        index=0
        tempNode=self.head
        while(index < location - 1):
          tempNode=tempNode.next
          index+=1
        nextNode=tempNode.next
        tempNode.next=node
        node.prev=tempNode
        node.next=nextNode
        nextNode.prev=node
      return 'Node added successfully'

  # Travserse the DLL                              #? time comp => O(n)
  def traverseDLL(self):
    if self.head is None:
      print('We cannot traverse the empty DLL')
    else:
      tempNode=self.head
      while(tempNode is not None):
        print(tempNode.value)
        tempNode=tempNode.next

  # Reverse Travsersal of  the DLL                #? time comp => O(n)
  def reverseTraverseDLL(self): 
    if self.head is None:
      print('We cannot traverse the empty DLL')
    else:
      tempNode=self.tail
      while(tempNode):
        print(tempNode.value)
        tempNode=tempNode.prev

  #Search for a node in DLL                       #? time comp => O(n)
  def serachInDLL(self,value):
    tempNode=self.head
    while(tempNode != None):
      if(tempNode.value == value):
        return 'Node exist in the DLL'
      tempNode=tempNode.next
    return 'Node does not exist in the DLL'

   #Delete a node from DLL                         #? time comp => O(n)
  def deleteNode(self,location):
     if self.head is None:
       return 'There is no node to delete in DLL'
     else:
       if location == 0:
         if self.head == self.tail:
           self.head=None
           self.tail=None
         else:
          self.head=self.head.next
          self.head.prev=None
       elif location == 1:
          if self.head == self.tail:
           self.head=None
           self.tail=None
          else:
            secondLastNode=self.tail.prev
            secondLastNode.next=None
            self.tail=secondLastNode
       else:
         index=0
         tempNode=self.head
         while(index < location - 1):
           tempNode=tempNode.next
           index+=1
         tempNode.next=tempNode.next.next
         tempNode.next.prev=tempNode

       return 'Node deleted successfully'


   #Delete the entire DLL                         #? time comp => O(n)
  def deleteDLL(self):  
    if self.head is None:
      return 'There are no nodes to delete in DLL'
    else:
      tempNode=self.head.next   #we are starting from second node because first node "prev" pointer already points to null
      while(tempNode):
        tempNode.prev=None
        tempNode=tempNode.next
      self.head=None
      self.tail=None
      return 'All nodes deleted successfully'


  #reverse the doubly linked list 
  #? Method 1 => using a stack  and then updating linked list data values ( time comp => O(N)  space comp => O(N))
  #? Method 2 => swapping the prev and next pointer of each node and changing head reference at the end (time => O(N)  space => O(1))

  def reverseDLL(self):
    curr=self.head
    temp=None
    while(curr!=None):
      temp=curr.prev
      curr.prev=curr.next
      curr.next=temp
      curr=curr.prev
    
    if temp is not None:
      self.head=temp.prev

    # return head

    




doublyLL=DoublyLinkedList()
print(doublyLL.createDLL(1))
print(doublyLL.insertInDLL(2,1))
print(doublyLL.insertInDLL(3,0))
print(doublyLL.insertInDLL(4,1))
print(doublyLL.insertInDLL(5,2))
doublyLL.traverseDLL()
# doublyLL.reverseDLL()
# doublyLL.traverseDLL()

# print(doublyLL.serachInDLL(8))
# doublyLL.reverseTraverseDLL()
# print(doublyLL.deleteNode(0))
# print(doublyLL.deleteDLL())
# doublyLL.traverseDLL()

