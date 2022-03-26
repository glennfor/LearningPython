import turtle
wn=turtle.Turtle()
wn.penup()
#wn.goto(-400, -200)
wn.pendown()
'''
To draw a Koch curve with length x, all you have to do is
1. Draw a Koch curve with length x/3.
2. Turn left 60 degrees.
3. Draw a Koch curve with length x/3.
4. Turn right 120 degrees.
5. Draw a Koch curve with length x/3.
6. Turn left 60 degrees.
7. Draw a Koch curve with length x/3.'''

'''
def draw(t, y):#paramters are the target winow and the lenght of the line to draw
    x=y
    if x==3:
        t.fd(x)
        return
    else:
        draw(t,x/3)
        t.lt(60)
        draw(t,x/3)
        t.rt(120)
        draw(t, x/3)
        t.lt(60)
        draw(t, x/3)
    x /=3'''
def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

draw(wn, 10, 10)
turtle.mainloop()
        
