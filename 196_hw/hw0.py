###############################################################################
###    HW0
###
###    Function definitions have been declared for you. Fill in the function
###    definitions with your solution.
###
###############################################################################

# Reverse String
#
# Given a string, print the reverse.
#
# Ex INPUT:
# "Hello World"
#
# Output:
# "dlroW olleH"
#
def reverse_string(my_str):
    print(my_str[::-1])

# Odd Even
#
# Given a string, print "odd" if there are an odd number of characters and "even" if there are an even number of characters
#
# Ex INPUT:
# "Hello World"
#
# Ex OUTPUT:
# "odd"
#
def oddEven(str):
    print("even" if len(str) % 2 == 0 else "odd")

# Sign Flipper
#
# Input:
#   ary: An array of ints with arbitrary length
#
# Output:
#   Flip the signs of all the integers in the array and return that
#   resulting array.
#
# Example:
#   >>> sign_flipper([1, -2, 3])
#    [-1, 2, -3]
#

def sign_flipper(arr):
    # what do with 0**********
    return [elem * -1 for elem in arr]

# Intersect Sum
#
# Input:
#   ary1: Array of ints with arbitrary length
#   ary2: Array of ints with arbitrary length
#
# Output:
#   Return the sum of integers that are in both the first array and the
#   second array. (Count each unique integer only once for the sum)
#
# Example:
#   >>> intersect_sum([1, 2, 3, 3, 4], [3, 4, 5, 6])
#    7
#
def intersect_sum(ary1, ary2):
    # a = [1, 2, 3, 3, 4]
    # b = [3, 4, 5, 6, 8, 10, 12]
    # smaller = a
    # larger = b
    # ---checking a[0] == 1
    # 1 in b? --> no; sum = 0
    # 2 in b? --> no; sum = 0

    if not ary1 or not ary2:
        return None

    result = []
    for elem in ary1:
        if elem in ary2 and elem not in result:
            result.append(elem)
    return sum(result)

# Given a Dictionary with the type of fruit as the key
# and the number of that type of fruit as its value, return the
# number of bananas as a String. Ex. "5 Bananas"
# We do not care about gramatical correctness. When there is 1 banana, please
# return '1 Bananas'.
# If bananas could not be found, return the String "No Bananas"
# Examples:
# >>> num_bananas({'apples': 4, 'bananas': 10, 'kiwis': 9})
# '10 Bananas'
# >>> num_bananas({'oranges': 10, 'apples': 2})
# 'No Bananas'
# >>> num_bananas({'bananas': 1, 'watermelons': 10})
# '1 Bananas'
#
def num_bananas(fruit_basket):
    # what if {"bananas": 0}*****
    if "bananas" not in fruit_basket:
        print("No Bananas")
    else:
        print(str(fruit_basket["bananas"]) + " Bananas")

# Given a string, return whether it has repeating letters or not.
# If the word is repeating, return the max number or repeating letters.
# Otherwise, return 0.
# Examples:
# >>> repeating('potato')
# 2
# >>> repeating('abcdefgh')
# 0
# >>> repeating('aabbccddeeffff')
# 4
#
def repeating(string):
    lookup = {}
    for c_char in string:
        if c_char not in lookup:
            lookup[c_char] = 1
        else:
            lookup[c_char] += 1
    c_max = 0
    for key in lookup:
        if lookup[key] > c_max:
            c_max = lookup[key]

    return c_max

# Given an integer N, print a triangle that is height N.
#
# Ex INPUT:
# 4
#
# Ex OUTPUT:
#     *
#    **
#   ***
#  ****
#
def triangle(input):
    stars = ""
    for i in range(input):
        for _ in range(input-i-1):
            print(" ", end="")
        stars = stars + "*"
        print(stars)
    
# Given an integer N, print the Fibonacci series up to its Nth term.
#
# Ex INPUT:
# 8
#
# Ex OUTPUT:
# 1,1,2,3,5,8,13,21
#
def fibonacci(input):
    lookup = [0 for i in range(input)]
    lookup[0] = 1
    lookup[1] = 1
    for i in range(2, input):
        lookup[i] = lookup[i - 1] + lookup[i - 2]
    return lookup[input - 1]

# Given a 2d array, flatten the array.
#
# Ex INPUT:
# [[1],[2,3],[4,5,6],[7,8,9,10]]
#
# Ex OUTPUT:
# [1,2,3,4,5,6,7,8,9,10]
#
def flatten(input):
    result = []
    for row in input:
        for elem in row:
            result.append(elem)
    return result

# Given a 2d NxN matrix, traverse the structure in a spiral and return an array
# representing the traversed values in order.
#
# Ex INPUT:
# [[a,b,c,d,e],
#  [f,g,h,i,j],
#  [k,l,m,n,o],
#  [p,q,r,s,t],
#  [u,v,w,x,y]]
#
# Ex OUTPUT:
# [a,b,c,d,e,j,o,t,y,x,w,v,u,p,k,f,g,h,i,n,s,r,q,l,m]
#
def spiralMatrix(input):
    halfway = (int)(len(input) / 2) + 1
    result = []
    for i in range(halfway):
        my_append(input, i, result)
    return result

def my_append(input, ith, result):
    N = len(input)
    if N % 2 == 1 and ith == (int)(N / 2):
        result.append(input[ith][ith])
    else:
        stop = N - ith - 1
        for j in range(ith, stop):
            result.append(input[ith][j])
        for i in range(ith, stop):
            result.append(input[i][stop])
        for j in range(stop, ith, -1):
            result.append(input[stop][j])
        for i in range(stop, ith, -1):
            result.append(input[i][ith])


"""
Given a string in a way formatted below, find the number of <name>'s
friend's friend who are not friends with <name>.

Format:
graph is given in a newline formatted string. The first word is a person's name,
and the following names are friends of that person.

Sample 1:
missing_friends('james', '''
                         james jack jill
                         jack jill james
                         jill jack james
                         ''')

This means that we need to find the number of James' friends' friends, that are
also not friends with James.

James is friends with Jack and Jill, and both Jack and Jill
have friends that are friends with James, that means we
should return 0. (James -> Jack -> Jill -> James and James -> Jill -> Jack -> James)

Sample 2:
missing_friends('james', '''
                         james jack
                         jack james jill bob
                         jill jack bob
                         bob jill jack
                         ''')
James is friends with Jack, and Jack is friends with Jill, Bob, and James. However,
Jill and Bob are not friends with James, so we return 2
(2 friends of friends that are not friends with James.)

Sample 3:
missing_friends('james', '''
                         james jack
                         jack james jill
                         jill jack
                         ''')

James is friends with Jack, who are friends with James and Jill. However,
Jill is not friends with James, so we return 1 (1 friends of friends that are not friends with James.)

"""
def missing_friends(name, graph):
    pass







# def brewster_flatten(x):
#     def flat(xs, acc, i, lim):
#         if i == lim:
#             return acc
#         else:
#             return flat(xs, acc+xs[i], i+1, lim)
#     return flat(x, [], 0, len(x))

# def brewster_spiralMatrix(matrix):
#     def f(n, o):
#         a = list(n*[0]) + list(range(1, n)) + list((n-2)*[n-1]) + list(reversed(range(1, n)))
#         b = a[n-1:] + a[:n-1]
#         return list(map(lambda r, c: matrix[r+o][c+o], a, b))
#     return brewster_flatten([f(n, o) for (n, o) in zip(range(len(matrix), 0, -2), range(len(matrix)))])