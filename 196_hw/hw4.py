# Counting Anagrams
#
# Write a function that, given a string, will return the number of instances
# of anagrams of that string in the provided list of strings.
#
# Two strings are anagrams when they have the exact same number and frequency
# of characters, and order is ignored. Taking a string and rearranging its
# characters generates anagrams of that string. So, 'listen' and 'silent' are
# anagrams.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: ['19cs6', 'apple', '1s9c6', 'dog', 'cs1962', 'sc961'], 'cs196'
#   Output:
#   3
#
# Example 2:
#   Input: ['aabbcc', 'abcabc', 'abcdef', 'defghi'], 'golf'
#   Output:
#   0
#
# Parameters
# ----------
# arr : List[str]
#   A list of strings
#
# uniq : str
#   The string to find anagrams of
#
# Returns
# -------
# int
#   The number of strings in arr that are exact anagrams of uniq.
#
def count_anagrams(arr, uniq):
    """
    Given a list of strings, find the anagrams of uniq in the list and return 
    the count.
    """
    pass

# Happy Numbers
#
# A happy number is a positive integer with the following characteristic: if we
# take ths sum of the square of its digits to get another number, and take the
# sum of the squares of that number and continue this process, we eventually
# get the number 1. If a number is not happy, we will get stuck in a cycle that
# does not include the number 1.
#
# Your task is to find the number of happy numbers between 0 and the given
# integer n.
#
# Calculation Example:
# 19 is a happy number.
# 19 -> 1^2 + 9^2 = 1 + 81 = 82
# 82 -> 8^2 + 2^2 = 64 + 4 = 68
# 68 -> 6^2 + 8^2 = 36 + 64 = 100
# 100 -> 1^2 + 0^2 + 0^2 = 1.
#
# Example(s)
# ----------
# Example 1:
#   Input: 8
#   Between 0 and 8, numbers 1 and 7 are happy numbers
#   Output:
#   2
#
# Example 2:
#   Input: 15
#   Between 0 and 25, numbers 1, 7, 10, and 13 are happy numbers
#   Output:
#   4
#
# Parameters
# ----------
# n : int
#   The high end of the range you need to check for happy numbers
#
# Returns
# -------
# int
#   The number of happy numbers between 0 and n (exclusive)
#
def happy_numbers(n):
    """
    Given an integer input, return the number of happy numbers between 0 and n
    """
    pass

# Reverse Dictionary
#
# Given a dictionary, return a new dictionary with keys and values swapped.
#
# Example(s)
# ----------
# Example 1:
#   Input: {'a': 1, 'b': 2}
#   We will need to swap the keys and values.
#   Output:
#   {1: 'a', 2: 'b'}
#
# Parameters
# ----------
# d : dict
#   The dictionary you will be required to swap
#
# Returns
# -------
# dict
#   The dictionary given, but reversed
#
def reverse_dictionary(d):
    """
    Given a dictionary d, reverse the keys and values.
    """
    pass

# Alphabet Finder
#
# Given a string, find the shortest prefix where all letters of the alphabet 
# first appears. If there is no prefix such that all the letters of the alphabet
# appear, return None.
#
# Example(s)
# ----------
# Example 1:
#   Input: 'abcdefghijklmnopqrstuvwxyz'
#   This is just the alphabet.
#   Output:
#   'abcdefghijklmnopqrstuvwxyz'
#
# Example 2:
#   Input: 'hi!abcdefghijklmnopqrstuvwxy you wont see a z till there!'
#   The alphabet first appears where the first z appears.
#   Output:
#   'hi!abcdefghijklmnopqrstuvwxy you wont see a z'
#
# Example 3:
#   Input: 'Wait, what if a sentence does not have all letters?'
#   There is no alphabet in the input.
#   Output:
#   None
#
# Parameters
# ----------
# arg1 : String
#   Input String
#
# Returns
# -------
# str
#   The prefix that the alphabet first appears.
# None
#   There is no complete alphabet.
#
def alphabet_finder(sentence):
    """
    Given a string, find the shortest prefix where all the letters of the 
    alphabet first appears.
    """
    pass

# Anagram of Palindrome
#
# Given a string, find out if it is an anagram of a palindrome.
#
# Example(s)
# ----------
# Example 1:
#   Input: 'ivicc'
#   Output: True
#   Anagram of 'civic', which is a palindrome.
#
# Parameters
# ----------
# arg1 : String
#   Input String
#
# Returns
# -------
# bool
#   True if the string is an anagram of a palindrome, False otherwise
#
def anagram_of_palindrome(word):
    """
    Given a string, return true if the string is an anagram of a palindrome.
    """
    pass

# is unique
#
# Given a string, find out if it is made of only unique characters. Characters 
# are not case sensitive, so 'l' and 'L' are considered to be the same 
# character.
#
# Example(s)
# ----------
# Example 1:
#   Input: 'abcdef'
#   Output: True
#   'abcdef' is made of unique characters
#
# Example 2:
#   Input: 'hello worLd'
#   Output: False
#   There are 3 'l's in 'hello world', therefore it is not made of unique 
#   characters.
#
# Parameters
# ----------
# arg1 : String
#   Input String
#
# Returns
# -------
# bool
#   True if the string is made of unique characters, false otherwise.
#
def is_unique(word):
    """
    Given a string, return true if the string is made of unique characters.
    """
    pass
