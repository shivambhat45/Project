import sys
# sys.stdin=open('input.in','r')
# sys.stdout=open('output.out','w')

from tkinter import *
import tkinter.messagebox
import backend
import sqlite3
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title('Republic Day Celebration')
        root.iconbitmap('download_.ico')

        Admissionnumber=StringVar()
        Firstname=StringVar()
        Lastname=StringVar()
        Class=StringVar()
        Rollno=StringVar()

        def cleardata():
            self.e0.delete(0,END)
            self.e1.delete(0,END)
            self.e2.delete(0,END)
            self.e3.delete(0,END)
            self.e4.delete(0,END)
        def adddata():
            if(self.e0.get()!=0):
                backend.submit(self.e0.get(),self.e1.get(),self.e2.get(),self.e3.get(),self.e4.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(self.e0.get(),self.e1.get(),self.e2.get(),self.e3.get(),self.e4.get())) 


        def display():
            studentlist.delete(0,END)
            for row in backend.viewdata():
                studentlist.insert(END,row,str(''))

        studentlist=Listbox(width=40,height=15)
        studentlist.grid(row=11,column=1)

        self.l0=Label(root,text='AdmissionNumber:')
        self.l0.grid(row=0)
        self.l1=Label(root,text='First Name:')
        self.l1.grid(row=1)
        self.l2=Label(root,text='Last Name:')
        self.l2.grid(row=2)
        self.l3=Label(root,text='Class:')
        self.l3.grid(row=3)
        self.l4=Label(root,text='Rollno:')
        self.l4.grid(row=4)


        self.e0=Entry(root,width=30,borderwidth=5)
        self.e0.grid(row=0,column=1)
        self.e1=Entry(root,width=30,borderwidth=5)
        self.e1.grid(row=1,column=1)
        self.e2=Entry(root,width=30,borderwidth=5)
        self.e2.grid(row=2,column=1)
        self.e3=Entry(root,width=30,borderwidth=5)
        self.e3.grid(row=3,column=1)
        self.e4=Entry(root,width=30,borderwidth=5)
        self.e4.grid(row=4,column=1)


        self.button1=Button(root,text='Submit',width=20,command=adddata)
        self.button1.grid(row=7,column=1,pady=20,columnspan=3)

        self.b2=Button(root,text='Show Record',width=20,command=display)
        self.b2.grid(row=8,column=1,pady=10,columnspan=3)

        self.b3=Button(root,text='Clear Data',width=20,command=cleardata)
        self.b3.grid(row=9,column=1,pady=20,columnspan=3)
            

if __name__=='__main__':
    root=Tk()
    application=Student(root)
    root.mainloop()