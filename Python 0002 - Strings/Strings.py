# Strings.py
# from Python 3.6.2 documentation
# created 09.27.2017 by CB Fay

# .format
x = "Hello"
y = "Dave"

print("{}, {}!".format(x, y))
print()

# SPECIAL CHARACTERS
# doing power operations is easy in Python
base = 2
exp = 4
result = base**exp

# Use a special character to get a single quote
print("It\'s very easy to do power calculations in Python")
print("{} to the power of {} is {}.".format(base, exp, result))
print()

# RAW STRINGS
# sometimes you don't want \ to refer to a special character
print('C:\some\name')

# insert r before quotes to avoid this problem
print(r'C:\some\name')
print()

# triple quotes can make String literals span multiple lines
print("""\
Usage: thingy [OPTIONS]
  -h  display this usage message
  -H  Hostname to connect to
""")
# End of lines are automatically included in the string
# However, adding a \ at the end of a line prevents this
print()

# CONCATENATION
# 3 times 'un', followed by 'ium'
word = 3 * 'un' + 'ium'
print(word)
print()

#Two or more string literals next to eachother are automatically concatenated
print('py' 'thon')
# This only works with two literals, not with variables or expressions:
print()

# If you want to concatenate variables or a variable and a literal, use +
prefix = 'py'
prefix += 'thon'
print(prefix)
print()

# the auto concatenation feature is helpful when you want to break long strings:
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
print()

# INDICES (INDEX)
# There are no chars in Python. A character is a string of size one:
word = 'Python'
print(word[0])
print(word[1])
print()

# Indices may also be negative numbers, to start counting from the right
print(word[-1])
print(word[-2])
print()

# Python supports slicing, which allows you to obtain substring
print(word[0:2]) # notice how the start is included while the end is excluded
print(word[2:6]) # this makes sure that s[:i] + s[i:] is always equal to s
print()

# Slice indices have useful defaults
# An omitted first index defaults to 0
# An omitted second index defaults to the size of the string being sliced
print(word[:2]) # characters from the beginning to position 2(excluded)
print(word[4:]) # characters from position 4 (included) to the end
print(word[-2:]) # characters from the second-last (included) to the end
print()

# this would result in an error: print(word[42])
# However, out of range slice indexes are handled gracefully when used for slicing
print(word[4:42])
print(word[42:]) # produces an empty string
print()

# Python strings cannot be changed - they are immutable
# This would result in an error: word[0] = 'J'
# If you need a different string, you should create a new one:
word2 = 'J' + word[1:]
print(word2)
print()

# BUILT IN FUNCTIONS
# The built in function len() returns the length of a string:
s = 'supercalifragilisticexpialidocious'
print(len(s)) # notice the parenthetical syntax
print()
