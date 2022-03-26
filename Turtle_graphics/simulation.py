import turtle

colors=['red', 'purple', 'blue', '#00FF00', 'orange', 'yellow']#other one is green
#t=turtle.pen()
t=turtle.Turtle()
turtle.speed(100)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    #turtle.color(colors[x%6])
    t.width(x/100 +1)
    t.forward(x)
    t.left(59)

turtle.done()
