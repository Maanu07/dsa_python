#Impelementing queue using python list (with size restriction)
#Linear queue vs Circular queue 


class Queue:
  def __init__(self,size):            #? time comp => O(1) and space comp => O(size/N)
    self.size=size
    self.items=[None] * self.size
    self.front=-1
    self.rear=-1

  def __str__(self):
    values=[str(x) for x in self.items]
    return ' '.join(values)

  #isEmpty                           #? space comp => O(1) and time comp => O(1)
  def isEmpty(self):
    if self.front == -1:
      return True
    else:
      return False

  #isFull                            #? space comp => O(1) and time comp => O(1)
  def isFull(self):
    if self.front==0 and self.rear==self.size-1 or self.rear==self.front - 1:
      return True
    else:
      return False
    
  #enqueue                           #? space comp => O(1) and time comp => O(1)
  def enqueue(self,value):
    if self.isFull():
      return 'The queue is fulled'
      #inserting the first element into queue
    elif self.isEmpty():
      self.front=0
      self.rear=0
      #when the rear points to last index 
    elif self.rear==self.size - 1:
      self.rear=0
    else:
      self.rear+=1
    self.items[self.rear]=value

  #dequeue                          #? space comp => O(1) and time comp => O(1)
  def dequeue(self):
    if self.isEmpty():
      return 'The queue is empty'
    else:
      deletedElem=self.items[self.front]
      front=self.front
      #if there exist only single item in queue
      if self.front == self.rear:
        self.front=-1
        self.rear=-1
      #if we are deleting first element from the right of queue
      elif self.front == self.size - 1:
        self.front=0
      else:
        self.front+=1
      self.items[front]=None
      return deletedElem

  #peek                              #? space comp => O(1) and time comp => O(1)
  def peek(self):
    return self.items[self.front]
  
  #delete queue                     #? space comp => O(1) and time comp => O(1)
  def delete(self):
    self.items=[None]*self.size
    self.rear=self.front=-1
    

myQueue=Queue(5)
print(myQueue.isEmpty())
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
myQueue.enqueue(6)
print(myQueue)
print(myQueue.isFull())