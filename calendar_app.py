#/usr/bin/env python

'''
add greater functionality
--date and time
--alarm for particular days
--etc
'''

#calendar program

import datetime
import calendar
import time
import tkinter
from tkinter import *
import tkinter.messagebox
import tkinter.ttk as ttk
import tkinter.tix as tix
import ttkthemes as tk


##r=tk.ThemedTk()
##r.mainloop()
win = tix.Tk()
win.resizable(False,False)
win.title('$PY~SIMPLE~CALENDAR$')
win.attributes('-alpha', 0.8)
root=tix.Frame(win, bg='#200020')
root.pack(fill=BOTH, expand=True)


def get_cal():
    global ent
    try:
        year = int(ent.get())
        try:
            assert(1<=year<400_000)
        except AssertionError:
            tkinter.messagebox.showerror('Error', 'The year is unrealistic!!!!')
            #raise ValueError('playeey')
            return
    except ValueError:
        tkinter.messagebox.showerror('Error', 'The year is not specified correctly !!')
    else:
        for slave in root.slaves():
            slave.destroy()
        root.grid_forget()
        calendar_of(year)

tix.Label(root, text='Enter the Year ', font='times 20', fg='blue', bg='#77FF77').grid(row=0, column=0,padx=4, pady=2)

ent=tix.Entry(root, width=10, font='times 20', justify=RIGHT)
ent.grid(row=0, column=1, columnspan=2, padx=6, pady=2)
ent.insert(END, '2020')

b=tix.Button(root, text='Apply', font='times 20', fg='teal', bg='yellow', command=get_cal).grid(row=0, column=3, padx=6, pady=2)
win.bind('<Return>', lambda ev:get_cal())


def calendar_of(year):
    global root
    month=0
    for r in range(1,4):
        for c in range(4):
            month += 1
            tix.Button(root, text=calendar.month(year, month),justify=tkinter.LEFT,height=8, font=('courier new', 10, 'bold'), bg='lime green', fg='#202020').grid(row=r, column=c, padx=8, pady=4)

calendar_of(2020)
root.mainloop() 
