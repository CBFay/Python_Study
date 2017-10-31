# GlobVars.py
# How to access and affect variables outside of frame/scope
# created 10.02.2017 by CB Fay

x = 6

def add5():
    global x # make x a global variable
    x += 5

add5()
print(x)

# how to affect 5 without making x global
def add5noglob():
    globx = x
    globx += 5

    return globx # assign x the return value outside of the function

x = add5noglob()
print(x)
