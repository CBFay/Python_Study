# A basic matplotlib graph
# Created 12.17.2017 by CB Fay

import matplotlib.pyplot as pt

x = [n for n in range(64)]
y = [n**2 for n in range(64)]

pt.bar(x,y,color=['blue','purple'], alpha=.9)
pt.xlabel("n")
pt.ylabel("n^2")
pt.title("Powers of 2")
pt.xlim(0,max(x)+1)
pt.ylim(0,max(y))
pt.show()
