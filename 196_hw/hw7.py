################################################################################
#   Node Class
#   Is a class representing a single node of the linked list. String together
#   nodes to make a linked list.
#   self.data is a variable holding the data value
#   self.next is a variable that holds the pointer to the next node.
#
################################################################################


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


################################################################################
#                                                                              #
#       HOMEWORK 7 PROBLEMS                                                    #
#                                                                              #
################################################################################

# ITERATE
#
# Given the head of a linked list, iterate through the linked list and print the
# values.
#
# Note: THIS IS A COMPLETED EXAMPLE FOR YOU
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE
#   OUTPUT:
#       1, 2, 3, 4
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
#
# Returns
# -------
#   None, prints values
#
def iterate(head):
    pass

# REVERSE
#
# Given the head of a linked list, return a linked list that is reversed.
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE
#   OUTPUT:
#       HEAD -> 4 -> 3 -> 2 -> 1 -> NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#  
#
# Returns
# -------
# head: node
#   Head of the reversed linked list
def reverse(head):
    pass

# SKIP
#
# Given the head of a linked list, return a linked list with every other node
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE
#   OUTPUT:
#       HEAD -> 1 -> 3 -> NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
#
# Returns
# -------
# head : node
#   Head of a linked list with every other node
def skip(head):
    pass

# TAIL
#
# Given the head of a linked list and an int, append a node with the int data to
# the tail of the linked list
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE, 5
#   OUTPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> 5 -> NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
# n : int
#   data for the tail node
#
# Returns
# -------
# head : node
#   Head of a linked list with the data node appended to the tail
def add_tail(head, n):
    pass

# HEAD
#
# Given the head of a linked list and an int, append a node with the int data to
# the head of the linked list
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE, 5
#   OUTPUT:
#       HEAD -> 5 -> 1 -> 2 -> 3 -> 4 -> NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
# n : int
#   data for the head node
#
# Returns
# -------
# head : node
#   Head of a linked list with the data node appended to the head
def add_head(head, n):
    pass

# ADD
#
# Given the head of a linked list, an int : data and an int : i, add a node with
# int : data to the i'th position in the linked list
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE, 5, 3
#   OUTPUT:
#       HEAD -> 1 -> 2 -> 3 -> 5 -> 4 ->  NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
# data : int
#   data for the tail node
#
# i : int
#   position of the new node
#
# Returns
# -------
# head : node
#   Head of a linked list with the data node in the i'th position of the linked
#   list
def add_position(head, data, i):
    pass

# DELETE
#
# Given the head of a linked list, an int : i, delete the i'th node in the
# linked list and return the new linked list.
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> NONE, 3
#   OUTPUT:
#       HEAD -> 1 -> 2 -> 3 ->  NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
# i : int
#   position of the node to delete
#
# Returns
# -------
# head : node
#   Head of a linked list with the node in the i'th position of the linked list
#   deleted
def delete(head, i):
    pass

# DELETE_DUPLICATE
#
# Given the head of a linked list, delete all consecutive duplicate nodes in the
# linked list. Only consider CONSECUTIVE duplicates.
#
#
# Example(s)
# ----------
# Example 1:
#   INPUT:
#       HEAD -> 1 -> 2 -> 2 -> 3 -> 4 -> 2 -> NONE
#   OUTPUT:
#       HEAD -> 1 -> 2 -> 3 -> 4 -> 2 -> NONE
#
#
# Parameters
# ----------
# head : node
#   Head of a linked list
#
# Returns
# -------
# head : node
#   Head of a linked list with the node with consecutive duplicates deleted.
def deleteDuplicate(head):
    pass
