# ListManipulation.py
# created 10.02.2017 by CB Fay

x = [1,4,23,7,9,7,5,3,4,6,4,2,26,22,6,7]
print(x)

x.append(2) # add information to the end of a list
print(x)

x.insert(0, 100)
print(x)

x.remove(4)
print(x)

# this works too
x.remove(x[2])
print(x)

print(x[5])

# accessing lists with slicing
print(x[5:9])

print(x[-1])

print(x.index(1))

# how many 6s are in the list?
print(x.count(6))

#sorting
x.sort()
print(x)

# strings are sorted alphabetically
y = ['janet', 'alan', 'bob', 'gary']
y.sort()
print(y)
