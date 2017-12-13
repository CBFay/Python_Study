# Review of Python documentation
# Created on 12.13.2017 by CB Fay

num = 5
t = 132, 'hello', num

# this is called sequence unpacking. 
x, y, z = t
print(x, y, z)

# tuples with one element are declared like this
singleton = "Notice the comma",
print(singleton[0])

# sequence unpacking on strings
letters = "ABCDEFG"
a, b, c, d, e, f, g = letters
print(a, b, c, d, e, f, g)
# multiple assignment is really just a combination of tuple packing and sequence unpacking.
