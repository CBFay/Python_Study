# ControlStatements.py
# from Python 3.6.2 documentation
# created 09.29.2017 by CB Fay

# 4.1 IF STATEMENTS
x = int(input('Please enter an integer: '))
if x < 0:
    X = 0;
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
# an if...elif sequence is a substitute for the switch statement
print()

# 4.2 FOR STATEMENTS
# Python's for statement interates over the items of any sequence...
# ...(a list or a string), in the order that they appear in the sequence
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
print()

for w in words[:]: # Loop over a slice copy of the entire list
    if len(w) > 6:
        words.insert(0, w)
print(words)
# With 'for w in words:', the example would attempt to create an infinite list...
# ...inserting 'defenestrate' over and over again
print()

# 4.3 THE 'range()' FUNCTION
# If you do need to iterate over a sequence of numbers, the build in function...
# ...range() comes in handy. It generates arithmetic progression
for i in range(5):
    print(i)
# The given end point is never part of the generated sequence.
print()

# It is possible to let the range start at another number, or to specify...
# ...a different increment (even negative; sometimes this is called the 'step')
for i in range(5,10): # prints 5-9
    print(i, end=' ')
print()

for i in range(0,10,3): # count to 10 in increments of 3, starting at 0
    print(i, end=' ')
print()

for i in range(100,0,-5): # count from 100 to 0 in increments of -5
    print(i, end=' ')
# Remember that the target value will be excluded
print('\n')

# To iterate over the indices of a sequence you can combine 'range()' and 'len()'
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
print()

# the object returned by 'range()' behaves like a list, but isn't.
print(range(10))
# such an object is described as 'iterable', that is suitable as a target...
# ...for functions and constructs that expect something from thich they can...
# ...obtain successive items until the supply is exhausted.
print()

# the function 'list()' is another 'iterator'. It creates lists from iterables
print(list(range(5)))
print(list(a))
b = list(a)
print(b)
print()

# 4.4 BREAK AND CONTINUE STATEMENTS, AND ELSE CLAUSES ON LOOPS
# The break statement breaks out of the smalles enclosing for or while loop
# break and else are demonstrated in this loop that finds prime numbers
for n in range(2,10): # for every value between 2(inc) and 10(exc)...
    for x in range(2,n): # check every value up to the value being factored (n)
        if n % x == 0: # if x is a factor of n...
            print(n, 'equals', x, '*', n//x) # print non-prime proof
            break # break the for x loop, go back into the for n loop
    else: # if the loop was completed (not broken)
        # loop fell through without finding a factor
        print(n, 'is a prime number')
print()

# The continue statement continues with the next iteration of the loop:
for num in range(2, 10):
    if num % 2 == 0:
        print('Found an even number', num)
        continue
    print('Found an odd number', num)
print()

# 4.5 PASS STATEMENTS
# The pass statement does nothing. It can be used when a statement...
# ...is required syntactically but the program requires no action.

# while True:
     # pass # Busy-wait for keyboard interrupt (CTRL+C)

# This is commonly used for creating minimal classes
class MyEmptyClass:
    pass

# Pass can also be used as a placeholder for a function or conditional body...
# ...when you are working on new code, allowing you to keep thinking at a...
# ...more abstract level
def initlog(*args):
    pass # remember to implement this!

# 4.6 DEFINING FUNCTIONS
def fib(n):
     """Calculates and prints the nth Fibonacci number""" # docstring
     a, b = 0, 1 # multiple assignment
     for i in range(n+1): # +1 because n would be excluded
        a, b = b, a+b # multiple assignment does calculation before assignment
        print('Fibonacci #', i, ':', a) # I wonder how you can exclude the spaces

fib(100) # tells you the 100th Fibonacci number
# the keyword 'def' introduces a function definition.
# It must be followed by the function name and the parenthesized...
# ...list of formal parameters. The statements that form the body of the...
# ...function start at the next line, and must be indented
# The first statement of the function body can optionally be a string literal;
# This string literal is the function's documentation string, or docstring
# It's good practice to include docstrings in code that you write

# All variables values in a function are stored in a 'local symbol table'?
# Global variables cannot be directly assigned a value within a function...
# ...unless named in a global statement, although they may be referenced.
# 'None' in Python is synonymous with 'void' in Java/C?
