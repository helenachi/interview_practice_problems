def merge(left, right):
  if not left and not right:
    return []
  elif not left and right:
    return right
  elif left and not right:
    return left
  
  result = []
  if (left[0] <= right[0]):
    result.append(left[0])
    tail = merge(left[1:], right)
    result.extend(tail)
  else:
    result.append(right[0])
    tail = merge(left, right[1:])
    result.extend(tail)

  return result


def mergesort(array):
  if not array or len(array) <= 1:
    return array
  
  mid = (int)(len(array) / 2)
  left = mergesort(array[:mid])
  right = mergesort(array[mid:])
  return merge(left, right)


array = [1, 3, 2, 1, 6, 7, 8, 4, 5]
print(array)
print(mergesort(array))