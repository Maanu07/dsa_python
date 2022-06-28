#Binary Tree
#1.Creation of a binary tree
#2.Inserting a node 
#3.Deleting a node
#4.Traversing a node
#5.Search for a node in a tree
#6.Delete the entire tree


import myQueue as q

class TreeNode:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None 


root=TreeNode('Drinks')
cold=TreeNode('Cold')
hot=TreeNode('Hot')
tea = TreeNode('Tea')
coffe = TreeNode('Coffe')
root.left=cold 
root.right=hot
hot.left = tea 
cold.right = coffe 



def preorderTraversal(rootNode):
  if rootNode is None:
    return 
  print(rootNode.data)
  preorderTraversal(rootNode.left)
  preorderTraversal(rootNode.right)


def inorderTraversal(rootNode):
  if rootNode is None:
    return 
  inorderTraversal(rootNode.left)
  print(rootNode.data)
  inorderTraversal(rootNode.right)



def postorderTraversal(rootNode):
  if rootNode is None:
    return 
  postorderTraversal(rootNode.left)
  postorderTraversal(rootNode.right)
  print(rootNode.data)


def levelorderTraversal(rootNode):
  if rootNode is None:
    return 
  customQueue = q.Queue()
  customQueue.enqueue(rootNode)
  while(not customQueue.isEmpty()):
    root=customQueue.dequeue()
    print(root.data)
    if (root.left is not None):
      customQueue.enqueue(root.left)
    if (root.right is not None):
      customQueue.enqueue(root.right)
    
    

#we can use any of the four traversal methods to search a node in the tree but we prefer BFS or level order traversal for this because queue performs much better than stack
def searchBT(rootNode,nodeValue):
  if not rootNode:
    return 'There is no BT to search'
  else:
    customQueue = q.Queue()
    customQueue.enqueue(rootNode)
    while(not customQueue.isEmpty()):
      root = customQueue.dequeue()
      if(root.data == nodeValue):
        return 'Node is present in the BT'
      if root.left is not None:
         customQueue.enqueue(root.left)
      if root.right is not None:
        customQueue.enqueue(root.right)
    else:
      return 'Node does not exist in the BT'


#insert node into Binary Tree
def insertBT(rootNode,nodeValue):
  if not rootNode:
    rootNode = TreeNode(nodeValue)
  else:
    customQueue = q.Queue()
    customQueue.enqueue(rootNode)
    while(not customQueue.isEmpty()):
     root = customQueue.dequeue()
     if(root.left is None):
       root.left = TreeNode(nodeValue)
       return 'Added successfully'
     elif root.left is not None:
        customQueue.enqueue(root.left)
     if (root.right is None):
      root.right = TreeNode(nodeValue)
      return 'Added successfully'
     elif root.right is not None:
        customQueue.enqueue(root.right)

# get deepest node from Binary Tree
def getDeepestNode(rootNode):
  if rootNode is None:
    return 
  else:
    customQueue = q.Queue()
    customQueue.enqueue(rootNode)
    while(not customQueue.isEmpty()):
      root = customQueue.dequeue()
      if root.left is not None:
        customQueue.enqueue(root.left)
      if root.right is not None:
        customQueue.enqueue(root.right)
    return root

#delete deepest node from Binary Tree
def deleteDeepestNode(rootNode,deepestNode):
  if rootNode is None:
    return 
  else:
    customQueue = q.Queue()
    customQueue.enqueue(rootNode)
    while(not customQueue.isEmpty()):
      root = customQueue.dequeue()
      if root == deepestNode:
        root = None 
        return 
      else:
        if root.right == deepestNode:
          root.right = None
          return 
        else:
          customQueue.enqueue(root.right)
        if root.left == deepestNode:
          root.left =None
          return
        else:
          customQueue.enqueue(root.left)
      
# delete a node from Binary Tree
def deleteNodeBT(rootNode,value):
  if rootNode is None:
    return 
  else:
    customQueue = q.Queue()
    customQueue.enqueue(rootNode)
    while(not customQueue.isEmpty()):
      root = customQueue.dequeue()
      if root.data == value:
        dNode = getDeepestNode(rootNode)
        root.data = dNode.data
        deleteDeepestNode(rootNode,dNode)
        return 'Deleted Successfully'
      else:
        if root.left is not None:
          customQueue.enqueue(root.left)
        if root.right is not None:
          customQueue.enqueue(root.right)

    return 'Failed to delete node'
      
      
 #delete entire Binary Tree     
def deleteBT(rootNode):
  if rootNode is None:
    return 
  else:
   rootNode.data = None
   rootNode.left =None
   rootNode.right = None

    





      
  
 
""" preorderTraversal(root)
print('--------------------')
inorderTraversal(root)
print('--------------------')
postorderTraversal(root)
print('--------------------')
levelorderTraversal(root) """
# print(searchBT(root,'Drinks'))
# print(insertBT(root,'Cola'))
levelorderTraversal(root)
print('--------------------')
# dNode = getDeepestNode(root)
# deleteNodeBT(root,'Hot')
deleteBT(root)
levelorderTraversal(root)