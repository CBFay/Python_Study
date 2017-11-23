# decorators.py
# Demonstration of Decorators in Python
# From a stackabuse.com article on Python Properties
# Created on 11.23.2017 by CB Fay

def some_func():
    print 'Hey, you guys'
    
# Python functions can take other functions as parameters    
def my_decorator(func):
    def inner():
        print 'Before func!'
        func()
        print 'After func!'
     
    # Python functions can return functions
    return inner

print 'some_func():'
some_func()

print ''

# In Python, variables can store functions
some_func_decorated = my_decorator(some_func)

print 'some_func() with decorator:'

some_func_decorated()
