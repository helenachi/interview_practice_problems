import unittest

def totalStringValues(arr):
  """
  :type arr: list of str
  :rtype: int
  """
  # raise ValueError
  # arr=[]
  total_sum = 0
  for s in arr:
    if s == "":
      continue
    else:
      total_sum += int(s)
  
  return total_sum

class Test(unittest.TestCase):
  def test_given_first(self):
    assert totalStringValues(["4", "6", "10", "", "0", "5"]) == 25, "Should be 25"

  def test_given_second(self):
    assert totalStringValues(["", "4", "", ""]) == 4, "Should be 4"

  def test_given_third(self):
    assert totalStringValues(["", ""]) == 0, "Should be 0"

  def test_negative_single(self):
    assert totalStringValues(["-3000"]) == -3000, "Should be -3000"

  def test_negative_small(self):
    assert totalStringValues(["-1", "", "-4", "3"]) == -2, "Should be -2"

  def test_invalid(self):
    self.assertRaises(ValueError, totalStringValues, ["3d4f"])

if __name__ == "__main__":
  print("Running tests...")
  unittest.main()
  print("Tests passed")