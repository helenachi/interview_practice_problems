# Find LCA for BST
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if root is None:
      return None
    p_parents = self.find_path(root, p)
    q_parents = self.find_path(root, q)
    
    if not p_parents or not q_parents:
      return None
    
    for i in range( len(p_parents) - 1, -1, -1):
      if p_parents[i] in q_parents:
        return p_parents[i]
    
    return root

  
  def find_path(self, root, target):
      """
      :type root: TreeNode
      :type target: TreeNode
      :rtype: list[TreeNode.val]
      """
      result = []
      if root.val:
        result.append(root)
      if target.val == root.val:
        return result
      elif target.val < root.val:
        result.extend(self.find_path(root.left, target))
      else:
        result.extend(self.find_path(root.right, target))
      
      return result
      

      