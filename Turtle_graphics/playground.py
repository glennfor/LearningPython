#UNIVERSAL COLOR LIST -->AVAILABLE FOR IMPORTATION

#made usable by configuration

#216 browser_safe colors(256 pallete)

color_list=['#000000', '#000033', '#000066', '#000099', '#0000CC', '#0000FF', '#003300', '#003333', '#003366', '#003399',
            '#0033CC', '#0033FF', '#006600', '#006633', '#006666', '#006699', '#0066CC', '#0066FF', '#009900', '#009933',
            '#009966', '#009999', '#0099CC', '#0099FF', '#00CC00', '#00CC33', '#00CC66', '#00CC99', '#00CCCC', '#00CCFF',
            '#00FF00', '#00FF33', '#00FF66', '#00FF99', '#00FFCC', '#00FFFF', '#330000', '#330033', '#330066', '#330099',
            '#3300CC', '#3300FF', '#333300', '#333333', '#333366', '#333399', '#3333CC', '#3333FF', '#336600', '#336633',
            '#336666', '#336699', '#3366CC', '#3366FF', '#339900', '#339933', '#339966', '#339999', '#3399CC', '#3399FF',
            '#33CC00', '#33CC33', '#33CC66', '#33CC99', '#33CCCC', '#33CCFF', '#33FF00', '#33FF33', '#33FF66', '#33FF99',
            '#33FFCC', '#33FFFF', '#660000', '#660033', '#660066', '#660099', '#6600CC', '#6600FF', '#663300', '#663333',
            '#663366', '#663399', '#6633CC', '#6633FF', '#666600', '#666633', '#666666', '#666699', '#6666CC', '#6666FF',
            '#669900', '#669933', '#669966', '#669999', '#6699CC', '#6699FF', '#66CC00', '#66CC33', '#66CC66', '#66CC99',
            '#66CCCC', '#66CCFF', '#66FF00', '#66FF33', '#66FF66', '#66FF99', '#66FFCC', '#66FFFF', '#990000', '#990033',
            '#990066', '#990099', '#9900CC', '#9900FF', '#993300', '#993333', '#993366', '#993399', '#9933CC', '#9933FF',
            '#996600', '#996633', '#996666', '#996699', '#9966CC', '#9966FF', '#999900', '#999933', '#999966', '#999999',
            '#9999CC', '#9999FF', '#99CC00', '#99CC33', '#99CC66', '#99CC99', '#99CCCC', '#99CCFF', '#99FF00', '#99FF33',
            '#99FF66', '#99FF99', '#99FFCC', '#99FFFF', '#CC0000', '#CC0033', '#CC0066', '#CC0099', '#CC00CC', '#CC00FF',
            '#CC3300', '#CC3333', '#CC3366', '#CC3399', '#CC33CC', '#CC33FF', '#CC6600', '#CC6633', '#CC6666', '#CC6699',
            '#CC66CC', '#CC66FF', '#CC9900', '#CC9933', '#CC9966', '#CC9999', '#CC99CC', '#CC99FF', '#CCCC00', '#CCCC33',
            '#CCCC66', '#CCCC99', '#CCCCCC', '#CCCCFF', '#CCFF00', '#CCFF33', '#CCFF66', '#CCFF99', '#CCFFCC', '#CCFFFF',
            '#FF0000', '#FF0033', '#FF0066', '#FF0099', '#FF00CC', '#FF00FF', '#FF3300', '#FF3333', '#FF3366', '#FF3399',
            '#FF33CC', '#FF33FF', '#FF6600', '#FF6633', '#FF6666', '#FF6699', '#FF66CC', '#FF66FF', '#FF9900', '#FF9933',
            '#FF9966', '#FF9999', '#FF99CC', '#FF99FF', '#FFCC00', '#FFCC33', '#FFCC66', '#FFCC99', '#FFCCCC', '#FFCCFF',
            '#FFFF00', '#FFFF33', '#FFFF66', '#FFFF99', '#FFFFCC', '#FFFFFF']

from turtle import *

a=Turtle()

a.clear()

class Draw(object):
    def __init__(self, pencil):
        self.pencil = pencil
    def drawcirc(self,x1,y1, r):
        self.pencil.penup()
        self.pencil.goto(x1,y1+r)
        self.pencil.pendown()
        for _ in range(120):
            self.pencil.rt(3)
            self.pencil.fd(1)


    def drawcoil (self, x1, y1, r, times=120):
        self.pencil.penup()
        self.pencil.goto(x1+r,y1+r)
        self.pencil.pendown()
        for _ in range(times):
            self.pencil.rt(3)
            self.pencil.fd(1)

def entry():#this is just like a main function in C/C++ but i name it anyhow and determine so
    colors=['blue', 'red', 'purple', 'green', 'yellow', 'grey', '#FFFF00', '#FF7777', '#FF00FF', 'magenta', 'cyan']
    a.speed(0)
    a.width(2)
    artist = Draw(a)
    for i in range(10):
        a.pencolor(colors[i % len(colors)])
        artist.drawcirc(100,0, i*4*2)
        artist.drawcoil(-100+i,0,i*4*2)

    for j in range(50):
        a.pencolor(colors[i % len(colors)])
        artist.drawcirc(j,0, i*4)

if __name__=='__main__':entry()
