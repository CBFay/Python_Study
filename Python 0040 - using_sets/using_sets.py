# Significant features and applications of sets
# Created 11.29.2017 by CB Fay

# using_sets.py

# sets can be declared with the set() method
s = set([1,3,4,3]) # a set will not represent duplicate elements
# s == {1, 3, 4}

s.add(5) # elements can be added and removed
s.remove(4) # a KeyError will be raised if the element doesn't exist
# s == {1, 3, 4, 5}

fs = frozenset(s) # frozen sets are immutable
# fs == {1, 3, 5}

newset = {12, 50, 33} # sets can also be declared by just using curly brackets
newerset = newset.copy() # return a shallow copy
newerset = newset # this doesn't work. It just creates a pointer.
newset.clear() # remove all elements from a set
newerset.clear()

print('\ndifference()')
x = {'a', 'b', 'c', 'd', 'e'}
y = {'b', 'c'}
z = {'a'}
# O(len(x))
print(x.difference(y)) # find elements that occur in x but not in y
print(x.difference(y).difference(z)) # same thing, but not in z as well.
print(x - y - z) # cool way to do this with operators!


print('\ndifference_update()')
print(x)
print(y)
# O(len(y))
x.difference_update(y) # remove all elements of x that aren't in y
print(x)
print(z)
x -= z # again, operators work the same way
print(x)


print('\ndiscard()')
x.add('3')
x.add('v')
x.add('t')
print(x)
x.discard('v')
print(x)


print('\nother operators')
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
c = {2, 4, 3}
print('a : ', a)
print('b : ', b)
print('c : ', c)
print('a|b : ', (a|b))
print('a&b : ', (a&b)) # O(min(a,b)) Average Case
print('a^b : ', (a^b)) # O(len(a))
print('a<b : ', (a<b))
print('c<a : ', (c<a))
print('c<b : ', (c<b))

print('\npop()') # removes and returns 1 arbitrary set element
print('a : ', a)
print('a.pop() : ', a.pop()) # O(1)
print('a.pop() : ', a.pop())
print('a.pop() : ', a.pop())
print('a.pop() : ', a.pop())
print('a.pop() : ', a.pop())

print('\nx in s') # O(1) on average, O(n) worst case
s.add('f')
s.add(5)
s.add('dogs')
print(s)
print('\'dogs\' in s : ', 'dogs' in s)
print('\'cats\' in s : ', 'cats' in s)
