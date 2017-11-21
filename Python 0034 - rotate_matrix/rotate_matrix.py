# Rotate a two dimensional list 90 degrees
# From pg 91 of Gayle Laakman McDowell's "Cracking the Coding Interview"
# created 11.21.2017 by CB Fay

def rotate_matrix(matrix):
    halfway = len(matrix)/2

    for y in range(0,halfway,1):
        for x in range(0,halfway,1):
          
            # storing these Y,X pairs allows for in place rotation
            a = [x, y]
            b = counterclock90([ a[0], a[1] ])
            c = counterclock90([ b[0], b[1] ])
            d = counterclock90([ c[0], c[1] ])

            # in place rotation
            matrix[a[0]][a[1]], \
            matrix[b[0]][b[1]], \
            matrix[c[0]][c[1]], \
            matrix[d[0]][d[1]]  \
            =   \
            matrix[b[0]][b[1]], \
            matrix[c[0]][c[1]], \
            matrix[d[0]][d[1]], \
            matrix[a[0]][a[1]]

   
def counterclock90(YX):
    return [YX[1], 3-YX[0]]

def clockwise90(YX):
    return [3-YX[1], YX[0]]


# test case
myMatrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
rotate_matrix(myMatrix)
print(myMatrix)

