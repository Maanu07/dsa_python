#Queue implementation with the help of linked list

class Node:
  def __init__(self,value=None):
    self.value=value
    self.next=None

class Queue:
  def __init__(self):                          #? time comp => O(1) & space comp => O(1)
    self.head=self.tail=None

  #isEmpty                                      #? time comp => O(1) & space comp => O(1)
  def isEmpty(self):
    if self.head == None:
      return True
    else:
      return False

  #enqeue operation                               #? time comp => O(1) & space comp => O(1)
  def enqueue(self,value): 
    temp=Node(value)
    if self.head==None:
      self.head=self.tail=temp
    else:
      self.tail.next=temp
      self.tail=temp
    return 'Item added successfully to the queue'
  
  #dequeue operation                          #? time comp => O(1) & space comp => O(1)
  def dequeue(self):
    if self.head == None:
      return 'The queue is empty'
    else:
      deletedVal=self.head.value
      if self.head == self.tail:
        self.head = self.tail = None
      else:
        self.head=self.head.next
    return deletedVal

  #peek                                    #? time comp => O(1) & space comp => O(1)
  def peek(self):
    if self.head == None:
      return 'The queue is empty'
    else:
      return self.head.value

  #delete queue                         #? time comp => O(1) & space comp => O(1)
  def delete(self):
    self.head=self.tail=None

  def traversal(self):                #? time comp => O(N) & space comp => O(1)
    temp=self.head
    while(temp):
      print(temp.value,end=' ')
      temp=temp.next


""" myQueue=Queue()
print(myQueue.isEmpty())
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
# myQueue.dequeue()
# myQueue.dequeue()
print(myQueue.peek())
myQueue.traversal() """


