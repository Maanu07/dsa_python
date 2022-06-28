#check whethter 2BT are identical or not 

class TreeNode:
  def __init__(self,value):
      self.val  = value 
      self.left = None
      self.right = None 


def isIdentical(b1,b2):
  if b1 is None and b2 is None:
    return 
  if b1 is not None and b2 is not None and b1.val == b2.val:
    isIdentical(b1.left,b2.left)
    isIdentical(b1.right,b2.right)
    
  else:
    return False

#creating first tree
BT1= TreeNode(10)
BT1.left = TreeNode(11)
BT1.right = TreeNode(12)
BT1.right.right = TreeNode(13)

#creating second tree
BT2= TreeNode(10)
BT2.left = TreeNode(11)
BT2.right = TreeNode(12)

print(isIdentical(BT1,BT2))



# Program to check whether a tree is a full binary tree or not 

""" def checkForFullBTree(root):
    #tree is empty
    if root is None:
        return True
    #check its child 
    if root.left is None and root.right is None:
        return True 
    if root.left is not None and root.right is not None:
        return checkForFullBTree(root.left) and checkForFullBTree(root.right)
    return False 
        
root = TreeNode(10)
root.left = TreeNode(11)
root.right = TreeNode(12)
root.left.left = TreeNode(13)

print(checkForFullBTree(root)) """
