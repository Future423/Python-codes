from tkinter import *
root = Tk()
root.geometry("220x150")
root.title('Nishant')
def update():
    print("GUI Updated")
    root.geometry(f"{width.get()}x{height.get()}")

width=StringVar()
height=StringVar()
Label(root, text="Width",padx=8,pady=8,font='comicsansms 16').grid()
Label(root, text="Height",font='comicsansms 16 ').grid(row=1)
Entry(root, textvariable=width).grid(row=0,column=1)
Entry(root, textvariable=height).grid(row=1,column=1)
Button(root, text='Apply',font='comicsansms 12',command=update).grid(row=2,column=1)
root.mainloop()
