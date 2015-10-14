# -*- coding:utf-8 -*-
from Tkinter import *

def xinlabel():
    global root
    s=Label(root,text="我爱python")
    s.pack()

root = Tk()
b1=Button(root,text='whoo',command=xinlabel)
b1['background']='red'
b1.pack()

root.mainloop()
