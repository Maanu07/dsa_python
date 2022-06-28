# BST is a binary search tree, BST is faster than binary tree for operations like insertion , deletion , searching etc...


import myQueue as q 

class BSTNode:
  def __init__(self,data):
    self.data = data 
    self.leftChild= None 
    self.rightChild = None 


# insert a node into bst       time comp => O(logn)  & space comp => O(logn)    where n= no. of nodes in BST
def insert(root,val):
  if root.data == None:
    root.data = val  
  elif root.data > val:
    if root.leftChild is None:
      root.leftChild = BSTNode(val)
    else:
      insert(root.leftChild,val)
  else:
    if root.rightChild is None:
      root.rightChild= BSTNode(val)
    else:
      insert(root.rightChild,val)
  return 'Node Added'

# for any traversal in binary tree the time amd space comp is both O(n)
def preOrder(rootNode):
  if rootNode == None:
    return 'No BST to traverse'
  else:
    print(rootNode.data)
    preOrder(rootNode.leftChild)
    preOrder(rootNode.rightChild)


def inOrder(rootNode):
  if rootNode == None:
      return 'No BST to traverse'
  else:
    inOrder(rootNode.leftChild)
    print(rootNode.data)
    inOrder(rootNode.rightChild)


def postOrder(rootNode):
  if rootNode is None:
    return 
  else:
    postOrder(rootNode.leftChild)
    postOrder(rootNode.rightChild)
    print(rootNode.data)
  

def levelOrder(rootNode):
  if rootNode is None:
    return 'No BST to traverse '
  else:
     customQueue =  q.Queue()
     customQueue.enqueue(rootNode)
     while(not customQueue.isEmpty()):
       root = customQueue.dequeue()
       print(root.data) 
       if root.leftChild is not None:
         customQueue.enqueue(root.leftChild)
       if root.rightChild is not None:
         customQueue.enqueue(root.rightChild)

# search for a node in bst      time comp => o(logn)   space comp =< log(n)
def searchNode(rootNode,nodeValue):
  if rootNode is None:
    return 
  else:
    if rootNode.data ==  nodeValue:
      return 'Found'
    elif rootNode.data > nodeValue:
      return searchNode(rootNode.leftChild, nodeValue)
    else:
      return searchNode(rootNode.rightChild, nodeValue)
      

def smallestNode(rootNode):
  current = rootNode.rightChild 
  while(current.leftChild is not None):
        current = current.leftChild
  return current 



def deleteNode(rootNode,nodeValue):
  if rootNode is None:
    return 
  elif 


      

newTree = BSTNode(70)
insert(newTree,50)
insert(newTree,90)
insert(newTree,30)
insert(newTree,60)
insert(newTree,80)
insert(newTree,100)
insert(newTree,20)
insert(newTree,40)

