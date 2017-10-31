# Fibonacci.py
# from Python 3.6.2 documentation
# The sum of two elements defines the next
# created 09.28.2017 by CB Fay

a, b = 0, 1 # this is called a 'multiple assignment'

while b < 1000:
    # the keyword argument 'end' can be used to avoid the newline...
    # ...after the output, or end the output with a different string
    print(b, end=', ')

    a, b = b, a+b
    # the expressions on the right side are all evalluated first...
    # ...before any of the assignments take place

    # in python, any non-zero integer is true; zero is false.
