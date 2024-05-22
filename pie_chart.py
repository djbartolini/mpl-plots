import matplotlib.pyplot as mpl 

x = [1, 2, 4, 5]

# this will explode the 1st wedge
# i.e. will separate the 1st wedge
# from the chart
e  = (0.1, 0, 0, 0)

mpl.pie(x, explode = e)
mpl.title("Pie chart")

mpl.show()
