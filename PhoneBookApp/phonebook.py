##!usr/bin/env python

#C:\Users\nfor\Desktop\python_programs\projects\PhoneBookApp\phonebook.py
#a simple phone book app


##########################################################@JG
# PyPhoneBook

# Description: PyPhoneBook is a phonebook developed 
# in python with tkinter. The goal of this application 
# is to save contacts. It is useful if you lose your 
# mobilephone contacts

# Author: ****  **** jg
##########################################################


#[rewrite same app to use entry date as the primary key
#[then make name modifiable, ability to create empty contacts,
#[INS]-=Android contact storage system REPLI.


#[GUI] impoorts
import tkinter
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox
import tkinter.filedialog
import tkinter.colorchooser

#{IMAGE] manipulation
import PIL
from PIL import ImageTk, Image

#[UTILS
import os
import glob
import sys
import datetime
import json
import shutil

#[DATABASING]
import sqlite3

#C:\Users\nfor\Desktop\python_programs\projects\PhoneBookApp\phonebook.py
#a simple phone book app


#[MAIN COMPONENTS]
'''
DATABASE FILE:contact_data.db
    -created on the first run
    -find a way to make it inaccessible

CONFIGURATION FILE: data_file.json
    -created on first run
    -holds password and username
    -find a way to make it inaccessible

CONTACT_IMAGES: Folder , holding photos of contacts
    -default.png is the default image for any contact without a specified photo
    
'''

class ScrolledListbox(Listbox):
    def __init__(self, master=None, **kw):
        self._frame = Frame(master)
        self._vbar = Scrollbar(self._frame)
        self._hbar = Scrollbar(self._frame, orient = HORIZONTAL)
        #packing::::-after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
        #griding::::-column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky
        self._vbar.pack(side=RIGHT, fill=Y)
        self._hbar.pack(side = BOTTOM, fill = X)
        #nb... packing trick for hbar and status bar skeptical

        kw.update({'yscrollcommand': self._vbar.set, 'xscrollcommand':self._hbar.set})
        Listbox.__init__(self, self._frame, **kw)
        self.pack(side=LEFT, fill=BOTH, expand=True)
        self._vbar['command'] = self.yview
        self._hbar['command'] = self.xview
        self['relief'] = SUNKEN
        self['borderwidth'] = 8

        # Copy geometry methods of self.frame without overriding Text
        # methods -- hack!
        list_meths = vars(Listbox).keys()
        methods = vars(Pack).keys() | vars(Grid).keys() | vars(Place).keys()
        methods = methods.difference(list_meths)

        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self._frame, m))


    def __str__(self):
        return str(self._frame)


class PhoneBook(object):
    def __init__(self):
        #self._window = tkinter.Tk(className = 'PyPhony')
        self._window = tkinter.Tk()
        self._mainframe = tkinter.Frame(self._window, background='#200020', borderwidth=2,relief=RAISED)
        self._mainframe.pack(fill=BOTH)
        self._window.title('PyPHONY')
        self._window.resizable(False, False)
        self._window.iconbitmap('ipad.ico')
        #self._window.wm_iconbitmap('po.dll')
        self.start_up()
        self._showing=False

        self.record=[
            'FULLNAME',
            'FIRSTNAME',
            'SURNAME',
            'OTHERNAME',
            'NICKNAME',
            'PHONENUMBER' ,
            'EMAIL' ,  
            'PICTURE' ,
            'BIRTHDAY' ,
            'TITLE' ,
            'ADDRESS' ,
            'CITY' ,
            'ENTRYDATE', 
            'WEBSITE' , 
            'CATEGORY' ,
            ]
        self.data_records={attribute:StringVar() for attribute in self.record}
        #print(self.data_records)
        
    def init(self):
        
        self._window.minsize(width=450, height=350)
        self._lab = tkinter.Label(self._mainframe, font = ('verdana', 20), relief = RAISED,borderwidth=5,height=3, text =  'PHONE BOOK',background='green')
        self._lab.pack(side = TOP, fill = X)
        tkinter.Label(self._lab, font = ('verdana', 8, 'bold'), relief = SOLID,height=2, foreground= 'teal',background ='black',
                    text =  ' Date : {}'.format(str(datetime.datetime.today())[:-15])).place(x=self._lab.winfo_width(), y = self._lab.winfo_height())
        self._commmandframe = Frame(self._mainframe, relief = RAISED, background = 'pink', borderwidth =5)
        self._listframe = Frame(self._mainframe, background = 'blue', relief = RAISED,borderwidth =5)
        self._commmandframe.pack(side = LEFT,fill=BOTH)
        
        for row, (text, cmd) in  enumerate([('My Contacts',self.show_contact_info),
                                        (' Add Group ', lambda : tkinter.messagebox.showinfo('Future',
                                                        'This feature is not yet available\nThis app is still under developement\nCheck some time later'))
                                     , ('   About ...  ', self.about_app)]):
            tkinter.Button(self._commmandframe, text = text, font = ('heveltica', 20, 'bold'),background ='teal',borderwidth =2,
                           command = cmd).grid(
                row = row, column =0 , padx = 4, pady = 45 if row==2 else 8)
        self.temp_frame = Frame(self._commmandframe, background='#400060', borderwidth=3, relief=RAISED)
        self.temp_frame.grid(row=0, column=1,rowspan=3,padx=8, pady=8, sticky=NW)#.pack(side=RIGHT, fill=BOTH)
        msg= 'ENJOY THE APP\n'+'-$ Add contacts\n'+'-$ Update existing contacts\n''-$ Delete useless contacts\n''-$ View contact details\n''-$ Obtain sizeable information on contacts\n''-$ Store contacts against their Photos\n'
        tkinter.Message(self.temp_frame,text=msg, foreground='#00A000', bg='#400060', font='cambria 16').pack(side=LEFT, expand=True, fill=BOTH)

    def set_login_window(self):
        #log in details
        attempts=0
        username, password = StringVar(), StringVar()

        def submit_login():
            nonlocal attempts
            if username.get()==USER_DATA['username'] and password.get()==USER_DATA['password']:
                tkinter.messagebox.showinfo('WELCOME', 'Enjoy your experience : Meet the Cool of Python!!')
                frame1.destroy()
                lab.destroy()
                self.init()
            else:
                username.set('')
                password.set('')
                attempts+=1
                if attempts==5:
                    tkinter.messagebox.showerror('Error',
                    'Aplication will shutdown due to authentication error\nError:Password or Username Mismatch')
                    self._exitApp()
                tkinter.messagebox.showerror('Error', f'Password or Username Mismatch: \n{5-attempts} chances left befor application shuts down')
                
        lab=tkinter.Label(self._mainframe, font = ('verdana', 30), relief = RAISED
                          ,borderwidth=5,
                height=3, text =  'PHONE BOOK',background='green')
        lab.pack(side = TOP, fill = X)
        frame1 = tkinter.Frame(self._mainframe, background ='teal', relief = RAISED, borderwidth = 5)
        Label(frame1, background='teal',text='USER NAME ',font = ('verdana', 20)).grid(row =0, column = 0, padx = 8, pady=8)
        n1=tkinter.Entry(frame1,font = ('Bookman Old Style', 20),
                         width = 16,textvariable=username)
        n1.grid(row =0, column = 1, padx = 8, pady=8)
        n1.focus_set()
        Label(frame1,background='teal', text='PASSWORD ',font = ('verdana', 20)).grid(row =1, column = 0, padx = 8, pady=8)
        tkinter.Entry(frame1,font = ('Bookman Old Style', 20), show = '*', width = 16,textvariable=password).grid(row =1, column = 1, padx = 8, pady=8)
        Button(frame1, command = submit_login, text='   Log In   ',width=12, justify=CENTER, anchor='center',foreground = 'aqua',background = 'blue',font = ('times', 20, 'bold'), relief = RAISED, borderwidth = 5).grid(row =2, column = 1, padx = 12, pady=12)
        frame1.pack(side=LEFT, fill=BOTH)
        #frame1.grid(row=0, padx=3, pady=3)

    def show_contact_info(self):
        if self._showing:
            return
        self.temp_frame.destroy()
        self.contacts_list = self.get_contact_names()
        self._showing = True
        self._lab.configure(height =2, font = ('verdana', 30))
        self._listframe.pack(side = RIGHT,fill=BOTH)
        self._list = ScrolledListbox(self._listframe,height =12, font = ('times', 13, 'bold')
                                     ,selectbackground = 'teal')
        for count, name in enumerate(self.contacts_list, start = 1):
            self._list.insert(count,  name)

        self._list.bind("<Double-Button-1>", lambda event:self.on__dblclick(event))

        Label(self._listframe ,  height =2,relief = RAISED,text = 'CONTACTS', background='pink' ,
              font = ('rockwell', 20, 'bold'), borderwidth = 4).pack(side = TOP, fill=X)
        Label(self._listframe , text='    ',relief = RAISED,height = 5, background='pink',
              font = ('script', 20, 'bold'), borderwidth = 4).pack(side=LEFT,fill=BOTH)
        Label(self._listframe ,  relief = RAISED,width = 30, background='pink',
              font = ('script', 20, 'bold'), borderwidth = 4).pack(side=BOTTOM,fill=X)
        self.__comms=Frame(self._listframe, width = 20,relief = RAISED, background='pink',borderwidth = 4)
        self._list.pack(side = LEFT,fill = BOTH)
        self.__comms.pack(side = RIGHT, fill = Y)
        for row, (text, cmd) in  enumerate([('ADD',self.add_contact),
                                            ('DISPLAY',self.display_contact_info)
                                            ,('UPDATE', self.edit_contact),
                                            ('DELETE', self.delete_contact)]):
            tkinter.Button(self.__comms, text = text, width=7,font = ('heveltica', 15, 'bold'),background ='#33FF33',borderwidth =5, command=cmd).grid(
                row = row, column =0 , padx = 4, pady =8)

    def on__dblclick(self, event):
        self.display_contact_info()
        

    def get_contact_names(self):
        #can only be gotten after login so no verification

        with sqlite3.connect('contact_data.db') as dbfile:
            cur = dbfile.cursor()
            cur.execute('SELECT * from contacts')
            table = cur.fetchall()
            #dbfile.close()

        names = []
        for row in table:
            names.append(row[0])
                         
        return sorted(names)
            

    def start_up(self):
        username, password = StringVar(),StringVar()
        if USER_DATA['password'] is not None and USER_DATA['username'] is not None:
            #not First time start up:
            self.set_login_window()
            return

        
        def on_create():
            try:
                assert len(username.get())>=6
                assert len(password.get())>=5
            except AssertionError:
                tkinter.messagebox.showerror('Error', 'Username name is a mandatory and at least  6 characters'
                                             '\n\nPassword must be at least 5 characters')
                return
            USER_DATA['username']=username.get()
            USER_DATA['password']=password.get()
            with sqlite3.connect('contact_data.db') as dbfile:
                 #(ID  INT AUTOINCREMENT  NOT NULL,)
                cursor = dbfile.cursor()
                cursor.execute('''CREATE TABLE Contacts (
                                FULLNAME    TEXT PRIMARY KEY NOT NULL,
                                FIRSTNAME TEXT NOT NULL,
                                SURNAME  TEXT,
                                OTHERNAME TEXT,
                                NICKNAME TEXT,
                                PHONENUMBER CHAR(12) NOT NULL,
                                EMAIL   TEXT,
                                PICTURE TEXT,
                                BIRTHDAY  CHAR(20),
                                TITLE CHAR(5),
                                ADDRESS CHAR(50),
                                CITY TEXT,
                                ENTRYDATE CHAR(20) NOT NULL,
                                WEBSITE  TEXT,
                                CATEGORY TEXT
                                );''')
                dbfile.commit()#keep the changes
            with open('data_file.json', 'w') as file_object:
                json.dump(USER_DATA, file_object)

            tkinter.messagebox.showinfo('Phone Book', 'Database for your contacts has been created successfully')
            frame.grid_forget()
            frame.destroy()
            lab.destroy()
            self.init()

            
        #[first_time_setup]
        #start the database
        #display message of sucees? or failure
        lab=tkinter.Label(self._mainframe, font = ('verdana', 20), relief = RAISED,borderwidth=10
                ,height=3, text =  'PHONE BOOK',background='green')
        lab.pack(side = TOP, fill = X)

        frame = tkinter.Frame(self._mainframe, borderwidth=10, relief=RAISED, background='olive')
        frame.pack(side=LEFT, fill=BOTH)
        #frame.grid(row=0)
        tkinter.Label(frame, foreground='#2020FF',background='olive', font='times 18', text='Username').grid(row=0, column=0, padx=8, pady=8)
        tkinter.Label(frame, foreground='#2020FF', background='olive', font='times 18', text='Password').grid(row=1, column=0, padx=8, pady=8)
        tkinter.Button(frame, background='green', foreground='black', borderwidth=8, relief=RAISED, font='times 18', text='Create New Account', command=on_create).grid(row=3, column=0,columnspan=2, padx=8, pady=8)
        e1=Entry(frame, textvariable = username, width=20, font=('courier new', 17, 'bold')
                 , borderwidth=5, relief=SUNKEN)
        e1.grid(row=0, column=1, padx=8, pady=10)
        e1.focus_set()
        Entry(frame, textvariable = password, width=20, font=('courier new', 17, 'bold'), borderwidth=5, relief=SUNKEN, show='*').grid(row=1, column=1, padx=8, pady=10)


    def delete_contact(self):
        try:
            index = self._list.curselection()
            contact = self._list.get(index)
        except (IndexError, tkinter.TclError):
            tkinter.messagebox.showinfo('Check', 'Select a contact to delete')
            return
        else:
            sure = tkinter.messagebox.askyesnocancel('Warning', f'Are you sure you want to remove\n{contact} from your contacts database', icon =  tkinter.messagebox.WARNING)

        if not sure:
            return
        
        with  sqlite3.connect('contact_data.db') as dbfile:
            cursor = dbfile.cursor()
            #cursor.execute('DELETE from contacts where FULLNAME={};'.format(contact))
            cursor.execute("""DELETE FROM contacts WHERE FULLNAME="{}";""".format(contact))
            dbfile.commit()
        self.contacts_list.remove(contact)
        tkinter.messagebox.showinfo('Success', f'{contact} has been successfully removed from your contacts')
        #self._list.delete(index)
        self.update_listbox()
            
        
    def display_contact_info(self):
        '-first name, last name, surname, phonenumber, email, picture, address, nickname, city, zip code,'
        'title, date of entry, birthday, website, catergories'
        try:
            index = self._list.curselection()
            contact = self._list.get(index)
        except (IndexError, tkinter.TclError):
            tkinter.messagebox.showinfo('Check', 'Select a contact to display details')
            return
        self.get_all()

        with sqlite3.connect('contact_data.db') as connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT * FROM contacts WHERE FULLNAME="{}";""".format(contact))
            #only one match is guaranteed
            details = cursor.fetchone()
            
        #using the order in which the table data was enterd
        #note is same order as data_rerds is
        for attrib, detail in list(zip(self.data_records.keys(), details)):
            self.data_records[attrib].set(detail)
        
        dis_font = ('Imprint MT Shadow', 18, 'underline')
        ent_font = ('Rockwell 16')
        display_win = tkinter.Toplevel(self._window)
        display_win.transient(self._window)
        display_win.iconbitmap('phonebook.ico')
        display_win.resizable(0,0)
        frame = tkinter.Frame(display_win, background='#202000', borderwidth=10, relief=RAISED)
        frame.pack(fill=BOTH)

        Label(frame, text='First Name :',
                    font = dis_font, background='#202000', foreground='#0000FF').grid(row=0, column=0,pady=2)
        Entry(frame, width=12, font=ent_font,state='readonly', background='#eeeeee', textvariable=self.data_records['FIRSTNAME']).grid(row=0, column=1, padx=2, pady=2)

        Label(frame, text='Surname : ',
                    font = dis_font,background='#202000', foreground='#0000FF').grid(row=1, column=0,pady=2)
        Entry(frame, width=12, font=ent_font,state='readonly', background='#eeeeee', textvariable=self.data_records['SURNAME']).grid(row=1, column=1, padx=2, pady=2)

        Label(frame, text='Other Name : ',
                    font = dis_font, background='#202000', foreground='#0000FF').grid(row=2, column=0,pady=2)
        Entry(frame, width=12, font=ent_font,state='readonly', background='#eeeeee', textvariable=self.data_records['OTHERNAME']).grid(row=2, column=1, padx=2, pady=2)

        Label(frame, text='NickName :',anchor=W,
                    font = dis_font, background='#202000', foreground='#0000FF').grid(row=3, column=0,pady=2)
        Entry(frame, width=12, font=ent_font, state='readonly', background='#eeeeee',textvariable=self.data_records['NICKNAME']).grid(row=3, column=1, padx=2, pady=2)

        #picture
        img = Image.open(self.data_records['PICTURE'].get())
        scl = (img.width*200)/img.height
        pic = ImageTk.PhotoImage(img.resize((int(scl), 200)))
        piclab = Label(frame, image=pic, background='white', width=200, height=200)
        piclab.image = pic
        piclab.grid(row=0, column=2,columnspan=2,rowspan=4,pady=2)
        Label(frame, text='This contact was enlisted on {}'.format(self.data_records['ENTRYDATE'].get()),
              font=('Lucida Fax', 20),background='#202000').grid(row=4, column=0, columnspan=4, pady=2, sticky=E)
        #[title] +[bd]
        Label(frame, text='Title: ',anchor=W,
                    font = dis_font, background='#202000', foreground='#0000FF').grid(row=0, column=4,pady=2)
        Entry(frame, width=12, font=ent_font,state='readonly', background='#eeeeee', textvariable=self.data_records['TITLE']).grid(row=0, column=5, padx=2, pady=2)

        Label(frame, text='Birth Day: ',anchor=W,
                    font = dis_font, background='#202000', foreground='#0000FF').grid(row=1, column=4,pady=2)
        Entry(frame, width=12, font=ent_font, state='readonly', background='#eeeeee',textvariable=self.data_records['BIRTHDAY']).grid(row=1, column=5, padx=2, pady=2)

        #[address]

        Label(frame, text='Address: ',anchor=W,
                    font = dis_font, background='#202000', foreground='#0000FF').grid(row=2, column=4,pady=2)
        Entry(frame, width=12, font=ent_font, state='readonly', background='#eeeeee',textvariable=self.data_records['ADDRESS']).grid(row=2, column=5, padx=2, pady=2)


        #[city]
        Label(frame, text='City: ',anchor=W,
                    font = dis_font, background='#202000', foreground='#0000FF').grid(row=3, column=4,pady=2)
        Entry(frame, width=12, font=ent_font,state='readonly', background='#eeeeee', textvariable=self.data_records['CITY']).grid(row=3, column=5, padx=2, pady=2)

        #fullname
        Label(frame, text='Full Name:',anchor=W,justify=LEFT,
                    font = dis_font, background='#202000', foreground='#0000FF').grid(row=5, column=0,pady=4)
        Entry(frame, width=24, font=ent_font,state='readonly', background='#eeeeee', textvariable=self.data_records['FULLNAME']).grid(row=5, column=1,columnspan=2, padx=2, pady=2)

        #phone number
        Label(frame, text='Phone Number:',anchor=W,justify=LEFT,
                    font = dis_font, background='#202000', foreground='#0000FF').grid(row=5, column=3,pady=4)
        Entry(frame, width=24, font=ent_font,state='readonly', background='#eeeeee', textvariable=self.data_records['PHONENUMBER']).grid(row=5, column=4,columnspan=2, padx=2, pady=2)

        #[email]
        Label(frame, text='Email: ',anchor=W,
                    font = dis_font, background='#202000', foreground='#0000FF').grid(row=6, column=0,pady=2)
        Entry(frame, width=24, font=ent_font,state='readonly', background='#eeeeee', textvariable=self.data_records['EMAIL']).grid(row=6, column=1,columnspan=2, padx=2, pady=2)


        #[website
        Label(frame, text='Website: ',anchor=W,justify=LEFT,
                    font = dis_font, background='#202000', foreground='#0000FF').grid(row=6, column=3,pady=2)
        Entry(frame, width=24, font=ent_font,state='readonly', background='#eeeeee', textvariable=self.data_records['WEBSITE']).grid(row=6, column=4, columnspan=2,padx=2, pady=2)


        #[Category of contact
        Label(frame, text='Category of contact: ',anchor=W,
                    font = dis_font, background='#202000', foreground='#0000FF').grid(row=7, column=0, pady=2)
        Entry(frame, width=24, font=ent_font,state='readonly', background='#eeeeee', textvariable=self.data_records['CATEGORY']).grid(row=7, column=1,columnspan=2, padx=2, pady=2)


        #notes or descrition
        Label(frame, text='Note',anchor=W,
                    font = dis_font, background='#202000', foreground='#0000FF').grid(row=7, column=3, pady=2)
        e1=Entry(frame, width=24, font=ent_font, foreground='gray',state='readonly', background='#eeeeee',)
        #e1.insert(0, 'No notes')
        e1.grid(row=7, column=4,columnspan=2, padx=2, pady=2)

        #submit
        display_win.grab_set()


        '''
        disp_win = tkinter.Toplevel(self._window)
        disp_win.resizable(0,0)
        disp_win.transient(self._window)
        disp_win.iconbitmap('phonebook.ico')
        frame = tkinter.Frame(disp_win, background='#002020', borderwidth=10, relief=RAISED)
        frame.pack(fill=BOTH)
        Label(frame, text='This contact was enlisted on {}'.format(self.data_records['ENTRYDATE'].get()),
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=0, column=0,columnspan=2,pady=4)
        Label(frame, text='First Name : {}'.format(self.data_records['FIRSTNAME'].get()),
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=1, column=0,pady=4)
        Label(frame, text='Surname : {}'.format(self.data_records['SURNAME'].get()),
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=2, column=0,pady=4)
        Label(frame, text='OtherName : {}'.format(self.data_records['OTHERNAME'].get()),
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=3, column=0,pady=4)
        Label(frame, text='NickName : {}'.format(self.data_records['NICKNAME'].get()),
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=4, column=0,pady=4)
        #picture
        piclab = Label(frame, image=pic)#, background='pink')
        im=Image.open(self.data_records['PICTURE'].get())
        scl = (im.width*200)/im.height
        im=im.resize((int(scl), 200))
        piclab.image = ImageTk.PhotoImage(im)
        piclab.grid(row=1, column=1,rowspan=4,pady=4)
        #fullname
        Label(frame, text='Full Name: {}'.format(self.data_records['FULLNAME'].get()),
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=5, column=0,columnspan=2,pady=4)
        #[title] +[borderwidth]
        Label(frame, text='Title: {}'.format(self.data_records['TITLE'].get()),
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=6, column=0,pady=4)
        Label(frame, text='BirthDay: {}'.format(self.data_records['BIRTHDAY'].get()),
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=6, column=1,pady=4)
        #[email]+[address]
        Label(frame, text='Email: {}'.format(self.data_records['EMAIL'].get()),
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=7, column=0,pady=4)
        Label(frame, text='Address: {}'.format(self.data_records['ADDRESS'].get()),
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=7, column=1,pady=4)

        #[city]+[zipcode]
        Label(frame, text='City: {}'.format(self.data_records['CITY'].get()),
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=8, column=0,pady=4)

        #[website
        Label(frame, text='Website: {}'.format(self.data_records['WEBSITE'].get()),
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=9, column=0,columnspan=2,pady=4)

        #[Category of contact
        Label(frame, text='Category of contact: {}'.format(self.data_records['CATEGORY'].get()),
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=10, column=0,columnspan=2,pady=4)

        disp_win.grab_set()
        '''

    def update_listbox(self):
        try:
            self._list.delete(0,len(self.contacts_list))
        except tkinter.TclError:
            pass
        for i, it in enumerate(sorted(self.contacts_list)):
            self._list.insert(i, it)

    def get_all(self):
        'sets the values of a particular record to the data_record'
        
        index = self._list.curselection()[0]
        contact = self._list.get(index)

        with sqlite3.connect('contact_data.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM contacts WHERE FULLNAME="{}";""".format(contact))
            res = cursor.fetchone()
           
      
        for i, item in enumerate(self.record):
            self.data_records[item].set(res[i])
        #print('After setting values')
        

    def reset_all(self):
        'resets all values to null fro record'
        for item in self.record:
            if item=='PICTURE':
                self.data_records[item].set('./contacts/default.gif')
            else:
                self.data_records[item].set('')
        

    def tuple_values(self):
        '''
        this method returns the values of the records in the same order in which
        it appears in the data base'''
        #tuple(value.get() for value in [val for val  in self.data_records.values()]))
 
        tup = []
        for item in self.record:
            tup.append(self.data_records[item].get())

        return tuple(tup)
        
    def add_contact(self):
        self.reset_all()
        self.data_records['PICTURE'].set('./contact_images/default.gif')
        def create():
            if self.data_records['FULLNAME'].get() in self.contacts_list:
                tkinter.messagebox.showerror('Error', 'Contact with the same name already exists')
                return
            if len(self.data_records['FIRSTNAME'].get())<2 or len(self.data_records['FIRSTNAME'].get())<2:
                tkinter.messagebox.showerror('Error', 'Names must be at least 2 characters')
                return
            if len(self.data_records['PHONENUMBER'].get()) < 9:
                tkinter.messagebox.showerror('Error', 'Phone Number must be at least 9 digits long')
                return
            if (self.data_records['FIRSTNAME'].get().strip().rstrip() not in self.data_records['FULLNAME'].get().split())\
               or  self.data_records['SURNAME'].get().strip().rstrip() not in self.data_records['FULLNAME'].get().split():
                tkinter.messagebox.showerror('Error', 'First name and Surname must be contained in fullname')
                return
            self.data_records['ENTRYDATE'].set(str(datetime.datetime.now())[:-7])
                
            
            with sqlite3.connect('contact_data.db') as connection:
                cursor = connection.cursor()
                cursor.execute('''INSERT INTO contacts (
                                    FULLNAME  ,
                                    FIRSTNAME ,
                                    SURNAME  ,
                                    OTHERNAME ,
                                    NICKNAME ,
                                    PHONENUMBER ,
                                    EMAIL ,
                                    PICTURE ,
                                    BIRTHDAY,
                                    TITLE ,
                                    ADDRESS ,
                                    CITY ,
                                    ENTRYDATE ,
                                    WEBSITE ,
                                    CATEGORY
                               )values
                               {};
                               '''.format( self.tuple_values()))
                connection.commit()
                self.contacts_list = self.get_contact_names()
                self.contacts_list.sort()
                self.update_listbox()
                self.reset_all()
                tkinter.messagebox.showinfo('Review', 'Contact was successfully created')
                add_win.destroy()
        #update the list box
                

        def browse():
            f = tkinter.filedialog.askopenfilename(title='Select a pic for the contact', filetypes=[('JPEG Images', '*.jpg'),('PNG Image', '*.png')],
                                                   defaultextension='.jpg')
            if f:
                ext = os.path.splitext(f)[-1]
                name=shutil.copy(f, './contact_images/{}{}'.format(self.data_records['FIRSTNAME'].get(), ext))
                self.data_records['PICTURE'].set(name)
                im=Image.open(self.data_records['PICTURE'].get())
                scl = (im.width*200)/im.height
                im=im.resize((int(scl), 200))
                pic = ImageTk.PhotoImage(im)
                piclab.configure(image=pic)
                piclab.image = pic
            else:
                tkinter.messagebox.showinfo('Reminder', 'Note:\nYou did not select any photo')
  

        #gui
        dis_font = ('Imprint MT Shadow', 18, 'underline')
        ent_font = ('Rockwell 16')
        add_win = tkinter.Toplevel(self._window)
        add_win.transient(self._window)
        add_win.iconbitmap('phone1.ico')
        add_win.resizable(0,0)
        frame = tkinter.Frame(add_win, background='#002020', borderwidth=10, relief=RAISED)
        frame.pack(fill=BOTH)

        Label(frame, text='First Name :',
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=0, column=0,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['FIRSTNAME']).grid(row=0, column=1, padx=2, pady=2)

        Label(frame, text='Surname : ',
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=1, column=0,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['SURNAME']).grid(row=1, column=1, padx=2, pady=2)

        Label(frame, text='Other Name : ',
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=2, column=0,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['OTHERNAME']).grid(row=2, column=1, padx=2, pady=2)

        Label(frame, text='NickName :',anchor=W,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=3, column=0,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['NICKNAME']).grid(row=3, column=1, padx=2, pady=2)

        #picture
        pic = ImageTk.PhotoImage(Image.open(self.data_records['PICTURE'].get()).resize((200, 200)))
        piclab = Label(frame, image=pic, background='white', width=200, height=200)
        piclab.image = pic
        piclab.grid(row=0, column=2,columnspan=2,rowspan=4,pady=2)
        Label(frame, text='Click here to change Photo for this contact', font='times 16', foreground='burlywood', background='#002020').grid(row=4,column=0, columnspan=3, pady=4)
        Button(frame, text='Browse', command=browse, relief=RAISED, borderwidth=4, background='#AA8080',font=dis_font).grid(row=4, column=3, padx=7, pady=5)


        #[title] +[bd]
        Label(frame, text='Title: ',anchor=W,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=0, column=4,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['TITLE']).grid(row=0, column=5, padx=2, pady=2)

        Label(frame, text='Birth Day: ',anchor=W,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=1, column=4,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['BIRTHDAY']).grid(row=1, column=5, padx=2, pady=2)

        #[address]

        Label(frame, text='Address: ',anchor=W,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=2, column=4,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['ADDRESS']).grid(row=2, column=5, padx=2, pady=2)


        #[city]
        Label(frame, text='City: ',anchor=W,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=3, column=4,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['CITY']).grid(row=3, column=5, padx=2, pady=2)

        #fullname
        Label(frame, text='Full Name:',anchor=W,justify=LEFT,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=5, column=0,pady=4)
        Entry(frame, width=24, font=ent_font, textvariable=self.data_records['FULLNAME']).grid(row=5, column=1,columnspan=2, padx=2, pady=2)

        #phone number
        Label(frame, text='Phone Number:',anchor=W,justify=LEFT,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=5, column=3,pady=4)
        Entry(frame, width=24, font=ent_font, textvariable=self.data_records['PHONENUMBER']).grid(row=5, column=4,columnspan=2, padx=2, pady=2)

        #[email]
        Label(frame, text='Email: ',anchor=W,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=6, column=0,pady=2)
        Entry(frame, width=24, font=ent_font, textvariable=self.data_records['EMAIL']).grid(row=6, column=1,columnspan=2, padx=2, pady=2)


        #[website
        Label(frame, text='Website: ',anchor=W,justify=LEFT,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=6, column=3,pady=2)
        Entry(frame, width=24, font=ent_font, textvariable=self.data_records['WEBSITE']).grid(row=6, column=4, columnspan=2,padx=2, pady=2)


        #[Category of contact
        Label(frame, text='Category of contact: ',anchor=W,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=7, column=0, pady=2)
        Entry(frame, width=24, font=ent_font, textvariable=self.data_records['CATEGORY']).grid(row=7, column=1,columnspan=2, padx=2, pady=2)


        #notes or descrition
        Label(frame, text='Note',anchor=W,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=7, column=3, pady=2)
        e1=Entry(frame, width=24, font=ent_font, foreground='gray')
        e1.insert(0, 'Notes or description here')
        e1.grid(row=7, column=4,columnspan=2, padx=2, pady=2)

        #submit
        Button(frame,text='CREATE CONTACT', background='black', foreground='#AAFFFF', command=create, borderwidth=10, relief=RAISED, font='times 20').grid(row=8, column=2, columnspan=2)

        add_win.grab_set()
        

        
        #end of gui


    def edit_contact(self):
        try:
            self.get_all()
        except (tkinter.TclError, IndexError):
            tkinter.messagebox.showinfo('Reminder', 'Choose a contact you want to update:edit')
            return
        def update():
            if len(self.data_records['PHONENUMBER'].get()) < 9:
                tkinter.messagebox.showerror('Error', 'Phone Number must be at least 9 digits long')
                return
            
            with sqlite3.connect('contact_data.db') as connection:
                cursor = connection.cursor()
                values = self.tuple_values()
                print('\nUPDATING\n')
                for key, new_item in list(zip(self.record[3:],values[3:] )):
                    cursor.execute("""UPDATE contacts SET {}="{}" WHERE FULLNAME="{}";""".format(key, new_item , values[0]))
                connection.commit()

                #
                #cursor.execute(
                '''UPDATE {}={} where FULLNAME={} (
                                    FULLNAME  ,
                                    FIRSTNAME ,
                                    SURNAME  ,
                                    OTHERNAME ,
                                    NICKNAME ,
                                    PHONENUMBER ,
                                    EMAIL ,
                                    PICTURE ,
                                    BIRTHDAY,
                                    TITLE ,
                                    ADDRESS ,
                                    CITY ,
                                    ENTRYDATE ,
                                    WEBSITE ,
                                    CATEGORY
                               )values
                               {};'''
                              # .format( self.tuple_values()))
                connection.commit()
                self.contacts_list = self.get_contact_names()
                self.contacts_list.sort()
                self.update_listbox()
                self.reset_all()
                tkinter.messagebox.showinfo('Review', 'Contact was successfully updated')
                edit_win.destroy()
        #update the list box
                

        def browse():
            f = tkinter.filedialog.askopenfilename(title='Select a pic for the contact', filetypes=[('JPEG Images', '*.jpg'),('PNG Image', '*.png')],
                                                   defaultextension='.jpg')
            if f:
                ext = os.path.splitext(f)[-1]
                try:
                    old = './contact_images/{}'.format(self.data_records['FIRSTNAME'].get())
                    os.remove(glob.glob(f'{old}.*')[0])
                except (FileNotFoundError, IndexError):
                    pass
        
                name=shutil.copy(f, './contact_images/{}{}'.format(self.data_records['FIRSTNAME'].get(), ext))
                self.data_records['PICTURE'].set(name)
                im=Image.open(self.data_records['PICTURE'].get())
                scl = (im.width*200)/im.height
                im=im.resize((int(scl), 200))
                pic = ImageTk.PhotoImage(im)
                piclab.configure(image=pic)
                piclab.image = pic
            else:
                tkinter.messagebox.showinfo('Reminder', 'Note:\nYou did not select any photo')
  

        #gui
        dis_font = ('Imprint MT Shadow', 18, 'underline')
        ent_font = ('Rockwell 16')
        edit_win = tkinter.Toplevel(self._window)
        edit_win.transient(self._window)
        edit_win.iconbitmap('phone1.ico')
        edit_win.resizable(0,0)
        frame = tkinter.Frame(edit_win, background='#200020', borderwidth=10, relief=RAISED)
        frame.pack(fill=BOTH)

        Label(frame, text='First Name :',
                    font = dis_font, background='#200020', foreground='#CC0000').grid(row=0, column=0,pady=2)
        Entry(frame, width=12, font=ent_font,state='readonly', textvariable=self.data_records['FIRSTNAME']).grid(row=0, column=1, padx=2, pady=2)

        Label(frame, text='Surname : ',
                    font = dis_font, background='#200020', foreground='#CC0000').grid(row=1, column=0,pady=2)
        Entry(frame, width=12, font=ent_font,state='readonly', textvariable=self.data_records['SURNAME']).grid(row=1, column=1, padx=2, pady=2)

        Label(frame, text='Other Name : ',
                    font = dis_font, background='#200020', foreground='#CC0000').grid(row=2, column=0,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['OTHERNAME']).grid(row=2, column=1, padx=2, pady=2)

        Label(frame, text='NickName :',anchor=W,
                    font = dis_font, background='#200020', foreground='#CC0000').grid(row=3, column=0,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['NICKNAME']).grid(row=3, column=1, padx=2, pady=2)

        #picture
        img2 = Image.open(self.data_records['PICTURE'].get())
        scl = (img2.width*200)/img2.height
        pic2 = ImageTk.PhotoImage(img2.resize((int(scl), 200)))
        piclab = Label(frame, image=pic2, background='white', width=200, height=200)
        piclab.image = pic2
        piclab.grid(row=0, column=2,columnspan=2,rowspan=4,pady=2)
        Label(frame, text='Click here to change Photo for this contact', font='times 16', foreground='burlywood', background='#002020').grid(row=4,column=0, columnspan=3, pady=4)
        Button(frame, text='Browse', command=browse, relief=GROOVE, borderwidth=6, background='#AA2020',font=dis_font).grid(row=4, column=3, padx=7, pady=5)


        #[title] +[bd]
        Label(frame, text='Title: ',anchor=W,
                    font = dis_font, background='#200020', foreground='#CC0000').grid(row=0, column=4,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['TITLE']).grid(row=0, column=5, padx=2, pady=2)

        Label(frame, text='Birth Day: ',anchor=W,
                    font = dis_font, background='#200020', foreground='#CC0000').grid(row=1, column=4,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['BIRTHDAY']).grid(row=1, column=5, padx=2, pady=2)

        #[address]

        Label(frame, text='Address: ',anchor=W,
                    font = dis_font, background='#200020', foreground='#CC0000').grid(row=2, column=4,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['ADDRESS']).grid(row=2, column=5, padx=2, pady=2)


        #[city]
        Label(frame, text='City: ',anchor=W,
                    font = dis_font, background='#200020', foreground='#CC0000').grid(row=3, column=4,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['CITY']).grid(row=3, column=5, padx=2, pady=2)

        #fullname
        Label(frame, text='Full Name:',anchor=W,justify=LEFT,
                    font = dis_font, background='#200020', foreground='#CC0000').grid(row=5, column=0,pady=4)
        Entry(frame, width=24, font=ent_font,state='readonly', textvariable=self.data_records['FULLNAME']).grid(row=5, column=1,columnspan=2, padx=2, pady=2)

        #phone number
        Label(frame, text='Phone Number:',anchor=W,justify=LEFT,
                    font = dis_font, background='#200020', foreground='#CC0000').grid(row=5, column=3,pady=4)
        Entry(frame, width=24, font=ent_font, textvariable=self.data_records['PHONENUMBER']).grid(row=5, column=4,columnspan=2, padx=2, pady=2)

        #[email]
        Label(frame, text='Email: ',anchor=W,
                    font = dis_font, background='#200020', foreground='#CC0000').grid(row=6, column=0,pady=2)
        Entry(frame, width=24, font=ent_font, textvariable=self.data_records['EMAIL']).grid(row=6, column=1,columnspan=2, padx=2, pady=2)


        #[website
        Label(frame, text='Website: ',anchor=W,justify=LEFT,
                    font = dis_font, background='#200020', foreground='#CC0000').grid(row=6, column=3,pady=2)
        Entry(frame, width=24, font=ent_font, textvariable=self.data_records['WEBSITE']).grid(row=6, column=4, columnspan=2,padx=2, pady=2)


        #[Category of contact
        Label(frame, text='Category of contact: ',anchor=W,
                    font = dis_font, background='#200020', foreground='#CC0000').grid(row=7, column=0, pady=2)
        Entry(frame, width=24, font=ent_font, textvariable=self.data_records['CATEGORY']).grid(row=7, column=1,columnspan=2, padx=2, pady=2)


        #notes or descrition
        Label(frame, text='Note',anchor=W,
                    font = dis_font, background='#200020', foreground='#CC0000').grid(row=7, column=3, pady=2)
        e1=Entry(frame, width=24, font=ent_font, foreground='gray')
        e1.insert(0, 'Notes or description here')
        e1.grid(row=7, column=4,columnspan=2, padx=2, pady=2)

        #submit
        Button(frame,text='UPDATE CONTACT', background='#207720', foreground='#FFAAFF', command=update, borderwidth=10, relief=GROOVE, font='times 20').grid(row=8, column=2, columnspan=2)

        edit_win.grab_set()
        

        

        '''
        dis_font = ('Imprint MT Shadow', 18, 'underline')
        ent_font = ('Rockwell 16')
        add_win = tkinter.Toplevel(self._window)
        add_win.transient(self._window)
        add_win.resizable(0,0)
        frame = tkinter.Frame(add_win, background='#002020', borderwidth=10, relief=RAISED)
        frame.pack(fill=BOTH)

        Label(frame, text='First Name :',
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=0, column=0,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['FIRSTNAME']).grid(row=0, column=1, padx=2, pady=2)

        Label(frame, text='Surname : ',
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=1, column=0,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['SURNAME']).grid(row=1, column=1, padx=2, pady=2)

        Label(frame, text='Other Name : ',
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=2, column=0,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['OTHERNAME']).grid(row=2, column=1, padx=2, pady=2)

        Label(frame, text='NickName :',anchor=W,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=3, column=0,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['NICKNAME']).grid(row=3, column=1, padx=2, pady=2)

        #picture
        pic = ImageTk.PhotoImage(Image.open(self.data_records['PICTURE'].get()).resize((200, 200)))
        piclab = Label(frame, image=pic, background='white')
        piclab.image = pic
        piclab.grid(row=0, column=2,columnspan=2,rowspan=4,pady=2)
        Label(frame, text='Click here to change Photo for this contact', font='times 16', foreground='burlywood', background='#002020').grid(row=4,column=0, columnspan=3, pady=4)
        Button(frame, text='Browse', command=browse, relief=RAISED, borderwidth=6, background='#AA2020',font=dis_font).grid(row=4, column=3, padx=7, pady=5)


        #[title] +[borderwidth]
        Label(frame, text='Title: ',anchor=W,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=0, column=4,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['TITLE']).grid(row=0, column=5, padx=2, pady=2)

        Label(frame, text='Birth Day: ',anchor=W,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=1, column=4,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['BIRTHDAY']).grid(row=1, column=5, padx=2, pady=2)

        #[address]

        Label(frame, text='Address: ',anchor=W,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=2, column=4,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['ADDRESS']).grid(row=2, column=5, padx=2, pady=2)


        #[city]
        Label(frame, text='City: ',anchor=W,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=3, column=4,pady=2)
        Entry(frame, width=12, font=ent_font, textvariable=self.data_records['CITY']).grid(row=3, column=5, padx=2, pady=2)

        #fullname
        Label(frame, text='Full Name:',anchor=W,justify=LEFT,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=5, column=0,pady=4)
        Entry(frame, width=24, font=ent_font, textvariable=self.data_records['FULLNAME']).grid(row=5, column=1,columnspan=2, padx=2, pady=2)

        #phone number
        Label(frame, text='Phone Number:',anchor=W,justify=LEFT,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=5, column=3,pady=4)
        Entry(frame, width=24, font=ent_font, textvariable=self.data_records['PHONENUMBER']).grid(row=5, column=4,columnspan=2, padx=2, pady=2)

        #[email]
        Label(frame, text='Email: ',anchor=W,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=6, column=0,pady=2)
        Entry(frame, width=24, font=ent_font, textvariable=self.data_records['EMAIL']).grid(row=6, column=1,columnspan=2, padx=2, pady=2)


        #[website
        Label(frame, text='Website: ',anchor=W,justify=LEFT,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=6, column=3,pady=2)
        Entry(frame, width=24, font=ent_font, textvariable=self.data_records['WEBSITE']).grid(row=6, column=4, columnspan=2,padx=2, pady=2)


        #[Category of contact
        Label(frame, text='Category of contact: ',anchor=W,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=7, column=0, pady=2)
        Entry(frame, width=24, font=ent_font, textvariable=self.data_records['CATEGORY']).grid(row=7, column=1,columnspan=2, padx=2, pady=2)


        #notes or descrition
        Label(frame, text='Note',anchor=W,
                    font = dis_font, background='#002020', foreground='#0000FF').grid(row=7, column=3, pady=2)
        e1=Entry(frame, width=24, font=ent_font, foreground='gray')
        e1.insert(0, 'Notes or description here')
        e1.grid(row=7, column=4,columnspan=2, padx=2, pady=2)

        #submit
        Button(frame,text='CREATE CONTACT', background='black', foreground='#AAFFFF', command=create, borderwidth=10, relief=RAISED, font='times 20').grid(row=8, column=2, columnspan=2)

        add_win.grab_set()'''
        

  

    def about_app(self):
        about_win = tkinter.Toplevel()
        about_win.transient(self._window)
        about_win.wm_iconbitmap('phone1.ico')
        about_win.resizable(False, False)
        
        developer_frame = tkinter.Frame(about_win, background='skyblue', borderwidth=5
                                        , relief = SUNKEN)
        #picture of developer
        #p = Image.open('developer.jpg').resize((200, 200)).convert('RGB')
        self.img = ImageTk.PhotoImage(Image.open('user.png').resize((175, 200)).convert('RGB'))
        Label(developer_frame, image = self.img).grid(
            row=0, column=0, rowspan = 5)
        for num, text in enumerate(['Nfor Glen Yinyu(JG)', 'Developed in Python']):
            Label(developer_frame, text=text, foreground = 'brown', font = ('courier new',15, 'bold italic underline')).grid(row=num, column=1)
        appinfo_frame = tkinter.Frame(about_win, background='skyblue', borderwidth=5,
                                      relief = SUNKEN)
        msg = 'The PHONEBOOK PyPHONY is a simple desktop app developed to manage contacts '\
        'for a user.\nSimple and easy to use\nStill under developement\n\nThis App will be useful if you lose your phone contacts'
        def help_():
            tkinter.messagebox.showinfo('Learn More', msg)
        Button(developer_frame, text='LEARN MORE', font='cambria 28', command=help_).grid(
            row=6, column=0, columnspan=2)
        developer_frame.pack()
        about_win.grab_set()

    def run(self):
        'run the main loop'
        self._window.mainloop()

    def _exitApp(self):
        self._window.quit()
        self._window.destroy()
        sys.exit()


#modify to 
if __name__ == '__main__':
    USER_DATA={
        'password':None,
        'username':None,
        }
    try:
        with open('data_file.json' , 'r') as data:
            USER_DATA = json.load(data)
    except (FileNotFoundError):
        '''means data is corrupted or its first time launch'''
        #[Handle appropriately]
        pass
    except (ValueError):
        root = Tk()
        root.withdraw()
        tkinter.messagebox.showerror('FATAL ERROR', 'Appliaction Data has been Corrupted\n\nUninstall immediately and reinstall')
        root.destroy()
        sys.exit()
        exit()
    else:
        PhoneBook().run()


