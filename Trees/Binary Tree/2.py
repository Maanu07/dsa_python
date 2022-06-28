# creating Binary Tree using python list



class BinaryTree:
  def __init__(self,size):
    self.customList = [None] * size 
    self.lastUsedIndex = 0
    self.maxSize = size 

  #insert into Binary Tree
  def insert(self,value):
    if self.lastUsedIndex + 1 == self.maxSize:
      return 'BT is full'
    else:
      self.customList[self.lastUsedIndex + 1] = value 
      self.lastUsedIndex +=1 
      return 'Node successfully added to BT'

  #search in a BT 
  def search(self,value):
    if self.lastUsedIndex == 0:
      return 'No node in the BT to search'
    else:
      for i in range(1,self.maxSize):
        if self.customList[i] == value:
          return 'Value exist in BT'
      return 'Not found'

  #pre-order traversal of BT 
  def preorderTraversal(self,index):
    if index > self.lastUsedIndex:
      return 
    print(self.customList[index])
    self.preorderTraversal(index * 2)
    self.preorderTraversal(index * 2 + 1)

  #in-order traversal of BT
  def inorderTraversal(self,index):
     if index > self.lastUsedIndex:
       return 
     self.inorderTraversal(index * 2)
     print(self.customList[index])
     self.inorderTraversal(index * 2 + 1)

  #post-order traversal of BT
  def postorderTraversal(self,index):
     if index > self.lastUsedIndex:
       return 
     self.postorderTraversal(index * 2)
     self.postorderTraversal(index * 2 + 1)
     print(self.customList[index])


  #level order traversal in BT
  def levelorderTraversal(self,index):
    for i in range(index,self.lastUsedIndex + 1):
          print(self.customList[i])
     

  #delete a node in a BT
  def deleteNodeBT(self,value):
    for i in range(1,self.lastUsedIndex + 1):
      if self.customList[i] == value:
        self.customList[i]= self.customList[self.lastUsedIndex] 
        self.customList[self.lastUsedIndex]= None
        self.lastUsedIndex -= 1
        return 'Deleted'

  #delete the entire BT
  def deleteBT(self):
    self.customList=None
    return 'BT Deleted'

      




newBT = BinaryTree(8)
print(newBT.insert('Drinks'))
print(newBT.insert('Hot'))
print(newBT.insert('Cold'))
print(newBT.insert('Tea'))
print(newBT.insert('Coffe'))
newBT.preorderTraversal(1)
print('---------------------------')
newBT.inorderTraversal(1)
print('---------------------------')
newBT.postorderTraversal(1)
print('---------------------------')
newBT.levelorderTraversal(1)
print(newBT.deleteNodeBT('Hot'))
print('---------------------------')
newBT.levelorderTraversal(1)
# print(newBT.search('Mocha'))






