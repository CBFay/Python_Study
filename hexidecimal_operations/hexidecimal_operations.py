
# hexidecimal_operations.py
# Useful base manipulations on numeric strings
# Created on 12.03.2017 by CB Fay

# !These lines are extremely important!
octdigits = set('01234567')
bindigits = set('01')

def is_hexidecimal(number):
	"""Return True if a string is hexidecimal"""
	hexdigits = set('0123456789abcdefABCDEF')
	for digit in number:
		if digit not in hexdigits:
			return False
	return True


# Converting numeric strings to different bases
a = 'FF'
a = '{0:b}'.format(int(a,16)) # convert a hexidecimal string to binary
# a == '11111111'
a = '{0:o}'.format(int(a,2)) # convert a binary string to octal
# a == 377
a = '{0:d}'.format(int(a,8)) # convert an octal string to decimal 
# a == '255'
