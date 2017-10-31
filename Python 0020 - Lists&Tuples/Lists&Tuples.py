# Lists&Tuples.py
# created 10.02.2017 by CB Fay

# Tuples are lists, but they are immutable
# Once they are defined, modules cannot be modified

# This is a tuple, because it is not enclosed by square brackets
x = 4,5,7,3,5
# This is another way to define a tuple
x = (4,5,7,3,5)
# Tuples are generated and iterated over faster than lists

#Tuples are useful if order needs to be rigid
def exampleFunc():
    return 15,6
x,y = exampleFunc()
