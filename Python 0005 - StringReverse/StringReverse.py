# StringReverse.py
# Creates a string and copies its inverse into another
# created 09.29.2017 by CB Fay

origin, reverse = 'Hello!', ''
for i in range(len(origin)-1,-1,-1):
    reverse += origin[i]
print(reverse)
