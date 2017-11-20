# Compress a string with repeating characters
# From pg 91 of Gayle Laakman McDowell's "Cracking the Coding Interview"
# created 11.20.2017 by CB Fay

def string_compress2(subject):
    finalLength = compress_len(subject)
    if finalLength >= len(subject):
        return subject
    
    compressed = [] * finalLength
    consecutive = 0
    for i in range(0, len(subject), 1):
        consecutive += 1
        
        if i + 1 == len(subject) or subject[i] != subject[i+1]:
            compressed.append(subject[i])
            compressed.append(str(consecutive))
            consecutive = 0
    
    return ''.join(compressed)


def compress_len(info):
    size = 0
    consecutive = 0
    
    for i in range(0, len(info), 1):
        consecutive += 1
        
        if i + 1 >= len(info) or info[i] != info[i+1]:
            if consecutive > 1:
                size += 2
            else:
                size += 1

    return size

print(string_compress2("aaabbcccc"))