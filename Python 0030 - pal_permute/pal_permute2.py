# Determine whether a string is a permutation of a palindrome
# From pg 90 Gayle Laakman McDowell's "Cracking the Coding Interview"
# created 11.17.2017 by CB Fay

def pal_permute2(str):
    odds = 0 # odd numbered characters
    frequencies = [0] * 128 # stores character frequency
    
    for x in str:
        if x != ' ': # ignore spaces
            frequencies[char_num(x)] += 1
            if frequencies[char_num(x)] % 2 == 1:
                odds += 1
            else:
                odds -= 1
    
    return odds <= 1


def char_num(character):
    return ord(character.lower()) # consider uppercase
