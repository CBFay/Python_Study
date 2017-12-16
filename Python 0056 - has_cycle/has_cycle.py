# created 12.16.2017 by CB Fay

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    seenbefore = set()
    node = head
    while node != None:
        if node in seenbefore:
            return True
        else:
            seenbefore.add(node)
            node = node.next
    return False
