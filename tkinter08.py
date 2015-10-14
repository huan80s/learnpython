# coding:utf-8
from Tkinter import *
import Dialog
def xin():
    d = Dialog(None, {'title': 'File Modified',
                      'text':
                      'File "Python.h" has been modified'
                      ' since the last time it was saved.'
                      ' Do you want to save it before'                              
                      ' exiting the application.',
                      'bitmap': DIALOG_ICON,
                      'default': 0,
                      'strings': ('Save File',
                          'Discard Changes',
                          'Return to Editor')})

    print(d.num)

t=Button(None,text='whoo调查',command=xin)
t.pack()
b=Button(None,text='关闭',command=t.quit)
b.pack()
t.mainloop()

