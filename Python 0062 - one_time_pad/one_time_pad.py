# Encode and decode Strings with a one time pad
# Created on 12.30.2017 by CB Fay

from bitarray import bitarray
from random import randrange
import sys

def string_to_bits(s, pad, show=False):
    if pad < 8:
        pad = 8
    result = bitarray()
    block = '0' * pad
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '0' * (pad-len(bits)) + bits
        for b in bits:
            result.append(int(b))
    if show:
        print('Converting string to bits: ', s)
        print('Result is: ', result)
        print()
        
    return(result)

def randkey(l):
    key = ''
    ords = []
    for i in range(l):
        key += chr(randrange(256))
        ords.append(ord(key[-1]))
    return key

def encrypt(m, k, p):
    msg = string_to_bits(m, p, show=True)
    key = string_to_bits(k, p, show=True)
    return msg ^ key    
    
def decrypt(m, k, p):
    m = m ^ string_to_bits(k, p)
    result = ''
    i = 0
    while i < len(m):
        block = ''
        for n in range(p):
            block += str((int(m[i])))
            i += 1
        result += chr(int(block, 2))
        del(block)
    return result


# Demo
mypad = 8 
mymsg = 'encodeme'
mykey = randkey(len(mymsg))
ciphertext = encrypt(mymsg, mykey, mypad)

print('This is the ciphertext: ', ciphertext)
print()

plaintext = decrypt(ciphertext, mykey, mypad)

print('The original plaintext was: {}'.format(plaintext))
