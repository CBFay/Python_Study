# https://www.hackerrank.com/challenges/ctci-ransom-note/problem
# Created 12.14.2017 by CB Fay

def ransom_note(magazine, ransom):
    """Return True if a magazine contains a counterpart
    for every word in a ransom message."""
    words = dict()
    for x in magazine:
        if x in words:
            words[x] += 1
        else:
            words[x] = 1
    for y in ransom:
        if y in words and words[y] > 0:
            words[y] -= 1
        else:
            return False
    return True        

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')

if m < n:
    print("No")
elif(ransom_note(magazine, ransom)):
    print("Yes")
else:
    print("No")
