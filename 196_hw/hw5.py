# Matrix Transpose
#
# Write a function that, given a 2d array (matrix) returns the trasnpose
# of that matrix. The transpose of a matrix is when the rows of the
# source matrix become the columns of the resulting matrix:
#
# 1  2      1  3  5
# 3  4  ->  2  4  6
# 5  6
#
# It may be useful to read this Wikipedia article on matrix transposes:
#   https://en.wikipedia.org/wiki/Transpose
#
# Note: You may not use any builtin functions in this problem.
#
# Example(s)
# ----------
# Example 1:
#   Input: [[1,2],[3,4],[5,6]]
#   Output:
#   [[1, 3, 5], [2, 4, 6]]
#
# Example 2:
#   Input: [['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p']]
#   Output:
#   [['a', 'e', 'i', 'm'], ['b', 'f', 'j', 'n'], ['c', 'g', 'k', 'o'], ['d', 'h', 'l', 'p']]
#
# Parameters
# ----------
# matrix : List[List]
#   A 2d array of arbitrary rectangular size with arbitrary data elements
#
#
# Returns
# -------
# List[List]
#   Returns the transposed matrix
#
def matrix_transpose(matrix):
    """
    returns the matrix transpose
    """
    pass

# matrix multiply
#
# Given two 2d arrays, return the product of those two matricies.
# You can read about matrix multiplication here: https://en.wikipedia.org/wiki/Matrix_multiplication
# If matrix multiplication is possible, return the product as a list representing said matrix.
# Otherwise, return None.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: [[1,4,6]], [[2,3],[5,8],[7,9]]
#
#
#   Output:
#   [[64,89]]
#
#   Reasoning:
#   Matrix product. Notice that the input and output for a matrix with one row is still nested in a 2d array.
#
# Parameters
# ----------
# arr0 : list
#   a 2d array representing a matrix
#
# arr1 : list
#   a 2d array representing a matrix
#
# Returns
# -------
# arr
#   2d array with the product
# None
#   if product is impossible
def matrix_multiply(arr0, arr1):
    """
    returns the product of two matricies, None if not possible.
    """
    pass

# Unique Rows
#
# Write a function that, given a 2d array (matrix) returns only the unique rows
# within a matrix, in the order that they appeared in the original matrix.
#
# 1 0 0 1 3
# 1 2 3 4 5     1 0 0 1 3
# 5 3 6 2 3  -> 1 2 3 4 5
# 1 0 0 1 3     5 3 6 2 3
# 5 3 6 2 3
#
# Example(s)
# ----------
# Example 1:
#   Input: [[1,2],[3,4],[1,2],[5,6]]
#   Output:
#   [[1,2],[3,4],[5,6]]
#
# Example 2:
#   Input: [[1,0,0,1,3],[1,2,3,4,5],[5,3,6,2,3],[1,0,0,1,3],[5,3,6,2,3]]
#   Output:
#   [[1,0,0,1,3],[1,2,3,4,5],[5,3,6,2,3]]
#
# Parameters
# ----------
# matrix : List[List]
#   A 2d array of arbitrary rectangular size with arbitrary data elements
#
# Returns
# -------
# List[List]
#   Returns a new matrix with the unique rows of the original matrix
#
def unique_rows(matrix):
    """
    returns unique rows
    """
    pass

# Zero Sum
#
# Return True if a subarray (not any element) summed can create 0.
# Otherwise return False.
#
# Restrictions
# ------------
# Your runtime must be O(n). You can assume the running time of updating a dictionary is O(s)
# where s is the size of the smaller dictionary (constant if you update a dictionary with finite
# elements).
#
# You CANNOT assume the order given will be sorted.
#
# Example(s)
# ----------
# Example 1:
#   Input: zero_sum([0, 1, 2, 3, 4, 5])
#   We need to see if a subarray can create 0.
#   The first element gives us 0. So there is a subarray that can create 0.
#   Output:
#   True
#
# Example 2:
#   Input: zero_sum([10, 20, -20, 3, 21, 2, -6])
#   We need to see if a subarray can create 0.
#   The subarray [20, -20] can create zero.
#   Output:
#   True
#
# Parameters
# ----------
# arr : list
#   A list/array of integers.
#
# Returns
# -------
# Bool
#   True if a subarray can be 0.
#   False if a subarray cannot be 0.
#
def zero_sum(arr):
    """
    Returns if the given list has a subarray that sums to 0.
    """
    pass

# Longest Incremental Sequence
#
# Given a list, find the longest sequence in the list.
# The sequence we want to find is defined to be the sequence in which
# the number be a certain number is one less.
# For example: [1, 2, 3, 4] would be a sequence we want to find, as well as,
# [5, 6, 7, 8] or [10, 11, 12] OR [101, 102, 103]. However, we do not want a sequence like
# [10, 20, 30, 40...] or [55, 60, 65, 70, 75...].
#
# Restrictions
# ------------
# Your runtime must be O(n). You can assume the running time of updating a dictionary is O(s)
# where s is the size of the smaller dictionary (constant if you update a dictionary with finite
# elements).
#
# You CANNOT assume the order given will be sorted.
#
# Example(s)
# ----------
# Example 1:
#   Input: [9, 3, 4, 1, 2, 100, 200, 1, 4]
#   Here, the longest sequence will be [1, 2, 3, 4]. Note a couple of things:
#   The order of appearance did not matter.
#   The sequence is defined to be incremented by 1. So we won't be looking for something like
#   [100, 200, 300] etc. Only a subsequence in order. i.e. [1, 2, 3, 4] or [5, 6, 7, 8].
#
#   Output:
#   4
#
# Example 2:
#   Input: [10, 20, 30, 40, -1, -2, -3, 0, 1, 2, 3, 100]
#   It is a bit easier to see than example 1. Nonetheless, the same principles apply.
#   The longest sequence here would be [-3, -2, -1, 0, 1, 2, 3].
#
#   Output:
#   7
#
# Parameters
# ----------
# arr : list
#   A list/array of integers.
#
# Returns
# -------
# int
#   The number of elements the longest incremental sequence the list has.
#
def longest_incremental_sequence(arr):
    """
    Given a list, returns the longest incremental sequence.
    """
    pass

# Magic Squares
#
# A magic square is an arrangement of distinct integers in a grid, where the numbers in each row, column, and the main
# and secondary diagonals all add up to be the same number, called the "magic constant".
# Given a 2d array representing a grid, find out if it is a magic square. Return is boolean "True" or "False".
#
# Restrictions:
# You CANNOT assume the size of the square
# You CANNOT assume that your input IS a square
# you CAN assume that objects in the grid will only be integers.
#
# Example(s)
# ----------
# Example 1:
#   Input: [[2,7,6],[9,5,1],[4,3,8]]
#
#
#   Output:
#   True
#
#   Reasoning:
#   row 0: 2+7+6 = 15
#   row 1: 9+5+1 = 15
#   row 2: 4+3+8 = 15
#   col 0: 2+9+4 = 15
#   col 1: 7+5+3 = 15
#   col 2: 6+1+8 = 15
#   diag 1: 2+5+8 = 15
#   diag 2: 4+5+6 = 15
#
#
# Parameters
# ----------
# arr : list
#   A 2d list/array of integers.
#
# Returns
# -------
# Bool
#   Whether or not the 2d matrix represents a magic square.
def magic_square(arr):
    """
    Returns if given array represents a magic square
    """
    pass

# nQueens
#
# NQueens is a classical problem that asks if we can place N queens on an NxN chessboard so that no two queens can attack
# each other.
# Write a function nQueens(board) that takes a 2d array of bits (0 or 1) that indicates whether a queen is present on
# said tile (1 means the queen is present, 0 is an empty cell). Return boolean True if the configuration makes it so that
# none of the queens can attack each other, and false if there are any sets of Queens that can.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: [[0,1,0],[0,0,0],[0,0,1]]
#
#
#   Output:
#   True
#
#   Reasoning:
#   The queens are located in arr[0][1] and arr[2][2]. There is no straight path from either Queen to the other, therefore
#   they cannot attack each other.
#
# Parameters
# ----------
# arr : list
#   A 2d list/array of integers (0 or 1).
#
# Returns
# -------
# Bool
#   Whether or not any set of queens can attack eath other on the board
def nQueens(arr):
    """
    Returns if given array represents an nQueens configuration
    """
    pass
