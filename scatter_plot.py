import matplotlib.pyplot as mpl 

x = [3, 1, 3, 12, 2, 4, 4]
y = [3, 2, 1, 4, 5, 6, 7]

mpl.scatter(x, y)

# Adding legend to the plot
mpl.legend("Point")

mpl.title("Scatter chart")
mpl.show()
