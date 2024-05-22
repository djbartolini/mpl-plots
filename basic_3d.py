import matplotlib.pyplot as mpl 

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
z = [1, 8, 27, 64, 125]

figure = mpl.figure()

ax = mpl.axes(projection = '3d')

as.plot3D(z, y, x)
