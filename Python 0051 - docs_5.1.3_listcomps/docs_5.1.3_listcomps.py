# Review of Python documentation
# Created 12.13.2017 by CB Fay

# list comprehensions
squares = [x**2 for x in range(11)]
cubes = list(map(lambda x: x**3, range(11)))

print(squares)
print(cubes) 

uniques = [(x, y) for x in [1, 2, 3] for y in [3, 4, 5] if x != y]

print(uniques)

numbers = [3, 5, 7, 9]
doubles = [x*2 for x in numbers]
print(doubles)

manynumbers = [2, 4, 0, 5, 8, 2, 4, 6, 3, 0, 8]
print([x for x in manynumbers if x!= 0])

names = [
    'Amanda',
    'Ashley',
    'Bailey',
    'Jessica',
    'Allyson',
    'Miranda'
]
print([x for x in names if x[0] == 'A'])

def abs_vals(items):
    return [abs(x) for x in items]
print(abs_vals([-2, 8, -1, 1, 0, -5]))

def flattened(items):
    """Return a one dimensional list from a two dimensional list."""
    return [value for blocks in items for value in blocks]
print(flattened( [[1,2,3], [4, 5, 6], [7, 8, 9]] ))

# nested listcomps
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print([[row[i] for row in matrix] for i in range ( 3)])

# zip() returns an iterator of tuples, each of which contain the ith element from each argument
print(list(zip(*matrix)))
