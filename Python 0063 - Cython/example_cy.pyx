# Same functionality as example_py.py, but uses Cython type declarations

cpdef int test(int x):
    cdef int y = 0
    cdef int i
    for i in range(x):
        y += 1
    return y
