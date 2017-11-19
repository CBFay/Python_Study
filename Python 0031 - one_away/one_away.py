# Determine whether one string can be identical to another with...
# ...a one character insert, removal, or replacement.
# From pg 91 of Gayle Laakman McDowell's "Cracking the Coding Interview"
# created 11.19.2017 by CB Fay

def one_away(a,b):
    if a == b:
        return True
    
    lenDif = abs(len(a) - len(b))
    if lenDif > 1:
        return False
    if lenDif == 1:
        return(can_insert(a,b))
    if lenDif == 0:
        return(can_replace(a,b))
    
    
def can_replace(a,b):
    charDif = 0
    
    for i in range(0, len(a), 1):
        if a[i] != b[i]:
            charDif += 1
            if charDif > 1:
                return False
    return True


def can_insert(a,b):
    if len(a) < len(b):
        a,b = b,a # swap
        
    for i in range(0, len(b)-1, 1):
        if b[i] != a[i] and b[i+1] != a[i]:
            return False
    return True

