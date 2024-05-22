import matplotlib.pyplot as mpl 
import numpy

x = numpy.linspace(0.1, 2 * numpy.pi, 41)
y = numpy.exp(numpy.sin(x))

mpl.stem(x, y, use_line_collection = True)
mpl.title("Stem graph")

# Legend
mpl.legend(["Example figure"])
mpl.show()
