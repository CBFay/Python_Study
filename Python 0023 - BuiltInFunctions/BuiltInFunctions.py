# BuiltInFunctions.py
# From Python 3.6.2 documentation
# created 10.03.2017 by CB Fay

x = 10

# returns the absolute value of a number
# if the argument is a complex number, its magnitude is returned.
abs(x)

# returns True if all elements of the iterable are True, or if the iterable is empty.
all(range(4))

# return True if any element in the iterable is true. If it's empty, return false.
any(range(5)) # range can be replaced with any iterable

# returns a string containing a printable representatoin of an object, but escape the non ASCII characters.
ascii(object)

# Convert an integer number to a binary string prefixed with '0b'. The result is a valid Python expression. If x is not a Python int object, it has to define an __index__() method that returns an integer.
bin(x)

# Other ways to accomplish this:
format(x, '#b')
format(x, 'b')
f'{x:#b}'
f'{x:b}'
# see format()

# class
# uses the standard 'truth testing procedure' to return a bool
bool([x])

# class
# return a new array of bytes
# the bytearray class is a mutable sequence of integers...
# ...in the range 0 <= x < 256
## bytearray([source[, encoding[, errors]]])

# class
# returns a new bytes object, which is an immutable version of bytearray.
## bytes([source[, encoding[, errors]]])

# Return the string representing a character whose Unicode code point is the integer i
# This is the inverse of ord().
# The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16)
chr(1000)

# returns the list of names in the current local scope
## dir([object])

# Convert an integer number to a lowercase hexadecimal string prefixed with “0x”. If x is not a Python int object, it has to define an __index__() method that returns an integer.
hex(x)

# Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime.
# This is the address of the object in memory!
id(x)

# If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that.
(input('type something! '))

# Return an integer object constructed from a number or string x, or return 0 if no arguments are given
int(x)

# Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).
y = 'hey'
print(len(y))

# Return the largest item in an iterable or the largest of two or more arguments.
max(iterable, *[, key, default])
max(arg1, arg2, *args[, key])
