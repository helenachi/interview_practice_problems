################################################################################
#
#   Node Class
#   Is a class representing a single node of the linked list. String together
#   nodes to make a linked list.
#   self.data is a variable holding the data value
#   self.next is a variable that holds the pointer to the next node.
#
################################################################################


class linked_node(object):
    # Node class for linked list implementation
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class tree_node(object):
    # Node class for BST implementation
    def __init__(self, data=None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


################################################################################
#                                                                              #
#       HOMEWORK 8 PROBLEMS                                                    #
#                                                                              #
################################################################################

# Merge
#
# Given the head of two linked lists, return true if the linked lists merge,
# and false if they do not merge.
#
# Example(s)
# ----------
# Refer to class notes on linked lists!
#
# Parameters
# ----------
# head_a : node
#   Head of a linked list
#
# head_b : node
#   Head of another linked list
#
#
# Returns
# -------
#   Boolean
#
def isMerged(head_a, head_b):
    pass

# Find Merge Point
#
# Given the head of two linked lists that are merged, return the data at the 
# node where the two lists merge.
#
# Example(s)
# ----------
# Refer to class notes on linked lists!
#
# Parameters
# ----------
# head_a : node
#   Head of a linked list
#
# head_b : node
#   Head of another linked list
#
# Returns
# -------
# int: data
#   data at merge node
def findMerge(head_a, head_b):
    pass

# Cycle
#
# Given the head of a linked list, find out whether or not there is a cycle.
#
#
# Example(s)
# ----------
# Refer to class notes on linked lists!
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
#
# Returns
# -------
# boolean :
#   True if there is a cycle, False if there is not
def foundCycle(head):
    pass


# Find Odd
#
# Given the head node of a BST, return all odd data members of nodes in the 
# tree in a list. Duplicates must be considered. Order does not matter.
#
#
# Example(s)
# ----------
# Input (tree representation):
#   head: node
#
#            3
#          /   \
#         2     5
#        / \   / \
#       4   3 8   7
#
# Output:
#   odds: list
#   [3,5,3,7]
#
#
# Parameters
# ----------
# head : node
#   Head of a BST
#
#
# Returns
# -------
# odds : list
#   list of odd data members in the tree
def findOdd(head):
    pass

# Find Median
#
# Given a stream of integers, find the new median after every iteration.
# You are given a class that emulates a stream. The insertDataFindMedian method
# represents a single output of the stream into your data structure. After 
# every call of this method, return the new median. In other words, you should 
# be modifying the functionality of the insertDataFindMedian method. To test, 
# instantiate an object of the median class and call the insertDataFindMedian 
# method multiple times.
#
#
# Example(s)
# ----------
# See class notes on heaps!
#
# Parameters
# ----------
# newNumber : double
#
# Returns
# -------
# median : double
#   new median
class median(object):
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def insertDataFindMedian(self, newNumber):
        # Takes an int number and adds it to the object. Every instance of this method being called
        # emulates a a new integer coming from a "stream". Return the median after each time this method
        # is called.
        pass
