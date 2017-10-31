# Lists.py
# from Python 3.6.2 documentation
# created 09.28.2017 by CB Fay

# In Python, the list is a compound data type
squares = [1, 4, 9, 16, 25]
print(squares) # prints the entirety of the list squares
print()

# Like strings (and all other built-in sequence type) lists can be indexed and sliced
print(squares[0])
print(squares[-4])
print(squares[2:]) # slicing returns a new list
print()

# lists support operations like concatenation
squares += [36, 49, 64, 81, 100] # Unlike strings, lists are mutable
print(squares)
squares[7] = 150
print(squares)
squares.append(7**3) # the .append() method can be used to add new items to the end of the list
print(squares)
print()

# Assignment to slices is also possible
# This can change the size of a list or clear it entirely
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
# Removing items
letters[2:5] = []
print(letters)
# Clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)
print()

# The build in function len() also applies to lists:
letters = ['a', 'b', 'c', 'd']
print(len(letters))
print()

# It is possible to nest lists (create lists containing other lists)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])
print()
