#/user/bin/env python

#C:\Users\nfor\Desktop\python_programs\projects\paint_program\paint_program.py

import tkinter
import tkinter.messagebox
import tkinter.filedialog
import tkinter.colorchooser
import tkinter.ttk as ttk
import ttkthemes
from tkinter import *

#root = Tk()
root = ttkthemes.ThemedTk(theme='breeze')
style = ttk.Style()
style.configure('TRadiobutton', justify=LEFT, anchor=W)
root.title('PYPAINT BOT')
root.wm_iconbitmap('paint.ico')

main_frame = tkinter.Frame(root, bg='brown')
main_frame.pack(fill=BOTH, expand=True)

container_frame = tkinter.Frame(main_frame)#,showhandle=True,bg='green')#, anchor=NW)
right_frame = tkinter.Frame(main_frame,bg='blue')
bottom_frame = ttk.Frame(main_frame)

#[packing for the topest level frames]
bottom_frame.pack(side=BOTTOM, fill=X)
container_frame.pack(side=LEFT, expand=True, fill=BOTH)
right_frame.pack(side=RIGHT, fill=Y)


#[pack the canvas container and add the canvas to window]
can_frame =tkinter.PanedWindow(container_frame,bg='yellow',showhandle=True) 
can_frame.pack(side=LEFT)

canvas= Canvas(can_frame, height = 400, width = 500,bg='coral', cursor = 'plus')
canvas.pack(side=LEFT, expand=True,fill=BOTH)

can_frame.add(canvas)

#[OTHER GLOBAL VARIABLES
drawing_data={
    'background':StringVar(value='white'),
    'foreground':StringVar(value='black'),
    'Thickness':IntVar(value=1),
    'fillcolor':StringVar(value='teal')
    }

save={
    'mode':StringVar(value='mono'),
    'orient':BooleanVar()
    }
oldpos = None,None



#[DRAWING AND UTILITY methods]

def save_image():
    global canvas
    filename = tkinter.filedialog.asksaveasfilename(title = 'Save File', initialdir = 'C:',
                    defaultextension=".png", filetypes= [('PNG Image', '.png'), ('JPEG Image', '.jpg'),
                                                         ('BitMap', '.bmp'), ('Icon', '.ico')])
    if filename:
        try:
            canvas.postscript(file=filename, colormode=save['mode'].get(), rotate=save['orient'].get())
        except tkinter.TclError:
            tkinter.messagebox.showerror('Error', 'Some error Ocurred while saving\nTry again')
    else:
        tkinter.messagebox.showwarning('Warning', 'You did not provide a file name\nYour drawing is not saved')



def set_oldpos(evnt):
    global oldpos
    oldpos = evnt.x, evnt.y
def draw(ev):
    global oldpos, canvas
    canvas.create_line(oldpos, (ev.x, ev.y), width = 2)
    oldpos = ev.x, ev.y

#[BINDING methods]
    
canvas.bind('<Button-1>', lambda ev: set_oldpos(ev))
canvas.bind('<B1-Motion>', lambda ev : draw(ev))


#[PRESENTATION AND ALL]
lab = ttk.LabelFrame(right_frame, text='SAVE CANVAS STATE')
lab.pack(side=LEFT)
ttk.Radiobutton(lab, text='Color Mode', variable=save['mode'], value='colormode').grid(row=0, column=0, padx=3, pady=3)
ttk.Radiobutton(lab, text='Gray', variable=save['mode'], value='gray').grid(row=0, column=1, padx=3, pady=3)
ttk.Radiobutton(lab, text='Black and White', variable=save['mode'], value='mono').grid(row=0, column=3, padx=3, pady=3)

ttk.Radiobutton(lab, text='Portrait', variable=save['orient'], value=False).grid(row=1, column=0, padx=3, pady=3)
ttk.Radiobutton(lab, text='Land Scape', variable=save['orient'], value=True).grid(row=1, column=1,columnspan=2, padx=3, pady=3)

tkinter.Button(lab, text='SAVE', font='times, 15', width=10,command=save_image, foreground='green', background='#200020', borderwidth=4).grid(row=2, columnspan=3, padx=3, pady=3)

root.mainloop()

      
