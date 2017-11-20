# Experimentation with destructive list functions
# Created 11.20.2017 by CB Fay

def list_destruction():
    list = ['h', 'e', 'l', 'l', 'o']
    print(list)
    
    # O(n)
    del list[1] # deletes elements at an index
    print(list)
    
    # O(n)
    list.insert(1, 'f')
    print(list)
    
    list.remove('h') # deletes elements of a specific value
    print(list) # lists have this function, but not strings
    
    print(list.pop()) # returns an element, AND removes it
    print(list)
    
    list.insert(2, 'hey')
    list.insert(4, 'hi')
    print(list)
    
    list[1:4] = [] # use to clear portions of the list
    print(list)
    
    list[:] = []
    print(list)
    
    del list # list can no longer be referenced unless redefined
    # print(list)
    
list_destruction()
