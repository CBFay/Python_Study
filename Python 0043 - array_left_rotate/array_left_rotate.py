# Perform leftward rotation on a list
# Created 12.04.2017 by CB Fay

def array_left_rotation(a, n, k):
    return (a[k%n:] + a[:k%n])
  
  
# n: the number of elements
# k: the number of left rotations
# a: the list

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
