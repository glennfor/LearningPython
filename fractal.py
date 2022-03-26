##Complex numbers are fascinating, though not all that useful in day-to-day life. One nice application,
##however, is fractals. Here is a program that draws the famous Mandelbrot set. The program
##requires the PIL and Python 2.6 or 2.7.

from tkinter import *
from PIL import Image, ImageTk, ImageDraw

def color_convert(r, g, b):
    return '#{0:02x}{1:02x}{2:02x}'.format(int(r*2.55),int(g*2.55),int(b*2.55))
def m():
    max_iter = 75
    xtrans = -.5
    ytrans = 0
    xzoom = 150
    yzoom = -150
    root = Tk()
    canvas = Canvas(width=300, height=300)
    canvas.grid()
    image=Image.new(mode='RGB',size=(300,300))
    draw = ImageDraw.Draw(image)
    for x in range(300):
        c_x = (x-150)/float(xzoom)+xtrans
        for y in range(300):
            c = complex(c_x, (y-150)/float(yzoom)+ytrans)
            count=0
            z=0j
            while abs(z)<2 and count<max_iter:
             z = z*z+c
             count += 1
            draw.point((x,y),fill=color_convert(count+25,count+25,count+25))
        canvas.delete(ALL)
        photo=ImageTk.PhotoImage(image)
        canvas.create_image(0,0,image=photo,anchor=NW)
        canvas.update()
    mainloop()
if __name__ == '__main__':
    m()
