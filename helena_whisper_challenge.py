"""
Helena Chi - Whipser.ai Coding Exercise
June 2020
"""

"""
Suggestions for Improvement
1. spacing
2. total += product is just a dot product
3. run pylint or black
4. don't use list.copy()
5. explain your convolve approach
6. time and space complexity
7. more extensive testing / separate testing program
8. making classes/modules
9. wrapping main in __main__
10. global variables should be all caps
11. readme for how to run program.
12. precondition
13. dependencies (python vresion, etc)
14. include comparison with np.convolve()
15. EXTRA write in all valid languages and compare
16. Consolidate get larger/smaller array methods
"""

import numpy as np

kaiser_smoothing_filter = [
  -0.01452123, -0.0155227, 0.01667252, 0.01800633, -0.01957209,
  -0.0214361, 0.02369253, 0.02647989, -0.03001054, -0.03462755,
  0.04092347, 0.05001757, -0.06430831, -0.09003163, 0.15005272,
  0.45015816, 0.45015816, 0.15005727, -0.09003163, -0.06430831,
  0.05001757, 0.04092347, -0.03462755, -0.03001054, 0.02647989,
  0.02369253, -0.0214361, -0.01957209, 0.01800633, 0.01667252,
  -0.0155227, -0.01452123
  ]


def decimate_by_2(in_arr):
  return [elem for index,elem in enumerate(in_arr) if index % 2 == 0]


def downsample_by_2(data_arr):
  convolved = my_convolve(data_arr, kaiser_smoothing_filter)
  return decimate_by_2(convolved)


def my_convolve(data_arr, filter_arr):
  """ Returns the convolution of applying a 1D filter array on a 1D data array
  Returns the same result as numpy's convolve from https://numpy.org/devdocs/reference/generated/numpy.convolve.html
  i.e. np.convolve(data_arr, filter_arr, mode='same')

  Keyword arguments:
  data_arr -- the array to be convolved by applying the filter_array
  filter_arr -- the filter array to be applied to the data_array
  """
  larger = get_larger_array(data_arr, filter_arr)
  smaller = get_smaller_array_reversed(data_arr, filter_arr)

  large_base_len = len(larger)
  small_base_len = len(smaller)

  padding = int(len(smaller) / 2)
  pad(larger, padding)

  output = []
  for i in range(large_base_len):
    max_start_index = max(padding, i)
    min_end_index = min(padding + large_base_len, i + small_base_len)
    total = 0
    for j in range(max_start_index, min_end_index):
      total += larger[j] * smaller[j]
    output.append(total)
    smaller.insert(0, 0)
  
  return output


def pad(arr, padding=0):
  """ Adds padding to either side of an array.

  Keyword arguments:
  arr -- array to be modified with padding
  padding -- the number of 0's to be added to each side of the array (default 0)
  """
  for i in range(padding):
    arr.insert(i, 0)
    arr.append(0)


def get_larger_array(arr1, arr2):
  """ Returns a copy of the larger of two arrays
  """
  return arr1.copy() if len(arr1) >= len(arr2) else arr2.copy()

def get_smaller_array_reversed(arr1, arr2):
  """ Returns a copy of the reverse of the smaller of two arrays
  """
  return arr1[::-1].copy() if len(arr1) < len(arr2) else arr2[::-1].copy()



example_data = [0, 1, 4, 13, 5, 3.22109]
print(downsample_by_2(example_data))