#more on turtle
import turtle, math
import random

st = turtle.Turtle('turtle')
st.color('blue', 'cyan')
st.speed(10)

##st.begin_fill()
##for i in range(100):
##    st.forward(math.sqrt(i)*10)
##    st.left(135)
##
##st.end_fill()

##for i in range(2000):
##    st.forward(math.sqrt(i)*10)
##    st.left(i*180)
###---------------------------------------------------
###sunosoidal funct
for i in range(1000):
    st.forward(10)
    st.fd(math.sqrt(i/10)*25)
    st.left(20)

###--------------------------------------
##
##p = turtle.Turtle('classic')
##p.color('cyan')
##p.getscreen().bgcolor('#880000')
##def star(tut, size):
##    if size <10:return
##    else:
##        for j in range(size):
##            tut.fd(10)
##            star(tut, size//2)
##            tut.lt(216)
##p.pu();p.fd(-300);p.pd()
##
##star(p, 100)
