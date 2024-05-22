import matplotlib.pyplot as mpl

# List of Days
days = [1, 2, 3, 4, 5]

# No of Study Hours
studying = [7, 8, 6, 11, 7]

# No of Playing Hours
playing = [8, 5, 7, 8, 13]

# Stackplot with X, Y, colors value
mpl.stackplot(days, studying, playing,
            colors =['r', 'c'])

# Days
mpl.xlabel('Days')

# No of hours
mpl.ylabel('No of Hours')

# Title of Graph
mpl.title('Representation of Study and \
Playing wrt to Days')

# Displaying Graph
mpl.show()
