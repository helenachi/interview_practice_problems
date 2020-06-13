import random


def swap(array, i, j):
  # array[i], array[j] = array[j], array[i]
  temp = array[i]
  array[i] = array[j]
  array[j] = temp


def partition(array, lo, hi):
  i = lo - 1
  for j in range(lo, hi ):
    if array[j] < array[hi]:
      i += 1
      swap(array, i, j)
  swap(array, i + 1, hi)
  return i + 1


def quicksort(array, lo, hi):
  if lo < hi:
    pi = partition(array,lo,hi) 
    quicksort(array, lo, pi-1) 
    quicksort(array, pi+1, hi)
  return array


array = [4, 0, 2, -1, 3]
print(array)
print(quicksort(array, 0, len(array) - 1))