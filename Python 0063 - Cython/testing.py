# Demonstrate performance gains with Cython

import timeit

cy = timeit.timeit('example_cy.test(1000)', setup='import example_cy', number=1000)

py = timeit.timeit('example_py.test(1000)', setup='import example_py', number=1000)

print(cy, py)
print("Cython is {}x faster".format(py/cy))
