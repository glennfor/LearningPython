from turtle import *
from math import sin, cos, tan, radians


def drawaxis(master):  # axis to draw primary trigonometric functions curves
    master.width(3)
    # starting with the y axis
    master.penup()
    master.goto(-400, -270)  # draw axis to be longer than the spcae to be actually used
    master.pendown()
    master.lt(90)
    master.forward(540)
    # and now the x-axis
    master.penup()
    master.goto(-410, -5)
    master.pendown()
    master.rt(90)
    master.fd(800)  # master ends at 360


def drawcurve(master, func, sign=1):  # with optional sign
    master.penup()
    master.goto(-400, -5)
    master.pendown()
    for i in range(360):
        x, y = (-400 + (i * 2), sign * (func(radians(i)) * 250) - 5)  # point to plot
        master.goto(x, y)

#testing the functions on ...

drawing_board=Turtle()


drawaxis(drawing_board)  #drawing the axis
drawcurve(drawing_board, sin)  #draw the sine curve
drawcurve(drawing_board, cos)  #draw the cosine curve
drawcurve(drawing_board, sin, -1)  #draw the -sine curve
drawcurve(drawing_board, cos, -1)  #draw the -cosine curve

done()

#since the tan , sinh, cosh, tanh, and others have an infinite amplitute they will be analysed later
