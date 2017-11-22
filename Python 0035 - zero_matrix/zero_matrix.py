# If an element in an NxM matrix is 0, its entire row and column are set to 0
# From pg 91 of Gayle Laakman McDowell's "Cracking the Coding Interview"
# created 11.21.2017 by CB Fay

# O(NM)
def zero_matrix(matrix):
    zero_coordinates = []
    
    for N in range(0, len(matrix), 1):
        for M in range(0, len(matrix[0]), 1):
            if matrix[N][M] == 0:
                zero_coordinates.append((N,M))
                
    for coords in zero_coordinates:
        zero_cross(matrix, coords)
    
# O(M+N)  
def zero_cross(matrix, coordinates):
    for N in range(0, len(matrix), 1):
        matrix[N][coordinates[1]] = 0
        
    for M in range(0, len(matrix[0]), 1):
        matrix[coordinates[0]][M] = 0
        
# O(N)       
def print_matrix(matrix):
    for line in matrix:
        print(line)

        
# test case
myMatrix = [[1, 3, 4, 5, 8],    \
            [5, 3, 7, 1, 0],    \
            [3, 1, 2, 0, 9],    \
            [2, 3, 2, 5, 5],    \
            [6, 8, 7, 3, 2]]

zero_matrix(myMatrix)
print_matrix(myMatrix)
