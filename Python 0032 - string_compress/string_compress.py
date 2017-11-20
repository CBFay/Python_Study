# Compress a string with repeating characters
# From pg 91 of Gayle Laakman McDowell's "Cracking the Coding Interview"
# created 11.19.2017 by CB Fay

def string_compress(subject):
        compressed = []
        index = 0
        
        while index < len(subject)-2:
            
            if subject[index] == subject[index+1]:
                
                blocksize = repeat_block(subject, index)
                compressed.append(subject[index] + str(blocksize))
                index += blocksize
                
            else:
                compressed.append(subject[index])
                index += 1
            
        if len(compressed) < len(subject):
            return ''.join(compressed)
         
        return subject

    
def repeat_block(info, loc):
    findme = info[loc]
    consecutive = 2
    loc += 2
    
    while info[loc] == findme:
        consecutive += 1
        loc += 1
        
    return consecutive
