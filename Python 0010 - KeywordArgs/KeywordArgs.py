# KeywordArgs.py
# from Python 3.6.2 documentation
# created 10.02.2017 by CB Fay

# 4.7.2. Keyword Arguments
# Functions can also be called using Keyword arguments of the form 'kward=value'
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# you can call this function in many ways
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
# the order of the arguments is irrelevant if you call define them all by name
# arguments without keywords are called positional
# keyword arguments MUST follow positional arguments
# No argument may receive a value more than once

# When a final formal parameter of the form **name is present, it receives a dictionary containing all keyword arguments except for those corresponding to a formal parameter
# This may be combined with a formal parameter of the form *name which receives a tuple containing the positional arguments beyond the formal parameter list
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords: # kw refers to entries in the dictionary
        print(kw, ":", keywords[kw]) # this delivers the value of each entry

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
# need to learn more about dictionaries
