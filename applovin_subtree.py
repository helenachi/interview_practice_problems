class Node:
  def __init__(self, key=None, left=None, right=None):
    self.key = key
    self.left = left
    self.right = right

def isSubtree(main, sub):
  if main is None:
    return (sub is None)
  elif sub is None:
    return True
  elif main.key == sub.key:
    return isSame(main, sub)
  else:
    return isSubtree(main.left, sub) or isSubtree(main.right, sub)

def isSame(a, b):
  if a is None:
    return (b is None)
  elif b is None:
    return True
  elif a.key != b.key:
    return False
  else:
    return isSame(a.left, b.left) and isSame(a.right, b.right)

if __name__ == '__main__':
  m = Node(1)
  m.left = Node(2)
  m.right = Node(3)
  m.left.right = Node(4)
  m.right.left = Node(5)
  m.right.right = Node(6)
  m.right.left.left = Node(7)
  m.right.left.right = Node(8)

  s = None
  # s = Node(3)
  # s.left = Node(5)
  # s.right = Node(6)
  print(isSubtree(m, s))