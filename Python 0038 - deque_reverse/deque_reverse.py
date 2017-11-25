# deque_reverse.py
# Personal implementations of deq.reverse()
# Created 11.25.2017 by CB Fay

from collections import deque

# reversal in place
def deque_reverse(deq):
    half = len(deq)/2 - 1
    
    for i in range(half, 0, -1):
        deq.rotate(i)
        swap1 = deq.pop()
        deq.rotate(-i)
        
        deq.rotate(-i)
        swap2 = deq.popleft()
        deq.rotate(i)
        
        deq.rotate(i)
        deq.append(swap2)
        deq.rotate(-i)
        
        deq.rotate(-i)
        deq.appendleft(swap1)
        deq.rotate(i)
    
    swap1 = deq.popleft()
    swap2 = deq.pop()
    deq.append(swap1)
    deq.appendleft(swap2)
    
    
# reversal by copy
def deque_reverse2(deq):
    reversed = deque()
    
    for i in deq:
        reversed.appendleft(i)

    return reversed

# a reversal that's almost in place
def deq_reverse3(deq):
    rev = deque()
    
    for x in range(len(deq)):
        rev.append(deq.pop())
    
    for x in range(len(rev)):
        deq.append(rev.popleft())
    
    del rev
