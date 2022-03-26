#  david_star.pyw

#draw david's star
#NB
'''
 I have configured the file to run without a console window attached
 '''


import turtle

draw=turtle.Turtle()
turtle.speed(25)
draw.hideturtle()#makes the turtle invisible

draw.width(3)
draw.penup()
draw.goto(0, 100)
draw.pendown()

for i in range(5):
    draw.fd(200)
    draw.right(144)

turtle.done()
    


