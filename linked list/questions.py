class Node:
  def __init__(self,value=None):
    self.data=value
    self.next=None

class SLL:
  def __init__(self):
    self.head=None
    self.tail=None

  #inserting into linked list
  def insert(self,value,pos):
    newNode=Node(value)
    if self.head == None:
      self.head=newNode
      self.tail=newNode
    else:
      #inserting at the beginning
      if pos ==0:
        newNode.next=self.head
        self.head=newNode
      #inserting at the end
      elif pos ==1:
        self.tail.next=newNode
        self.tail=newNode
      #inserting in between
      else:
        tempNode=self.head
        index=1
        while(index<pos):
          tempNode=tempNode.next
          index+=1
        newNode.next=tempNode.next
        tempNode.next=newNode
    return 'Node inserted successfully'

  #deleting node from a linked list
  def delete(self,pos):
    if self.head is None:
      return 'There is no node to delete'
    else:
      if pos==0:
        if self.head == self.tail:
          self.head=None
          self.tail=None
        else:
          self.head=self.head.next
      elif pos==1:
        if self.head==self.tail:
          self.head=None
          self.tail=None
        else:
          tempNode=self.head
          while(tempNode.next!=self.tail):
            tempNode=tempNode.next
          tempNode.next=None
          self.tail=tempNode
      else:
          tempNode=self.head
          index=1
          while(index < pos-1):
            tempNode=tempNode.next
            index+=1
          tempNode.next=tempNode.next.next
      return 'Node deleted successfully'

  #traversing the linked list
  def traverse(self):
      if self.head is None:
        return 'No nodes to traverse'
      tempNode=self.head
      while(tempNode!=None):
        print(tempNode.data)
        tempNode=tempNode.next

  #reverse the linked list
  def reverse(self,head):
      curr=head
      next=prev=None
      while(curr!=None):
        next=curr.next
        curr.next=prev 
        prev=curr
        curr=next
      return prev

  #Find the middle of a given linked list       #? time comp => O(N/2)
  def middle(self):
    slowPtr=fastPtr=self.head
    while(fastPtr.next!=None and fastPtr.next.next!=None):
      slowPtr=slowPtr.next
      fastPtr=fastPtr.next
    return slowPtr.data

  #check if linked list is palindrome or not   #? time comp => O(N/2 + N/2 + N/2)  space comp => O(1)
  def checkForPalindrome(self):
    #check if there is only one node 
    if self.head == None or self.head==self.tail:
      return True
    #step 1 => get the mid node
    slowPtr=fastPtr=self.head
    while(fastPtr.next!=None and fastPtr.next.next!=None):
      slowPtr=slowPtr.next
      fastPtr=fastPtr.next
    #step 2 => reverse the second half of linked list
    slowPtr.next=self.reverse(slowPtr.next)
    slowPtr=slowPtr.next
    #step 3 => compare 
    tempNode=self.head
    while(slowPtr!=None):
      if tempNode.data != slowPtr.data:
        return False
      slowPtr=slowPtr.next
      tempNode=tempNode.next
    return True

  #Remove duplicates from a unsorted linked list
  #Method 1 => using a temporary buffer  #? space comp => O(N)  time comp => O(N)
  """ def removeDuplicates(self):
      tempNode=self.head
      #add first node to the set
      visited=set([tempNode.data])
      while(tempNode.next is not None):
          #if node already present in the list 
          if tempNode.next.data in visited:
              tempNode.next=tempNode.next.next
          #if node is not in the list
          else:
              tempNode=tempNode.next
              visited.append(tempNode.data)
      print('duplicates removed') """

  #Method 2 => without using a temporary buffer  #? space comp => O(1)  time comp => O(N*N)
  def removeDuplicates(self):
        if self.head is None:
            return 'There is no node in the linked list'
        else:
            curr=self.head
            while(curr.next is not None):
                runner=curr
                while(runner.next is not None):
                    if runner.next.data == curr.data:
                        runner.next=runner.next.next
                    else:
                        runner=runner.next
                curr=curr.next
            print('Duplicates removed')

  #Print nth node from the end of linked list     #? time comp = O(N)  space comp => O(1)
  def printNthNode(self,n):
      #step 1 => get the lenght of linked list
      curr=self.head
      length=0
      while(curr is not None):
        length+=1
        curr=curr.next
      beg=length-n
      index=1
      curr=self.head
      while(index < beg):
          curr=curr.next
          index+=1
      return curr.next.data
      


#creating singly linked list with no node
singlyLL=SLL()
print(singlyLL.insert(100,1))
print(singlyLL.insert(200,1))
print(singlyLL.insert(300,1))
print(singlyLL.insert(400,1))
print(singlyLL.insert(200,1))
print(singlyLL.insert(300,1))
singlyLL.traverse()
print(singlyLL.printNthNode(3))
# singlyLL.removeDuplicates()
# singlyLL.traverse()




#Reverse a linked list
# 1 method => Iterative method (We use 3 pointers approach)
""" def reverse(self):
  curr=self.head
  next=prev=None
  while(curr!=None):
    next=curr.next
    curr.next=prev 
    prev=curr
    curr=next
  return prev """

#Method 2 => using recursion
""" def reverse(head,curr,next,prev):
  if curr!=None:
    next=curr.next
    prev=curr
    curr=next
    return reverse(head,curr,next,prev)
  else:
    return prev

self.head=reverse(head,head,None,None) """





#Rerversing a linked list in batches of k or Reverse a Linked List in group of given size 
#Input => 1 => 2 => 3 => 4 => 5 => 6 => 7 => 8 => Null  k=3   head=1
#Output=> 3 => 2 => 1 => 6 => 5 => 4 => 8 => 7 => Null  and head=3
""" def reverse(self,h,k):
  curr=h
  next=prev=None
  count=1
  while(curr is not None and count <= k):
    next=curr.next
    curr.next=prev
    prev=curr
    curr=next
    count+=1
  if next != None:
    h.next=reverse(next,k)
  return prev
 """




    

    