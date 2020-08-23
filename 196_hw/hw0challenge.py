################################################################################
### Eric Lee
### ericdl2
################################################################################
# Let's say there exists some alien language. You have a number of sorted
# strings in this language. Figure out the ordering of letters in this alphabet.
#
# English Example:
#           ACE, MOZ, ACDEM
#   Order:
#           A -> C -> D -> E -> M -> O -> Z
# English Example:
#           "ACE", "MOZ", "ACDEM", "ACODZ"
#   Order:
#           A -> C -> D -> E -> M -> O -> Z
################################################################################
# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def reverse_alphabet(list_of_words):
    pass


def word_to_linked_list(word):
    if not word or word == "":
        return None
    head = Node(word[0])
    temp = head
    for c in word[1:]:
        temp.next = Node(c)
        temp = temp.next
    return head


def print_linked_list(head):
    result = str(head.data)
    temp = head.next
    while temp:
        result += " -> "
        result += str(temp.data)
        temp = temp.next
    print(result)


if __name__ == "__main__":
    print_linked_list(word_to_linked_list("bitch"))
