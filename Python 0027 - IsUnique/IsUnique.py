# Determine if a string has all unique characters without using additional data structures.
# From pg 90 Gayle Laakman McDowell's "Cracking the Coding Interview"
# created 11.13.2017 by CB Fay

def is_unique(str):
	if len(str) > 128:
		return False
		
	for i in range(0, len(str), 1):
		for j in range(i+1, len(str), 1):
			if str[i] == str[j]:
				return False
	return True
	
def main():
	print(is_unique("activate windows"))
	
if __name__ == "__main__":
	main()