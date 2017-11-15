# Determine if one string is a permutation of another
# From pg 90 Gayle Laakman McDowell's "Cracking the Coding Interview"
# created 11.14.2017 by CB Fay

# relatively fast and very readable
def check_permutation1(a, b):
	if len(a) != len(b):
		return False
		
	a = sorted(a)
	b = sorted(b)
	return a == b
		

# faster, but not very readable		
def check_permutation2(a, b):
	if len(a) != len(b):
		return False
	
	list = [0] * 128 
	for i in range(0, len(a), 1):
		list[ord(a[i])] += 1
		
	for i in range(0, len(b), 1):
		list[ord(b[i])] -= 1
		if list[ord(b[i])] < 0:
			return False
			
	return True
	
	
print(check_permutation1("checkme", "checkme"))
print(check_permutation2("checkme", "checkme"))