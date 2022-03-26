import turtle
big_line = 100
little_line = 50
angle = 90
turtle.left(angle)
turtle.forward(big_line)
count = 0
while count < 4:
    turtle.right(angle//2)
    if count != 3:
        turtle.forward(little_line)
    else:
        turtle.forward(big_line)
    count = count + 1
turtle.right(90)
turtle.forward(130)

'''
import turtle
wn=turtle.Turtle()
an=30
sl=50
ll=100
wn.width(5)
wn.penup()
wn.goto(-500,0)
wn.pendown()
for i in range(12):
    wn.rt(an)
    wn.fd(ll)
    wn.rt(330)
    wn.bk(sl)
    wn.rt(-an)
    wn.fd(ll)
    wn.rt(-330)
    wn.bk(sl)'''
'''

    or

    for i in range(5):
    wn.rt(an)
    wn.fd(ll)
    wn.rt(an2)
    wn.bk(sl)
    an*=-1
    an2 *= -1'''
    
'''

from turtle import *
for i in range(200):
    forward(i)
    left(91)
'''

'''
from turtle import *
colors = ['red', 'purple', 'blue', 'green', 'orange']
for x in range(150):
    pencolor(colors[x % 5])
    width(x/10 + 1)
    forward(x)
    left(59)
'''
'''

from turtle import *
pendown()
circle_size = 100
for i in range(6):
    circle(circle_size)
    left(60)

'''
'''
from turtle import *
for angle in range(0, 360, 20):
    setheading(angle)
    forward(100)
    write(str(angle) + '\u00B0')
    backward(100)
'''
