# Compress a string with repeating characters
# From pg 91 of Gayle Laakman McDowell's "Cracking the Coding Interview"
# created 11.20.2017 by CB Fay

def string_compress2(subject):
    
    compressed = []
    consecutive = 0
    for i in range(0, len(subject), 1):
        consecutive += 1
        
        if i + 1 == len(subject) or subject[i] != subject[i+1]:
            compressed.append(subject[i])
            compressed.append(str(consecutive))
            consecutive = 0
    
    if len(compressed) < len(subject):
        return ''.join(compressed)
    return subject

print(string_compress2("aaabbcccc"))