'''
'''
# I have configured the file to run without a console window attached
'''


import turtle
#from playground import color_list as colours

draw=turtle.Turtle()
turtle.speed(9)
draw.hideturtle()#makes the turtle invisible

draw.width(3)

#draw.color('')
#raw.begin_fill()
draw.width(5)
draw.lt(90)
draw.circle(100, 200)
draw.penup()
draw.home()
draw.pendown()
draw.lt(90)
draw.circle(-100, 200)
pos=draw.position()
for i in range(9):
    draw.rt(i*1.5)
    draw.fd(i*10)
    
draw.penup()
x,y=pos
x+=-400
draw.goto(x,y)
draw.pendown()
draw.lt(90)
for i in range(9):
    draw.lt(i*1.5)
    draw.fd(i*10)
    
#draw.end_fill()

turtle.done()
'''

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure() # create a figure
ax = fig.gca(projection='3d') # create a 3-dimensional axis
X = np.arange(-5, 5, 0.25) # horizontal range
Y = np.arange(-5, 5, 0.25) # vertical range
X, Y = np.meshgrid(X, Y) # create a special grid
R = np.sqrt(X**2 + Y**2) # calculate square root
Z = np.sin(R) # calculate sinus
## use #@UndefinedVariable below to ignore the error for cm.coolwarm
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap=cm.coolwarm, linewidth=0,antialiased=False)
ax.set_zlim(-1.01, 1.01) # z-axis is third dimension
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show() # display the figure




 

