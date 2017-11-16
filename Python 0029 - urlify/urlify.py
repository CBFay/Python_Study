# Replace spaces with '%20'
# From pg 90 Gayle Laakman McDowell's "Cracking the Coding Interview"
# created 11.15.2017 by CB Fay

def urlify(str, truelen):
	spaces = 0
	
	for i in range(0, truelen-1, 1):
		if str[i] == ' ':
			spaces += 1
	
	i = truelen-1
	j = len(str)-1
	
	while spaces > 0:
		if str[i] == ' ':
			
			str[j] = '0'
			str[j-1] = '2'
			str[j-2] = '%'
			
			j -= 3
			i -= 1
			spaces -= 1
			
		else:
			str[j] = str[i]
			i -= 1
			j -= 1

			
# the string we want to operate on			
phrase = 'for the birds    '

# copy phrase into a list
phraselist = []
for letter in phrase:
	phraselist.append(letter)

# print the results of the function call	
urlify(phraselist, 13)
for letter in phraselist:
	print(letter, end='')