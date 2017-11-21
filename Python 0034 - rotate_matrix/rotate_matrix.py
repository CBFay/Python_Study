def rotate_matrix(matrix):
    for y in range(0,2,1):
        for x in range(0,2,1):
            
            a = [x, y]
            b = clockwise90([ a[0], a[1] ])
            c = clockwise90([ b[0], b[1] ])
            d = clockwise90([ c[0], c[1] ])

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

    print(matrix[0])
    print(matrix[1])
    print(matrix[2])
    print(matrix[3])

   
def clockwise90(YX):
    return [YX[1], 3-YX[0]]
    
myMatrix = [[0, 1, 2, 3], 
            [4, 5, 6, 7],
            [8, 9, 10, 11],
            [12, 13, 14, 15]]

rotate_matrix(myMatrix)

# [0][0] -> [0][1] +0,1
# [0][2] -> [2][3] +2,1
# [1][2] -> [2][2] +1,0
# [1][3] -> [3][2] +2,-1
