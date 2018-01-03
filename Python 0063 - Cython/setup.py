# Run the following to compile the specified .pyx as C code
# python3 setup.py build_ext --inplace

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('example_cy.pyx'))
