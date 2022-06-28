from tkinter import *

from tkinter import messagebox

window = Tk()

window.title("Welome to techBOT portal!")

window.geometry('800x800')

def clicked():

    messagebox.showwarning('Message title', 'This is an Urgent Message')
    messagebox.showwarning('Message title', 'We Have Detected a Malware !')
    res = messagebox.askyesno('Message title','Would you like help?')

btn = Button(window,text='Click here', command=clicked)

btn.grid(column=10,row=10)



window.mainloop()
