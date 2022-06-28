#Implementing 2 stacks in an array         #? space comp => O(N) where N is size of array
class twoStack:
  def __init__(self,size):
    self.size=size
    self.arr=[None]*size
    self.top1=-1
    self.top2=len(self.arr)

  def push1(self,value):              #? time comp => O(1)
    if (self.top1 + 1 != self.top2):
      self.top1+=1
      self.arr[self.top1]=value
      return 'Inserted successfully'
    else:
      return 'No space left in the array'

  def push2(self,value):            #? time comp => O(1)
    if (self.top1 + 1 != self.top2):
      self.top2-=1
      self.arr[self.top2]=value
      return 'Inserted successfully'
    else:
      return 'No space left in the array'

  def pop1(self):                   #? time comp => O(1)
    if self.top1 >=0:
      self.arr[self.top1]=None
      self.top-=1
      return "Deleted successfully"
    else:
      return "No element to delete from stack1"

  def pop2(self):                #? time comp => O(1)
    if self.top2<=self.size-1:
      self.arr[self.top2]=None
      self.top2+=1
      return "Deleted successfully"
    else:
      return "No element to delete from stack1"

  def traversal(self):
    if len(self.arr) > 0:
      for item in self.arr:
        print(item)
    else:
      print('No item in the array')


t=twoStack(5)
t.push1(1)
t.push1(2)
t.push2(100)
t.push2(200)
t.push2(500)
t.pop2()
t.traversal()
print(t.push1(3))
t.traversal()
print(t.push2(800))






