"""
problem description
"""


def max_score(i):
  '''
  dvnselfjkds,
  '''
  lookup_table = [0 for _ in range(0, len(scores))]
  lookup_table[len(scores) - 1] = max(0, scores[len(scores) - 1])
  for i in range(len(scores) - 2, -1, -1):
    min_dance_index = min(len(scores) - 1, i + 1 + waittimes[i])
    dance = scores[i] + lookup_table[min_dance_index]
    min_wait_index = min(len(scores) - 1, i + 1)
    wait = lookup_table[min_wait_index]
    lookup_table[i] = max(dance, wait)
  return lookup_table[0]
  

def max_score_recursive(s, w):
  '''
  lrvjdfknsd
  '''
  if not s:
    return 0
  elif len(s) == 1:
    return max(s[0], 0)

  index = 1 + w[0]
  dance = s[0] + max_score_recursive(s[index:], w[index:])
  wait = max_score_recursive(s[1:], w[1:])
  return max(dance, wait)


scores = [5, 7, -2, 3, 10, 3]
waittimes   = [1, 0,  3, 1,  0, 2]
print("scores: ", sep="")
print(scores)
print("wait: ", sep="")
print(waittimes)
print("DP: ", sep="")
print(max_score(0))
print("recursive: ", sep="")
print(max_score_recursive(scores, waittimes))