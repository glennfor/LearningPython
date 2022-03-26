#C:\Users\nfor\Desktop\python_programs\projects\calculator\calculator.py

import tkinter
import tkinter as tk
import tkinter.tix as tix
import tkinter.ttk as ttk
from tkinter import *

import tkinter.colorchooser as tkcc
import tkinter.messagebox 

import PIL
from PIL import ImageTk, Image

import math
import cmath
import random

#import sympy, scipy, numpy, matplotlib, pandas, os, sys,countn, fractions


#÷  ∙  √   2ⁿ   

main_Buttons = {
            'numbers':[ ['7', '8', '9'],['4', '5', '6'],['1', '2', '3']],# ['0', '.']],
            'operators':['+', '-', '/', '*'],
            'op2':['(', '%', '1/x','x²','x^3'],
            'op3':[')', '√', 'xⁿ'],#'=' takes the reaining space
            'utility':['<-', 'CE', 'C', 'MC', 'MR', 'MS', 'M+', 'M-'],
            'functions': ['fact', 'int', 'hex', 'oct', 'bin', 'cos']
            
    }

class Calculator(object):
    def __init__(self, master, title='PYCALEX Calculator'):
        self._window = master
        self._window.title (title)
        self._window.iconbitmap('IconleakAtrousCalculator.ico')
        self._expression = StringVar()
        self._answer = StringVar()

        #self._window.geometry('%dx%d+%d+%d'%( 350, 200, 30, 20))
        self._window.resizable(False, False)
        self._entry_lab = Label(self._window, justify = RIGHT,anchor=E,  font = ('times', 20, 'bold'), bg = '#eee',
                                textvariable = self._expression, height=3,borderwidth=10, relief=SUNKEN, width=22)
##        self._result_lab = Entry(self._window, state = 'readonly', font = ('verdana', 20, 'bold'),  disabledbackground = '#FF00FF',
##                                 textvariable = self._answer)
        self._btns_frame = Frame(self._window,relief=RAISED, bg = '#CCF')
        self.init_win()
    def init_win(self):
        self._window.bind('<Return>', lambda ev:self.calculate())
        
##        self._entry_lab.pack(fill = X)
##        #self._result_lab.pack(fill = X)
##        self._btns_frame.pack(fill = BOTH)

        self._entry_lab.grid(row=0, padx=5, pady=10)
        #self._result_lab.pack(fill = X)
        self._btns_frame.grid(row=1, padx=5, pady=10)

        #backpace and clear
        tkinter.Button(self._btns_frame, width=3, borderwidth=5, text = 'DEL', font= ('verdana', 15, 'bold'),fg = 'blue', bg = 'gray',
                       command = self.backspace).grid(row = 0, column = 0, padx = 2, pady = 2)
        tkinter.Button(self._btns_frame, borderwidth=5,width=7,font= ('verdana', 15, 'bold'), text ='CLR', bg ='pink'
                       ,command = self.clear).grid(row = 0, column =1 ,
                                                        columnspan=2, padx = 2, pady = 2)


        #numbers 1 to 9
        for row, item in enumerate(main_Buttons['numbers'], start = 1):
            for col, num in enumerate(item, start = 0):
                    tkinter.Button(self._btns_frame, borderwidth=5,width=3, font= ('verdana', 15, 'bold'), text = num
                       , fg = '#88FF88', bg = 'gray', command = lambda item = num: self.btn_callback(item)  ).grid(row = row, column = col, padx = 2, pady = 2)
        #  0
        tkinter.Button(self._btns_frame, borderwidth=5,width = 8, justify = CENTER,text = '0',font= ('verdana', 15, 'bold'), fg = '#88FF88',
                       bg = 'gray', command = lambda item = '0': self.btn_callback(item)  ).grid(row = 4, column = 0,
                                                           sticky = W, columnspan = 2,padx = 2, pady = 2)
        #  .
        tkinter.Button(self._btns_frame, borderwidth=5,width=3, font= ('verdana', 15, 'bold'), text = '.', fg = '#88FF88', bg = 'gray'
                       , command = lambda item = '.': self.btn_callback(item)  ).grid(row = 4, column =2 , padx = 2, pady = 2)
         # +/-
        tkinter.Button(self._btns_frame, borderwidth=5,width=3, font= ('verdana', 15, 'bold'), text =  '±', fg = '#00CCFF', bg = 'gray'
                       , command = self.negate).grid(row = 0, column =4 , padx = 2, pady = 2)
         # +   -  /  *
        for row, item in enumerate(main_Buttons['operators'], start=1):
            tkinter.Button(self._btns_frame, borderwidth=5,width=3 ,font= ('verdana', 15, 'bold'), fg = '#00CCFF', bg = 'gray',text = item,
                            command = lambda it =item: self.btn_callback(it)).grid(row = row, column = 4, padx = 2, pady = 2)

        for row, item in enumerate(main_Buttons['op2'], start=0):
            tkinter.Button(self._btns_frame, borderwidth=5,width=3,  font= ('verdana', 15, 'bold')
                           ,text = item, fg = '#440044',
                           bg = 'gray').grid(row = row, column = 5, padx = 2, pady = 2)

        for row, item in enumerate(main_Buttons['op3'], start=0):
            tkinter.Button(self._btns_frame, borderwidth=5,width=3,
                           font= ('verdana', 15, 'bold'), text = item,
                           fg = '#660066', bg = 'gray'
                           ).grid(row = row, column = 6, padx = 2, pady = 2)

       #=
        tkinter.Button(self._btns_frame,width=3, borderwidth=5,height = 3,font= ('verdana', 15, 'bold'), text = '=', fg = '#FFFF00', bg = 'gray',
                        command = self.calculate).grid(row = 3,
                                               rowspan = 2, column = 6, padx = 2, pady = 2)#rowspan = 2,
        self._window.mainloop()

        '''
        all tkinter.Buttons normally add their text to the general expresion except special cases like below
        '''

    def negate(self):
        if self._expression.get():
            self._entry_lab.configure(fg = 'black')
            self._expression.set('-('+self._expression.get()+')')

    def  func(self, param1, param2):
        pass
    
    def btn_callback(self, item):
        self._entry_lab.configure(fg = 'black')
        if item == '.' and '.' in self._expression.get():
            return
        self._expression.set(self._expression.get()+ item)
        #self._entry_lab.configure(text = self._expression)
        

    def calculate(self):
        try:
            self._expression.set(str(eval(self._expression.get())))
            #self._entry_lab.configure(text = self._expression)
        except (ValueError, SyntaxError, NameError):
            self._entry_lab.configure(fg = 'red')
            tkinter.messagebox.showerror('Math Error', 'MATH ERROR: Invalid Mathematical statement')
            self._expression.set('')
        except ZeroDivisionError:
            self._entry_lab.configure(fg = 'red')
            tkinter.messagebox.showerror('Math Error', 'MATH ERROR:Division by zero')
            self._expression.set('')

        finally:
            #self._expression = str(self._answer)
            pass
        '''
            try:
            self._answer = eval(self._expression)
            self._result_lab.configure(text = str(self._answer))
        except ValueError:
            self._answer = 0
            self._result_lab.configure(text = 'MATH ERROR')
        finally:
            self._expression = str(self._answer)
            '''

    def backspace(self):
        self._entry_lab.configure(fg = 'black')
        if self._expression.get()=='':  # or self._expression.get()==str(self._answer.get()) or not self._expression:
            '''if 0 means there was error or last calulation was 0
            if anser means nothing has been typed in yet
            if empty of course it won't make sense'''
            return
        self._expression.set(self._expression.get()[:-1])#delete last character and update the label
        #self._entry_lab.configure(text = self._expression)

    def clear(self):
        self._expression.set('')
        #self._entry_lab.configure(text = self._expression)
        
    def set_bindings(self):
        pass

    def _create_menu(self):
        pass

if __name__=='__main__':
    win = tkinter.Tk()
    Calculator(win)
    win.mainloop()
       
        

