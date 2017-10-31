# WriteToFile.py
# created 10.02.2017 by CB Fay

text = 'hey this is some different text\nhey it\'s a new line'

# we're going to open(create) this file, and write to it
saveFile = open('D:\Quick Access\Desktop\exampleFile.txt', 'w')
saveFile.write(text)
saveFile.close()
