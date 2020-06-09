import pprint
pp = pprint.PrettyPrinter(indent=4)


"""
  This file shows two different approaches to the minimum Edit Distance (MED) problem:
  recursion and dynamic programming (DP).

  As a quick little overview...
    DP problems are often able to be solved recursively, but the running time is much 
    smaller than recursive solutions and therefore more efficient.
    This is due to a multitude of factors, such as a DP lookup table's dimensions, and 
    how problems are reduced to its base cases differently based on their approach.

  We start with the base cases:
    x is empty string, y is empty string  --> ED = 0      (match)
    x is empty string, y is not           --> ED = len(y) (insertion)
    x is not empty string, y is           --> ED = len(x) (deletion)
    x is string length 1, y is too        --> ED = hamming_distance(x, y) (match/substitution),
  where the hamming distance in this situation is 1 if x != y.

  We first determine a recursive strategy to solve this problem:
    The result is based on the smallest MED between all the combinations of prefixes 
    of a source string x and a target string y.
    min_ed_recursive(x, y) = min( 1 + min_ed_recursive(x[:-1], y)                                         # insertion/delete 
                                  1 + min_ed_recursive(x, y[:-1]),                                        # insertion/delete
                                  ham_dist(x[len(x)-1], y[len(y)-1] + min_ed_recursive(x[:-1], y[:-1]))   # match/substitution )
    (x[:-1], y), (x, y[:-1]), and (x[:-1], y[:-1]) represents all the possible combination of smaller prefixes.

  Now we can analyze our recursive solution to see how we can build a lookup table for
    the DP approach. Let's make the table size m*n, where m = len(x) and n = len(y).
  From here, the intuition is that we need to fill out the table from the uppermost, leftmost 
    corner -- so both being prefixes of length 1. Therefore, the answer we're looking for, 
    which would be the value at lookup_table[len(x)-1][len(y)-1], the values of the cells above, 
    to the left of, and to the upper left of it.
  
  With this understanding, we can write code that iterates through a double array of size m*n with 
    a nested for loop, and initialize the 0th row and columns with base case values. Then, we can 
    populate the table's values in order and finally reach the desired answer, the last cell to be 
    filled.
"""


def ham_dist(a, b):
  '''
  @param a    source character
  @param b    target character
  @return     a == b
  '''
  return a != b


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
  pp.pprint(lookup_table)
  return lookup_table[i][j]


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