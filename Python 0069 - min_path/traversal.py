import sys

# Format input as an triangular matrix of Integers named "triangle"
with open(sys.argv[1]) as testcase:
    triangle = [[int(string) for string in line.strip('\n').split('  ')] \
           for line in testcase.readlines()]
    
def min_path(tri):
    """Hold a list of upward paths to the
    "root" of tri, continually pushing optimal
    paths leftward in the list."""
    
    # Create a list of paths from the bottom row of tri.
    paths = [[number] for number in tri[-1]]
    
    # left -> right, bottom -> top
    for row in reversed(range(len(tri))):
        for col in range(row):
            
            # Choose the better of the two adjacent (child) paths.
            if sum(paths[col+1]) <  sum(paths[col]):
                paths[col] = paths[col+1][:]
                
            # Append the parent value to the current path.    
            paths[col].append(tri[row-1][col])
    
    # Print each element (node) in the finalized leftmost path.
    for node in reversed(paths[0]):
        print(node)

if __name__ == '__main__':
    min_path(triangle)
