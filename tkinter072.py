# coding:utf-8
from Tkinter import *

root=Tk()
m=Menu(root)

m2=Menu(m)
for x in ['python','perl','php','ruby']:
    #m2.add_command(label=x)
    m2.add_checkbutton(label=x)

m2.add_separator()

for x in ['java','c++','c']:
    #m2.add_command(label=x)
    m2.add_radiobutton(label=x)

m.add_cascade(label='lan',menu=m2)

root['menu']=m
root.mainloop()
