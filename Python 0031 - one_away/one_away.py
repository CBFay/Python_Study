# three operations: insert, delete, replace
def one_away(A,B):
    
    lenDif = abs(len(A) - len(B))
    if lenDif > 1:
        print("lenDif is too big")
        return False
    
    a = list(A)
    b = list(B)
    
    if lenDif == 0:
        return(can_replace(a,b))
    
    if lenDif == 1:
        return(can_insert(a,b))
    
    
def can_replace(a,b):
    charDif = 0
    
    for i in range(0, len(a), 1):
        print(charDif)
        if a[i] != b[i]:
            charDif += 1
            if charDif > 1:
                print("can't replace")
                return False
    print("can replace")
    return True
    
def can_insert(a,b):
    if len(a) > len(b):
        big = a
        small = b
    else:
        big = b
        small = a
        
    for i in range(0, len(small)-1, 1):
        if small[i] != big[i] and small[i+1] != big[i]:
            print("can't insert/delete")
            return False
    print("can insert/delete")
    return True
    
one_away('hello', 'helo')

# hlo
# halo
# hllo
# hello
# ello
# helo
