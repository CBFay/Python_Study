# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# The basis for an iterative method of detecting prime numbers
# Created on 01.07.2018 by CB Fay

class sieve:
    def __init__(self, n):
        self.composites = set()
        for p in range(2, n):
            if p in self.composites:
                continue
            for multiple in range(2, n//p):
                self.composites.add(multiple*p)
                
