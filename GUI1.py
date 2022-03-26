#Want to try out a GUI application
#!/usr/bin/python3
import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
#top = tkinter.Tk()
# Code to add widgets will go here...
#top.mainloop()
 
    #Example (Hello, World):
#import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()
