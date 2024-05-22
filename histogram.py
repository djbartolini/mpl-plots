import matplotlib.pyplot as mpl

x = [1, 2, 3, 4, 5, 6, 7, 4]

mpl.hist(x, bins = [1, 2, 3, 4, 5, 6, 7])
mpl.title("Histogram")

# Legend
mpl.legend("Height")
mpl.show()
