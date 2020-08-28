import math
##############################################################################
#
#   HW1.py
#   CS196 FA16
#   Functions, Strings, Types
#   Released: August 31, 2016
#   Due: September 6th, 7pm
#
###############################################################################
# CSVify
#
# Often, you will need to take some sort of data and condition it to be in a
# particular format. In this case, we will take a long string and manipulate it
# to behave like a comma-separated-value file. To do this, you should remove
# the whitespace between words in the string and RETURN the conditioned string
# whilst keeping intact line breaks.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: 'the quick  brown   fox\njumped    over the  lazy   dog'
#   Should replace all the whitespace between the words with commas
#   Output:
#   'the,quick,brown,fox\njumped,over,the,lazy,dog'
#
# Parameters
# ----------
# raw_str : str
#   A (potentially) multilined string containing words, newlines, and
#   whitespace
#
# Returns
# -------
# str
#   The comma-separated string
#
def csvify(raw_str):
    """
    Removes whitespaces and replaces with commas

    >>> print csvify('the quick  brown   fox\\njumped    over the  lazy   dog')
    the,quick,brown,fox
    jumped,over,the,lazy,dog
    >>> print csvify('subject course   term\\nCS 196    Fall16\\nCS 125     Fall16')
    subject,course,term
    CS,196,Fall16
    CS,125,Fall16
    """
    # Your code goes here!
    separated = raw_str.split(" ")
    print(separated)
    result = ""
    index = 0
    for word in separated:
        if word != "":
            result = word
            break
        else:
            index += 1
    for word in separated[index + 1:]:
        if word != "":
            result += "," + word
    return result


###############################################################################
# To_Binary
#
# RETURN a string representing the integer parameter in binary.
#
# Note: Solutions must not use the `bin()` Python builtin.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: 23
#   The binary representation of 23 is 10111
#   Output:
#   '10111'
#
# Parameters
# ----------
# num : integer
#   A positive integer
#
# Returns
# -------
# str
#   String representation of the integer using the fewest number of characters
#   as possible. (No zero padding)
#
def to_binary(num):
    """
    Represents an integer in binary as a string of 0's and 1's

    >>> print to_binary(23)
    10111
    >>> print to_binary(123456789)
    111010110111100110100010101
    """
    # Your code goes here!
    lookup = {0: [0], 1: [1]}
    l_to_m_sb = to_binary_helper(num, lookup)
    result = ""
    for i in l_to_m_sb[::-1]:
        result += str(i)
    return result

# to_binary_helper
#
# RETURN a string representing the integer parameter in binary.
#
# Parameters
# ----------
# num : integer
#   A positive integer
# lookup: dict
#   A lookup table of integer binary representations in LSB->MSB list
#
# Returns
# -------
# list
#   List representation of the given integer, num, in binary form from LSB to MSB
#
def to_binary_helper(num, lookup):
    if (num in lookup):
        return lookup[num]
    
    length = int(math.log(num, 2))
    result = [1 if i == length else 0 for i in range(length + 1)]

    remainder = int(num - math.pow(2, length))
    if (remainder > 0):
        sub_length = int(math.log(remainder, 2))
        result[:sub_length+1] = to_binary_helper(remainder, lookup)
    
    lookup[num] = result
    return lookup[num]



###############################################################################
# Sum List
#
# Return an integer that represents the sum of the string list
#
#
# Example(s)
# ----------
# Example 1:
#   Input: "20,4,12"
#   The summation of 20, 4, and 12 is 36.
#   Output:
#   36
#
# Parameters
# ----------
# nums : str
#   Comma separated string list of integers
#
# Returns
# -------
# int
#   Int representation of the sum of strings from the list
#
def sum_list(arr):
    """
    Sums the list of strings into an int

    >>> print sum_list("1,2,3,4")
    10
    >>> print sum_list("4,4")
    8
    """
    iterable = arr.split(",")
    total = 0
    for i in iterable:
        total += int(i)
    return total


###############################################################################
# Remove Given String
#
# You will be given a string and a removal string, and you will
# need to remove the removal string (both upper and lower case)
# from the string and then return your result.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: ("." , "Hello. I'm Frodo.")
#   You should remove all periods.
#   Output:
#   "Hello I'm Frodo"
#
# Parameters
# ----------
# remove_str : str
#   String to remove
# word : str
#   Word to remove character from
#
# Returns
# -------
# str
#   The string you removed the character from
#
def remove_given_str(remove_str, word):
    """
    Removes remove_str from word

    >>> print remove_given_str("H","Harry is hot in Hogwarts")
    arry is ot in ogwarts
    >>> print remove_given_str("oops","Whoopsie, I made an oopsie. Oops!")
    Whie, I made an ie. !
    """
    # Your code goes here!
    length = len(remove_str)
    start = word.lower().find(remove_str.lower())
    while (start >= 0):
        word = word[:start] + word[start+length:]
        start = word.lower().find(remove_str.lower())
    return word


###############################################################################
# To Integer
#
# Take a list of booleans and return an integer made from its binary
#
#
# Example(s)
# ----------
# Example 1:
#   Input: "true,false,true,false"
#   The decimal equivalent of 1010 is 10
#   Output:
#   10
#
# Parameters
# ----------
# arr : str
#   Comma separated string list of booleans
#
# Returns
# -------
# int
#   Int representation of the sum of strings from the list
#
def to_int(arr):
    """
    Converts a list of booleans into an integer

    >>> print to_int("true,false,true,true")
    11
    >>> print to_int("true,false,false,false,true")
    17
    """
    # Your code goes here!
    lsb_to_msb = get_lsb_to_msb(arr)
    total = 0
    for i,val in enumerate(lsb_to_msb):
        if val == 1:
            total += 2 ** i
    return total

def get_lsb_to_msb(arrstr):
    lsb_to_msb = []
    for val in arrstr.split(",")[::-1]:
        if val == "true":
            lsb_to_msb += [1]
        elif val == "false":
            lsb_to_msb += [0]
    return lsb_to_msb


###############################################################################
# Carpet Weaving
#
# Given a width and height, print out a carpet design with alternating diagonal rows of O's and X's
# Define and use a helper function to decide if a carpet square should be an O or X.
#
# Example(s)
# ----------
# Example 1:
#   Input: 4,3
#   Width of 4 and height of 3
#   Output:
#   XOXO
#   OXOX
#   XOXO
#
# Example 2:
#   Input: 2,2
#   Width of 2 and height of 2
#   Output:
#   XO
#   OX
#
# Parameters
# ----------
# width : int
#   Width of carpet
# height : int
#   Length of carpet
#
# Prints
# -------
# The finished carpet
#
def weave_carpet(width, height):
    """
    Prints a design width alternating diagonal rows of O's and X's
    Must use a helper function

    >>> weave_carpet(2,3)
    XO
    OX
    XO
    """
    # Your code goes here!
    string = ""
    for row in range(height):
        for col in range(width):
            string += x_or_o(row, col)
        print(string)
        string = ""

def x_or_o(row, col):
    status_i = row % 2
    status_j = col % 2
    if status_i == status_j:
        return "X"
    else:
        return "O"


###############################################################################
# Caesar Cipher
#
# Caesar Cipher is an old way to encrypt secret messages across two users,
# by using a number to each word in the sentence by.
#
# We will be using the alphabet A-Z, a-z, then 0-9, which means the alphabet you will be shifting
# through will contain 62 characters.
#
# For reference here is the alphabet you will be shifting through:
#
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# a b c d e f g h i j k l m n o p q r s t u v w x y z
# 0 1 2 3 4 5 6 7 8 9
#
# where A is the first character in the alphabet, B is the second, C is the third, and so on.
# Please ignore any characters not in the alphabet, and keep them the same as before.
#
# Given a string and the number of shifts, RETURN the resulting string of the caesar cipher operation.
#
# Example(s)
# ----------
# Example 1:
#   Input: caesar_cipher('Test.', 15)
#   You will need to encode the string 'Test.', by shifting right by 15.
#   T + 15 = i
#   e + 15 = t
#   s + 15 = 7
#   t + 15 = 8
#   . -> . (Keep everything not in the alphabet out)
#   Output:
#   'it78.'
#
# Parameters
# ----------
# sentence : String
#   The sentence that must be encoded.
# shifts : Int
#   The number of right shifts that should be done on the string.
#
# Returns
# -------
# String
#   The Caesar Cipher of the sentence shifted right by shift.
#
def caesar_cipher(sentence, shifts):
    """
    Given a sentence and the number of shifts, RETURN the resulting caesar cipher.

    >>> caesar_cipher('Test.', 15)
    'it78.'
    >>> caesar_cipher('Encoded strings are difficult to read', 30)
    'iH6I787 MNLCHAM 4L8 7C99C6OFN NI L847'
    >>> caesar_cipher('3Q JZf xLY CPLO ESTd AWPLdP DPYO 2PWa!', 15)
    'If You Can Read This Please Send Help!'
    """
    # Your code goes here!
    original = get_original()
    # print()
    result = ""
    for c in sentence:
        char = c
        if c in original.values():
            key = get_key(original, c)
            char = original[(key + shifts) % len(original)]
        result += char
    return result

def get_original():
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    original = {}
    for ind,val in enumerate(string):
        original[ind] = val
    return original

def get_key(dictionary, value):
    for index,char in dictionary.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if char == value:
            return index
    return None


###############################################################################
# Mom and Dad
#
# Given a string, RETURN True if the continous substring 'mom' appears the same number of times
# as the continous substring 'dad'. Otherwise, RETURN false.
#
# The input will always be given as a lower case string. You do not have to worry about upper cases.
#
# Example(s)
# ----------
# Example 1:
#   Input: mom_and_dad('momdad')
#   We have the substring going from 'mom' and 'dad'. There is one each.
#
#   Output:
#   True
#
# Example 2:
#   Input: mom_and_dad('momomdad')
#   We have the string 'mom' from the first part of the string (mom omdad)
#   However, we have another occurance of 'mom' right after. (mo mom dad)
#   Next we only have 1 occurance of 'dad'.
#
#   Output:
#   False
#
# Parameters
# ----------
# string: String
#   String representing the sentence to find the number of occurances of 'mom' and 'dad'.
#   The string will always be given as a lowercase.
#
# Returns
# -------
# Bool
#   Boolean representing whether or not the same number of 'mom' and 'dad' occur in the string.
def mom_and_dad(string):
    """
    Given a string, RETURN True if the number of appearnces of 'mom' and 'dad' are the same.

    >>> mom_and_dad('momdad')
    True
    >>> mom_and_dad('momomdad')
    False
    >>> mom_and_dad('mom091213aiomomdadmomoomomomdadadfishsdadandwich')
    False
    >>> mom_and_dad('momomdadad')
    True
    """
    # Your code goes here!
    pass


if __name__ == "__main__":
    # Students can test this just by running the script
    # With the -v argument, they can find out the ones they got wrong.
    import doctest

    doctest.testmod()
