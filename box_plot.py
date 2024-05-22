import matplotlib.pyplot as mpl 
import numpy

numpy.random.seed(10)
data = numpy.random.nomral(100, 20, 100)

figure = mpl.figure(figsize = (10, 7))

mpl.boxplot(data)

mpl.show()
