# info_mask.py
# Mask client information to comply with business rules
# Created 12.01.2017 by CB Fay

"""This Program has been modified from its original format
to facilitate review."""

def info_mask():
    """Mask user information"""
    info = []
    result = []
    
    for x in range(1):
        try: 
            entry = "E:" + input("Enter an Email: ")
        except EOFError:
            break # until there is no more input...
        info.append(entry) # ... append lines to a list.
        
    for x in range(1):
        try: 
            entry = "P:" + input("Enter a Phone Number: ")
        except EOFError:
            break # until there is no more input...
        info.append(entry) # ... append lines to a list.
        
    for entry in info:
        if entry[0] == 'E':
            result.append(e_mask(entry))
        if entry[0] == 'P':
            result.append(p_mask(entry))

    for entry in result:
        print(entry) # final output

def e_mask(email):
	"""Mask email address"""
	masked = email[:3] + '*****'
	masked += email[email.index('@')-1:] # find the '@' and slice
	return masked
	
	
def p_mask(phone):
	"""Mask phone number"""
	masked = phone[:2]
	
	if phone[2] == '+': # only check elements if necessary
		masked += '+'
		i = 3
		while phone[i].isnumeric():
			masked += '*'
			i += 1
		masked += '-'
		
	masked += '***-***-' + phone[-4:]
	return masked
	

info_mask() # call solution function
