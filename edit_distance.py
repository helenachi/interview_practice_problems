import pprint
pp = pprint.PrettyPrinter(indent=4)

def min_ed(i, j):
  '''
  DP Approach
  @param i    index for source string x
  @param j    index for target string y
  @return     the edit distance from x[0..i] to y[0..j]
  '''
  if not x and not y:
    return 0
  elif not x and len(y) != 0:
    return len(y)
  elif len(x) != 0 and not y:
    return len(x)

  lookup_table = [[0 for _ in range(0, j + 1)] for _ in range(0, i + 1)] 
  # populate the 0th row and column padding
  for row in range(0, i+1):
    lookup_table[row][0] = row
  for col in range(0, j+1):
    lookup_table[0][col] = col

  # iterate through table
  for row in range(1, i+1):
    for col in range(1, j+1):
      sources = []
      sources.append(1 + lookup_table[row - 1][col])
      sources.append(1 + lookup_table[row][col - 1])
      sources.append(ham_dist(x[row-1], y[col-1]) + lookup_table[row - 1][col - 1])
      lookup_table[row][col] = min(sources)

  # pp.pprint(lookup_table)
  return lookup_table[i][j]


def ham_dist(a, b):
  '''
  @param a    source character
  @param b    target character
  @return     a == b
  '''
  return a != b


def min_ed_recursive(a, b):
  '''
  Recursive Approach
  @param x    source string
  @param y    target string
  @return     the edit distance from x to y
  '''
  if not a and not b:
    return 0
  elif not a and len(b) != 0:
    return len(b)
  elif len(a) != 0 and not b:
    return len(x)
  elif len(a) == 1 and len(b) == 1:
    return ham_dist(a, b)

  sources = []
  sources.append(1 + min_ed_recursive(a[:-1], b))
  sources.append(1 + min_ed_recursive(a, b[:-1]))
  sources.append(ham_dist(a[len(a)-1], b[len(b)-1]) + min_ed_recursive(a[:-1], b[:-1]))
  return min(sources)



x = input("Enter a string x: ")
y = input("Enter a string y: ")
print(min_ed(len(x), len(y)))
# print(min_ed_recursive(x, y))
# print(min_ed(len(x), len(y)) == min_ed_recursive(x, y))