# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem 
# Created on 12.13.2017

def number_needed(a, b):
    """Return the minimum number of chracter deletions
    necessary to make two strings anagrams.
    """
    char_balance = [0]*26
    for char in a:
        char_balance[ord(char)-97] += 1
    for char in b:
        char_balance[ord(char)-97] -= 1
    steps = 0
    for i in char_balance:
        steps += abs(i)
    return steps

a = input().strip()
b = input().strip()

print(number_needed(a, b))


    
