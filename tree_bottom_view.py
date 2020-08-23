class Node:
  def __init__(self, key=None, left=None, right=None):
    self.key = key
    self.left = left
    self.right = right
  
def bottomViewUtil(root, hdist, level, dict):
  if root is None:
    return
  if hdist not in dict or level >= dict[hdist][1]:
    dict[hdist] = (root.key, level)
  bottomViewUtil(root.left, hdist - 1, level + 1, dict)
  bottomViewUtil(root.right, hdist + 1, level + 1, dict)

def printBottomView(root):
  dict = {}
  bottomViewUtil(root, 0, 0, dict)
  for key in sorted(dict.keys()):
    print(dict.get(key)[0], end=' ')
  print()

if __name__ == '__main__':
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.right = Node(4)
  root.right.left = Node(5)
  root.right.right = Node(6)
  root.right.left.left = Node(7)
  root.right.left.right = Node(8)
  printBottomView(root)


'''
time complexity: O(n log(n))
space complexity: O(n)
'''