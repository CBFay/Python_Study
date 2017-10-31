# DefaultArgVal.py
# from Python 3.6.2 documentation
# created 10.02.2017 by CB Fay

# 4.7. More on Defining Functions
# 4.7.1. Default Argument Values

# This function can be called in several ways
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        # The 'in' keyword tests whether or not a sequence contains a certain value
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -=1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
# It has to be given 'prompt', but the other parameters have default values

# The default value is evaluated only once
# This makes a difference when the default is a mutable object
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
#This will print
#[1]
#[1, 2]
#[1, 2, 3]

# If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
def g(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
