from enum import Enum
Numbers = Enum('Numbers', 'ONE TWO THREE FOUR FIVE')

def product(D, S):
  """
  :type D: integer [1..5]
  :type S: string ["one", "two", "three", "four", "five]
  :rtype: integer
  """
  return D * Numbers[S.upper()].value

print(product(2, "five"))

def battleship(N, S, T):
  """
  returns the number of sunken ships and hit ships as a string separated by one comma
  """
  pass

def get_land_area(land_map):
  pass

def get_largest_island_size(land_map, i, j, visited):
  pass