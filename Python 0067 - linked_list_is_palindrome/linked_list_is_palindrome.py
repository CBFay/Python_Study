# Determine if a Linked List is a Palindrome
# Created 1.16.2018 by CB Fay

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
def LLisPal(root):
    stack = []
    slow = root
    fast = root
    while(fast != None and fast.next != None):
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    if fast != None:
        slow = slow.next
    
    while len(stack) > 0:
        if stack.pop() != slow.data:
            return False
        slow = slow.next
    return True
