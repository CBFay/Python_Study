# Import.py
# Demonstrate proper syntax for importing and referencing modules
# created 10.02.2017 by CB Fay

# allows you to reference the statistics module without having to type its name each time you call it
import statistics as s

# this allows you to reference items within a module without having to use the dot operator
# you can import multiple items simultaneously
from statistics import mean, median

# 'from' and 'as' can be used in conjunction like this:
from statistics import mode as m, stdev as d

# we can import everything contained in a module
# use this if you want to call the functions without having to say 'statistics.'
from statistics import *

numbers = [1,2,3,4,4,5,6,7,8,9,0,]
print(s.variance(numbers))
print(mean(numbers))
print(d(numbers))
