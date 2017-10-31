# Dictionaries.py
# created 10.02.2017 by CB Fay

# Dictionaries don't have inherent order
# They have 'keys' and 'values'

# use curly braces to define a dictionary
exDict = {'Jack':15, 'Bob':22, 'Alice':12, 'Kevin':17}
print(exDict)
print(exDict['Jack']) # find the value of key Jack
exDict['Tim'] = 14 # add a key
print(exDict)
exDict['Tim'] = 15 # update Tim's age
del exDict['Tim'] # delete key Tim

exDict2 = {'Mark':[16, 'brown'], 'Bill':23, 'Ashley':24, 'Louis':19}
print(exDict2)
print(exDict2['Mark']) # print the entirety of the value of Mark
print(exDict2['Mark'][1]) # print a specific element within Mark
# Values can be almost anything: other dictionaries, functions, etc..
