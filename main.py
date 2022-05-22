import random
from matplotlib.pyplot import *
import numpy

lst_main = [i for i in range(10)]
lst1 = [random.randint(10, 100) for i in range(10)]
lst2 = [random.randint(10, 100) for i in range(10)]
print(lst1, lst2, sep="\n")

width = 0.3
x = numpy.arange((len(lst_main)))

fig, ax = subplots()
rects1 = ax.bar(x - width/2, lst1, width, label="lst1")
rects2 = ax.bar(x + width/2, lst2, width, label="lst2")

ax.set_xticks(x)
ax.set_xticklabels(lst_main)
show()