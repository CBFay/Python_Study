# docs_7.1_output_formats.py
# Review of Python documentation
# Created 12.24.2017 by CB Fay

import math

def format_demo():
    for x in range(1, 11):
        # the prefix to d represents the amount of right justifiation
        # everything following the : is called the 'format specifier'
        print('{0:2d} {1:3d} {2:4d} {3:5d}'.format(x, x**2, x**3, x**   4))
        # these curly braces are called 'format fields'.
        
def rjust_demo():
    for x in range(1, 11):
        print(repr(x).rjust(2), end = '')
        print(repr(x**2).rjust(4), end = '')
        print(repr(x**3).rjust(5), end = '')
        print(repr(x**4).rjust(6))
# str objects also have the methods ljust() and center()

def ljust_demo():
    for x in range(1, 11):
        for e in range(1,4):
            print(repr(x**e).ljust(e+2), end='')
        print()

def zfill_demo():
    for x in range(1,11):
        for e in range(1,4):
            print(repr(x**e).zfill(e+1), end=' ')
        print()

def pos_format():
    # these format fields use positional arguments
    print('We are the {0} who say {1}!'.format('tights', 'tea'))
    
def kw_format():
    # these format fields use keyword arguments
    print('This {food} is {adjective}!'.format(
        food='broccoli', adjective='horrible'))

def additional_formats():
    # {!a} applies ascii()
    # {!s} applies str()
    # {!r} applies repr()
    print('My hovercraft is full of {!r}!'.format('feels'))
    
def format_specifiers():
    # specify the number of decimal places used by a double
    print('The value of pi is approximately {0:.5}.'.format(math.pi))

def char_min():
    table = {
        'Jack' : 8673742827,
        'Jill' : 6284827284,
        'Giant' : 2173284237 }
    
    # following the : with an integer specifies a minimum char width
    for x in table:
        print('{:6} -> {:12}'.format(x, table[x]))
