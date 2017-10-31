# FunctionAnnotations.py
# From Python 3.6.2 documentation
# created 10.03.2017 by CB Fay

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

print(f('spam'))
