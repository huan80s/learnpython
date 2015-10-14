# -*- coding:utf-8 -*-
from Tkinter import *
import tkMessageBox

# 从Frame派生Application
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.creatWidgets()

    def creatWidgets(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.alertButton=Button(self,text='Hello',command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name=self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message','Hello,%s'%name)

app=Application()
#设置窗口标题
app.master.title('Hello world')
#主消息循环
app.mainloop()
