#Implementing queue with the help of python list (with no size limit)

class Queue:
  def __init__(self):
    self.items=[]

  def __str__(self):
    values=[str(x) for x in self.items]
    return ' '.join(values)

  #isEmpty                               #? time comp => O(1)
  def isEmpty(self):
    if self.items == [] or len(self.items) == 0:
      return True
    else:
      return False

  #enqueue                             #? time comp => O(n)
  def enqueue(self,value):
    self.items.append(value)
    return 'The element is inserted to the end of queue'

  #dequeue                             #? time comp => O(n)
  def dequeue(self):
    if self.isEmpty():
      return 'The queue is empty'
    else:
      return self.items.pop(0)

  #peek                               #? time comp => O(1)
  def peek(self):
    if self.isEmpty():
      return 'The queue is empty'
    else:
      return self.items[0]

  #delete queue                      #? time comp => O(1)
  def delete(self): 
    self.items=None
    return 'Queue deleted successfully'


myQueue=Queue()
print(myQueue.isEmpty())
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print(myQueue.peek())
print(myQueue.dequeue())
print(myQueue.delete())
# print(myQueue)



