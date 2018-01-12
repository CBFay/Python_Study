# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# The basis for an iterative method of detecting prime numbers
# Updated on 01.12.2018 by CB Fay

from math import sqrt

class sieve_set:
    def __init__(self, n):
        self.composites = set()
        for p in range(2, int(sqrt(n))):
            if p in self.composites:
                continue
            for multiple in range(p, (n // p)+1):
                self.composites.add(multiple*p)

class sieve_list:
    def __init__(self, n):
        self.prime = [False, False] + [True] * (n-1)
        for p in range(2, int(sqrt(n))):
            if not self.prime[p]:
                continue
            for multiple in range(p, (n // p)+1):
                self.prime[multiple*p] = False
