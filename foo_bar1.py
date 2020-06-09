def solution(s):
  # Your code here
  # test cases:
  # 0. "ab|ab||ab|ab" --> 4
  # 1. "abc|abc" --> 4
  # 2. "aba|aba|aba" --> 3
  # 3. "a" --> 1
  # 4. "" --> 0
  # 5. "abcdefghi" --> 1
  
  
  # string: "ababab"
  #          012345
  # prefix: "ab" 01
  # len(prefix) aka index = 2
  # num_slices = 6/2 = 3
  # comp:   "__ab" 23
  # 1, 2, 3 xrange(1, num_slices)
  # pattern: s[0:2], compare s[2:4], compare s[4:6]
  
  if s == "":
    return 0
  for index in range(1, (int)(len(s)/2)):
    # index represents len(prefix) too
    prefix = s[0:index]
    if len(s) % index != 0:
        continue
    num_slices = (int) (len(s) / index)
    # if prefix repeats an integer number of times, return num_slices
    # total = 1
    print("prefix: " + prefix)
    for i in range(0, num_slices):
      comp = s[i*index : (i+1):index]
      if prefix == comp :
        print(prefix + " vs. " + comp)
  return num_slices


test_string = input("Enter a string: ")
print(solution(test_string))
print("gosh darn it")