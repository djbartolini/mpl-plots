import matplotlib as mpl 

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 2, 1, 6, 7, 8, 2]

# error parameter
y_error = 0.2

mpl.plot(x, y)

mpl.errorbar(x, y, yerr = y_error, fmt = 'o')

mpl.show()
