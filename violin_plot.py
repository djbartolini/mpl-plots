import matplotlib.pyplot as mpl 
import numpy

# create list of uniformly distributed values
uniform = numpy.arrange(-100, 100)

# create list of normally distributed values
normal = numpy.random.normal(size = 100) * 30

# figure & axes to plot 
fig, (ax1, ax2) = mpl.subplots(
    nrows = 1,
    ncols = 2,
    figsize = (9, 4),
    sharey = True)

# plot for uniform dist
ax1.set_title('Uniform distribution')
ax1.set_ylabel('Values')
ax1.violinplot(uniform)

# plot for normal dist 
ax2.set_title("Normal distribution")
ax2.violinplot(normal)

mpl.show()
