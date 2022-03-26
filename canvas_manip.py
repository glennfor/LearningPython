from tkinter import *
def mouse_motion_event(event):
    label.configure(text='({}, {})'.format(event.x, event.y))
def wheel_event(event):
    global x1, x2, y1, y2
    if event.delta>0:
        diff = 1
    elif event.delta<0:
        diff = -1
        x1+=diff
        x2-=diff
        y1+=diff
        y2-=diff
    canvas.coords(rect,x1,y1,x2,y2)
def b1_event(event):
    global color
    if not b1_drag:
        color = 'Red' if color=='Blue' else 'Blue'
    canvas.itemconfigure(rect, fill=color)

def b1_motion_event(event):
    global b1_drag, x1, x2, y1, y2, mouse_x, mouse_y
    x = event.x
    y = event.y
    if not b1_drag:
        mouse_x = x
        mouse_y = y
        b1_drag = True
        return
    x1+=(x-mouse_x)
    x2+=(x-mouse_x)
    y1+=(y-mouse_y)
    y2+=(y-mouse_y)
    canvas.coords(rect,x1,y1,x2,y2)
    mouse_x = x
    mouse_y = y
def b1_release_event(event):
    global b1_drag
    b1_drag = False
root=Tk()
label = Label()
canvas = Canvas(width=200, height=200)
canvas.bind('<Motion>', mouse_motion_event)
canvas.bind('<ButtonPress-1>', b1_event)
canvas.bind('<B1-Motion>', b1_motion_event)
canvas.bind('<ButtonRelease-1>', b1_release_event)
canvas.bind('<MouseWheel>', wheel_event)
canvas.focus_set()
canvas.grid(row=0, column=0)
label.grid(row=1, column=0)
mouse_x = 0
mouse_y = 0
b1_drag = False
x1 = y1 = 50
x2 = y2 = 100
color = 'blue'
rect = canvas.create_rectangle(x1,y1,x2,y2,fill=color)
mainloop()
