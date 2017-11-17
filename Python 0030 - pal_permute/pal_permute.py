# Determine whether a string is a permutation of a palindrome
# From pg 90 Gayle Laakman McDowell's "Cracking the Coding Interview"
# created 11.16.2017 by CB Fay

def pal_permute(str):
	
	odd = 0 # odd numbered characters allowed
	letters = len(str) # amount of true characters
	list = [0] * 128 # stores character frequency
	
	for x in str:
        list [char_num(x)] += 1 
		if x == ' ': # consider spaces
			letters -= 1

	if letters % 2 != 0:
		odd = 1 
		
	for x in str:
		if list[char_num(x)] % 2 != 0: 
			odd -= 1
		if odd < 0:
			return False
			
	return True
	
def char_num(character):
return ord(character.lower()) # consider uppercase
