import random


def swap(array, i, j):
  # array[i], array[j] = array[j], array[i]
  temp = array[i]
  array[i] = array[j]
  array[j] = temp


def partition(array, lo, hi):
  # swap(array, pivot, hi)
  i = lo - 1
  for j in range(lo, hi ):
    if array[j] < array[hi]:
      i += 1
      swap(array, i, j)
  swap(array, i + 1, hi)
  return i + 1


def quicksort(array):
  if not array or len(array) <= 1:
    return array
  # p = random.randint(0, len(array) - 1)
  # print("random pivot index and value: " + str(p) + ", " + str(array[p]))
  p_index = partition(array, 0, len(array) - 1)
  quicksort(array[0:p_index])
  quicksort(array[p_index + 1:])
  return array


array = [4, 0, 2, -1, 3]
print(array)
print(quicksort(array))








# def partition(arr,low,high): 
#   i = ( low-1 )         # index of smaller element 
#   pivot = arr[high]     # pivot 

#   for j in range(low , high): 
#     # If current element is smaller than or 
#     # equal to pivot 
#     if   arr[j] <= pivot: 
#       # increment index of smaller element 
#       i = i+1 
#       arr[i],arr[j] = arr[j],arr[i] 

#   arr[i+1],arr[high] = arr[high],arr[i+1] 
#   return ( i+1 ) 


# def quickSort(arr,low,high): 
#   if low < high: 
#     # pi is partitioning index, arr[p] is now 
#     # at right place 
#     pi = partition(arr,low,high) 

#     # Separately sort elements before 
#     # partition and after partition 
#     quickSort(arr, low, pi-1) 
#     quickSort(arr, pi+1, high) 


# array = [4, 1, 5, 2, 3]
# n = len(array)
# quickSort(array, 0, n-1)
# print("Sorted array is: ")
# print(array)