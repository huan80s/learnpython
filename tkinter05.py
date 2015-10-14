# coding:utf-8
#Button练习
from Tkinter import *

def xinlabel(event):
    global root
    s=Label(root,text='Tkinter ,值得关注')
    s.pack()

root=Tk()
t=Label(root,text='模拟按钮')
t.bind('<Button-1>',xinlabel)
t.pack()

root.mainloop()
