#C:\Users\nfor\Desktop\python_programs\projects\calculator\calculator.py

import tkinter
import tkinter as tk
import tkinter.tix as tix
import tkinter.ttk as ttk
from tkinter import *
import ttkthemes as tt
import tkinter.colorchooser as tkcc
import tkinter.messagebox as tkmb

import PIL
from PIL import ImageTk, Image

import math
import cmath
import random

#import sympy, scipy, numpy, matplotlib, pandas, os, sys,countn, fractions

#÷  ∙  √   2ⁿ   

main_Buttons = {
            'numbers':[ ['7', '8', '9'],['4', '5', '6'],['1', '2', '3']],# ['0', '.']],
            'operators':[ '±','+', '-', '/', '*'],
            'op2':['(', '%', '1/x','x²','x^3'],
            'op3':[')', '√', 'xⁿ'],#'=' takes the reaining space
            'utility':['<-', 'CE', 'C', 'MC', 'MR', 'MS', 'M+', 'M-'],
            'functions': ['fact', 'int', 'hex', 'oct', 'bin', 'cos']
            
    }

class Calculator(object):
    def __init__(self, title):
        self._window =tt.ThemedTk(theme='breeze')
        style = ttk.Style(self._window)
        style = ttk.Style(self._window)
        style.configure('.', borderwidth=5, relief=RAISED)
        self._window.title ('PYCALEX Calculator')
        self._expression = ''
        self._answer = ''
        #self._window.geometry('%dx%d+%d+%d'%( 350, 200, 30, 20))
        self._window.resizable(False, False)
        self._entry_lab = Label(self._window, height = 2, font = ('verdana', 12, 'bold'), bg = '#C8C8C8')
        self._result_lab = Entry(self._window, state = 'readonly', font = ('verdana', 20, 'bold'),  bg = '#FF00FF')
        self._btns_frame = Frame(self._window, bg = '#CCF')
        self.init_win()
    def init_win(self):
        self._entry_lab.pack(fill = X)
        self._result_lab.pack(fill = X)
        self._btns_frame.pack(fill = BOTH)
        #backpace and clear
        ttk.Button(self._btns_frame, width=3, text = 'DEL'
                         ).grid(row = 0, column = 0,
                                                       padx = 2, pady = 2)
        ttk.Button(self._btns_frame, text ='CLR' ).grid(row = 0, column =1 ,
                                                        columnspan=2, padx = 2, pady = 2)


        #numbers 1 to 9
        for row, item in enumerate(main_Buttons['numbers'], start = 1):
            for col, num in enumerate(item, start = 0):
                    ttk.Button(self._btns_frame,width=3,  text = num
                          ).grid(row = row, column = col, padx = 2, pady = 2)
        #  0
        ttk.Button(self._btns_frame,text = '0').grid(row = 4, column = 0,
                                                           sticky = W, columnspan = 2,padx = 2, pady = 2)
        #  .
        ttk.Button(self._btns_frame,width=3,  text = '.').grid(row = 4, column =2 , padx = 2, pady = 2)
         #+/-   +   -  /  *
        for row, item in enumerate(main_Buttons['operators'], start=0):
            ttk.Button(self._btns_frame,width=3,  text = item).grid(row = row, column = 3, padx = 2, pady = 2)

        for row, item in enumerate(main_Buttons['op2'], start=0):
            ttk.Button(self._btns_frame,width=3,  text = item).grid(row = row, column = 4, padx = 2, pady = 2)

        for row, item in enumerate(main_Buttons['op3'], start=0):
            ttk.Button(self._btns_frame,width=3,  text = item).grid(row = row, column = 5, padx = 2, pady = 2)

        # = 
        #ttk.Button(self._btns_frame,text = '=').grid(row = 3,
         #                                      column = 5, padx = 2, pady = 2)#rowspan = 2,
        self._window.mainloop()

        '''
        all ttk.Buttons normally add their text to the general expresion except special cases like below
        '''
    def btn_callback(self, item):
        self._expression += item
        self._entry_lab.configure(text = self._expression)


    def equals_to(self):
        try:
            self._answer = eval(self._expression)
            self._result_lab.configure(text = str(self._answer))
        except ValueError:
            self._answer = 0
            self._result_lab.configure(text = 'MATH ERROR')
        finally:
            self._expression = str(self._answer)

    def backspace(self):
        if self._expression=='0' or self._expression==str(self._answer) or not self._expression:
            '''if 0 means there was error or last calulation was 0
            if anser means nothing has been typed in yet
            if empty of course it won't ake sense'''
            return
        self._expression = self._expression[:-1] #delete last character and update the label
        self._entry_lab.configure(text = self._expression)

    def clear(self):
        self._expression = ''
        self._entry_lab.configure(text = self._expression)
        
    def set_bindings(self):
        pass

    def _create_menu(self):
        pass

Calculator('PYCALEX Calculator')
       
        

