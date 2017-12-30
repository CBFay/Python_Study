# Detect IPv4 and IPv6 addresses in a list
# Created 12.01.2017 by CB Fay

def checkIPs(ips):
	"""Return a list of strings
	corresponding to the IP address type
	of addresses in the given list.
	"""
	results = []
	for i in ips:
		if isIPv4(i):
			results.append('IPv4')
		elif isIPv6(i):
			results.append('IPv6')
		else:
			results.append('Neither')
	return results
	
	
def isIPv4(strng):
	"""Determine if a string is an IPv4 address"""
	a = 0
	b = 0
	segments = 0
	while a < len(strng):
		segments += 1
		if segments > 4: 
			return False # wrong size
		while b < len(strng) and strng[b] != '.':
			b += 1
		if not strng[a:b].isdigit() or int(strng[a:b]) > 255: 
			return False # wrong values
		b += 1
		a = b
	return True	

	
def isIPv6(strng):
	"""Determine if a string is an IPv6 address"""
	hexdigits = set('0123456789abcdefABCDEF')
	a = 0
	b = 0
	segments = 0
	while a < len(strng):
		segments += 1
		while b < len(strng) and strng[b] != ':':
			if strng[b] not in hexdigits:
				return False # wrong values
			if (b - a) > 4 or segments > 8: 
				return False # wrong size
			b += 1
		b += 1
		a = b
	return True	
