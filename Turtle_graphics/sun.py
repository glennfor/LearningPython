'''
import turtle
wn = turtle.Screen()
al=turtle.Turtle()
ay=turtle.Turtle()
ap=turtle.Turtle()
tri=turtle.Turtle()
ay.speed (0)
al.speed (0)
ap.speed (0)
tri.speed (0)
tri.penup()
tri.left(90)
tri.forward(-100)
tri.right(90)
tri.pendown()
for triangle in range(3):
    tri.forward(60)
    tri.left(120)
for square in range(4):
    al.forward (50)
    al.left (90)
ay.penup ()
ay.forward (100)
for octagon in range(8):
    ay.pendown ()
    ay.forward (50)
    ay.left (45)
ap.penup ()
ap.backward (50)
for hexagon in range(6):
    ap.pendown()
    ap.backward (50)
    ap.right (60)
'''



  #===============222===============
'''
import turtle
wn = turtle.Screen()
bob=turtle.Turtle()
bob.speed(0)
n=int(input("number of sides?"))
l=int(input("length of side?"))
c=input("color?")
f=input("fill color?")
bob.color(c, f)
bob.begin_fill()
bob.forward(300)
for i in range(n):
	bob.forward(l)
	bob.left(360/n)
bob.end_fill()
''' 
  
#=================3333333333333333==============
'''

import turtle
wn = turtle.Screen()
bob=turtle.Turtle()
dot=turtle.Turtle()
bob.shape("turtle")
dot.shape("arrow")
dot.penup()
bob.penup()
wn.bgcolor("lightgreen")
bob.color("blue")
dot.color("blue")
bob.speed(0)
dot.speed(0)
for circle in range(12):
    bob.forward(70)
    bob.stamp()
    bob.forward(-70)
    bob.right(30)
for dots in range(12):
    dot.forward(45)
    dot.pendown()
    dot.forward(5)
    dot.penup()
    dot.forward(-50)
    dot.right(30)
  '''
  

#============================44444444444444444444444===============
'''
import turtle
wn=turtle.Screen()
b = turtle.Turtle()
b.shape("arrow")
b.speed(0)
for i in range(100):
	b.forward(50)
	b.left(85)
b.pendown()
'''
  
  
  

#=============================55555555555555555555555=======================
'''
import turtle
wn = turtle.Screen()
spider = turtle.Turtle()
spider.shape("triangle")
spider.shape("circle")
spider.speed(0)
n = int(input("How many legs should this sprite have? "))
angle = 360 / n
for i in range(n):
    spider.right(angle)
    spider.forward(65)
    spider.stamp()
    spider.right(180)
    spider.forward(65)
    spider.right(180)
    
'''
#++++++++++++++++^6666666++++++++++++++++++==


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
