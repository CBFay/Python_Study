# ReadFile.py
# created 10.02.2017 by CB Fay

# saves the entirety of the text as a list?
readMe = open('D:\Quick Access\Desktop\exampleFile.txt', 'r').read()
print(readMe)

# saves each line as elements in a list
readMe = open('D:\Quick Access\Desktop\exampleFile.txt', 'r').readlines()
print(readMe)
