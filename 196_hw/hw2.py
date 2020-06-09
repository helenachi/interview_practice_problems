# Pangram
#
# A pangram is any string that contains all the letters of the alphabet.
# In this function, you will be given a string and your task is to RETURN
# a boolean representing whether or not the string is a pangram.
#
# Note: Case does not matter when determining if a string is a pangram. So,
#       'abcDeFghiJkLmNopqrstuvwxyz' is a valid pangram.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: 'the quick brown fox jumps over the lazy dog'
#   This string indeed contains all letters from a-z
#   Output:
#   True
#
# Parameters
# ----------
# str_in : str
#   A mixed case single-line string.
#
# Returns
# -------
# bool
#   Whether or not str_in is a pangram
#
def pangram(str_in):
    pass

# Prime Test
#
# A prime number is any natural number greater than 1 which has no positive
# divisors other than 1 and itself. In this function, you will get an integer
# and RETURN a boolean representing whether or not the number is prime.
#
# (Pat yourself on the back if you're able to prime check 961748941 in under
#  a second)
#
# Example(s)
# ----------
# Example 1:
#   Input: 13
#   13 has no divisors other than 1 and itself
#   Output:
#   True
#
# Example 2:
#   Input: 24
#   24 is divisible by 2, so it is not a prime number
#   Output:
#   False
#
# Parameters
# ----------
# num : int
#   The integer to check for being prime.
#   For the purposes of this problem, num < 10**5
#
# Returns
# -------
# bool
#   Whether or not 'num' is a prime number
#
def prime_test(num):
    pass


# Count Vowels
#
# For our purposes a vowel is either a, e, i, o, or u. Iterate through
# a string and return the number of vowels in it. Case does not matter.
#
# Example(s)
# ----------
# Example 1:
#   Input: aAaeeizzzzz
#   This string contains 3 a's, 2 e's, 1 i. So 6 vowels.
#   Output:
#   6
#
# Parameters
# ----------
# str_in : str
#   A mixed case single line string.
#
# Returns
# -------
# int
#   Number of vowels.
#
def count_vowels(str_in):
    pass


# Most Common Character
#
# You will receive a string as a parameter and you will need to return the
# character in the string that occurs the most. Case does not matter. The
# output should be lower case (if applicable). In case of a tie, return the
# character that showed up first.
#
# Example(s)
# ----------
# Example 1:
#   Input: aaAAaBBbcc
#   a occurs the most, at 5 times.
#   Output:
#   a
#
#
# Parameters
# ----------
# str_in : str
#   A mixed case single line string
#
# Returns
# -------
# str
#   The most common character in the given string
#
def most_common_char(str_in):
    pass

# Fibonacci Sequence
#
# Given a number n, return the nth fibonacci sequence.
#
# Restrictions
# ------------
# We will not test a number larger than 100.
#
# Example(s)
# ----------
# Example 1:
#   Input: fibonacci(4)
#   The fourth fibonacci number can be calculated by doing a sequence.
#   1, 1, 2, 3, 5,...
#   The fourth sequence is 3.
#   Output: 3
#
# Example 2:
#   Input: fibonacci(5)
#   The fifth fibonacci number can be calculated by doing a sequence.
#   1, 1, 2, 3, 5,...
#   The fourth sequence is 5.
#   Output: 5
#
# Parameters
# ----------
# num : int
#   Num is the nth number of the sequence you need to calculate.
#
# Returns
# -------
# num : int
#   The nth number in the fibonnaci sequence
def fibonacci(num):
    pass


# Advanced Divide
#
# Given 2 numbers, divide the first with the second.
# However, you must return an integer when the number is an integer,
# otherwise return a float.
#
# Restrictions
# ------------
# Zero will not be given as one of the arguments
#
# Example(s)
# ----------
# Example 1:
#   Input: advanced_divide(5, 6)
#   We want to divide 5 by 6. The result is a fraction, so we need to represent it as a float
#
#   Output:
#   0.8333333333333334
#
# Example 2:
#   Input: advanced_divide(10, 5)
#   We want to divide 10 by 5. The result is an integer, so we need to represent it as an integer.
#
#   Output:
#   2
#
# Parameters
# ----------
# num1 : int or float
#   The number that will get divided.
# num2 : int or float
#   The number that will divide.
#
# Returns
# -------
# int or float
#   An integer if the division should produce an integer.
#   A float if the division is a fraction.
def advanced_division(num1, num2):
    pass


# Palindrome
#
# A palindrome is any string that is the same when reversed.
# You will be given a string and you must RETURN a boolean 
# representing whether or not the string is a palindrome.
#
# Note: Case does not matter
#
#
# Example(s)
# ----------
# Example 1:
#   Input: 'a nut for a jar of tuna'
#   This string is the same forward and back
#   Output:
#   True
#
# Example 2:
#   Input: 'this is not a palindrome'
#   This string is not the same forward and back
#   Output:
#   False
#
# Parameters
# ----------
# str_in : str
#   A mixed case single-line string.
#
# Returns
# -------
# bool
#   Whether or not str_in is a palindrome
#
def palindrome(str_in):
    pass

# Unique
#
# Check if a word is made up of unique letters
# Note: Case does not matter
#
# Example(s)
# ----------
# Example 1:
#   Input: 'computer'
#   The word 'computer' has no repeating letters
#   Output:
#   True
#
# Example 2:
#   Input: 'science'
#   The word 'science' repeats the letters c and e
#   Output:
#   False
#
# Parameters
# ----------
# str_in : str
#   A mixed case single-line string.
#
# Returns
# -------
# bool
#   Whether or not str_in is made up of unique letters
#
def unique(str_in):
    pass

# nthPalindromicPrime
#
# Given a non-negative integer n return the nth palindromic prime
# A palindromic prime is a number that is both prime and a palidrome - a prime number that is read the same backwards and forwards.
# Some examples of palindromic primes: 2,3,5,7,11,101,131,151,181,191,313
# For example, if n = 3, the third palindromic prime is 5. Return 5.
#
# Example(s)
# ----------
# Example 1:
#   Input: 5
#   What is the 5th palindromic prime? It is 11
#   Output:
#   11
#
# Example 2:
#   Input: 8
#   What is the 8th palindromic prime? It is 151
#   Output:
#   151
#
# Parameters
# ----------
# n : a non-negative integer
#
# Returns
# -------
# int
#   the nth palindromic prime
#
# hint: write a helper function isPalindromicPrime(n) first!

def nthPalindromicPrime(n):
    pass
