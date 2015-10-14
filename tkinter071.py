# coding:utf-8
from Tkinter import *

def xin():
    global root
    Label(root,text='I love python').pack()

root=Tk()
menubar=Menu(root)

for x in ['vb','c','php']:
    menubar.add_command(label=x)

menubar.add_command(label='python',command=xin)

def pop(event):
    menubar.post(event.x_root,event.y_root)

root.bind("<Button-3>",pop)
root.mainloop()

