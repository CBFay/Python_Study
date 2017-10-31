# Statistics.py
# demonstrate a useful built in module
# created 10.02.2017 by CB Fay

import statistics

example_list = [3,4,6,2,7,9,5,3,3]

# average
x = statistics.mean(example_list)
print('mean is', x)

# median
x = statistics.median(example_list)
print('median is', x)

#
x = statistics.mode(example_list)
print('mode is', x)

# standard deviation
x = statistics.stdev(example_list)
print('standard deviation is', x)

# variance
x = statistics.variance(example_list)
print('variance is', x)
