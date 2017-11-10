# Study on eliminating unnecessary work
# From pg 68 Gayle Laakman McDowell's "Cracking the Coding Interview"
# created 11.10.2017 by CB Fay
 
# O(n^3)
def printPairs(n):
	"""Print values of a,b,c,d where (a**3 + b**3 = c**3 + d**3)."""
	num = 0
	for a in range(1,n):
		for b in range(1,n):
			for c in range(1,n):
				A = a**3;
				B = b**3;
				C = c**3;
				if (A + B - C) > 0: # this is necessary to avoid complex numbers
					d = int((A + B - C)**(1/3)) # there i only one valid d value for each (a,b,c)
				else: continue
				if a**3 + b**3 == c**3 + d**3 and d <= n:
					num += 1
					print(num, end="\t")
					print("{},{},{},{}".format(a,b,c,d))
				
# O(n^2)
def printPairs2(n):
	"""Print values of a,b,c,d where (a**3 + b**3 = c**3 + d**3)."""
	map = {} # a dictionary that holds all of the possible c**3 + d**3 combinations
	num = 0 # a count of solutions found
	for c in range(1,n):
		for d in range(1,n):
			result = c**3 + d**3; 
			map[result] = c, d # appends the pair (c, d) at key result
	for a in range(1,n):
		for b in range (1,n):
			result = a**3 + b**3
			list = [] # create an empty list
			list.append(map[result]) # add all of the pair values at key result to the list
			for pair in list: # print each element in the list. These are necessarily correct values of a and b
				num += 1 
				print(num, end="\t")
				print(a, b, pair[0], pair[1], end=" ")
				print("\t= {}".format(a**3 + b**3))

# O(n^2)
def printPairs3(n):
	"""Print values of a,b,c,d where (a**3 + b**3 = c**3 + d**3)."""
	map = {} # a dictionary that holds all of the possible c**3 + d**3 combinations
	num = 0 # the count of combinations of a,b,c,d values that make the statement true
	for c in range(1,n): # start at 1, end with 999
		for d in range(1,n):
			result = c**3 + d**3
			map.setdefault(result, []) # check for the key result, and if it doesn't exist, calling it will return an empty list.
			map[result].append((c,d)) # appends a tuple (c,d) to the end of the single list held as a value to the key result
			
	for keys in map: # for every possible outcome of c**3 + d**3...
		for pair1 in map[keys]: # each value (list of tuples) in map gets assigned to pair1
			for pair2 in map[keys]: # each value (list of tuples) in map gets assigned to pair2
				num += 1 # increment the count
				print(pair1, pair2)
				
				# print(num, end = "\t")
				# print(pair1, pair2, end = "\t")
				# print("a**3 + b**3 =",end = " ")
				# print(pair1[0]**3 + pair1[1]**3)
				
def main():
	printPairs3(1000)

if __name__ == "__main__":
	main() 
			