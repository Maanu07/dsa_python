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