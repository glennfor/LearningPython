import turtle
artist=turtle.Turtle()
artist.speed(5)
artist.shape()
for j in range(3):
    artist.forward(100)
    artist.left(90+180)
    artist.backward(10)
    artist.right(90)
    artist.forward(100)

    artist.left(60)
artist.penup()
#artist.goto(102, 0)
artist.color("blue", "blue")
artist.pencolor("black")
artist.setpos(0,-25)
artist.begin_fill()
artist.circle(25)
artist.end_fill()
'''
#Draw a right anglen triangle
draw=turtle.Turtle()
draw.shape('arrow')#no pointer specified
draw.speed(50)
draw.setpos()
draw.pendown()
draw.forward(400)
draw.right(90)
draw.forward(300)
draw.left(60)
draw.backward(500)
'''
turtle.done()
