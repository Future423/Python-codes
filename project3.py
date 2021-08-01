import googletrans 
from tkinter import *
from tkinter import ttk,messagebox
import textblob

def tris():
    global lang
    try:
        t=googletrans.Translator()
        translated=t.translate(text=text1.get(1.0, END),
                               src = com1.get(),dest = com2.get())
        text2.delete(1.0, END)
        text2.insert(END, translated.text)        

    except Exception as e:
        messagebox.showerror("googletrans","please try again")
        

root=Tk()
root.minsize(1200,500)
root.maxsize(1200,500)
root.wm_iconbitmap("Firstfear.ico")
root.title('Translator by Nishnat')
root.configure(background="SlateBlue4")
l1=Label(root,text='Python Project - Language Translator',bg='SlateBlue4'
         ,fg='white',padx=3,pady=10, font='ArialRoundedMTBold 30 bold')
l1.pack()

mnfrm=Frame(root,bg='gainsboro')
mnfrm.place(x=23,y=80,width=1150,height=400)

lang=googletrans.LANGUAGES
lanV=list(lang.values())
lan1=lang.keys

com1=ttk.Combobox(root,values=lanV,font='CouriesNew 14',state='r',)
com1.place(x=50,y=130)
com1.set("english")

f=Frame(root)
f.place(x=50,y=200,width=440,height=210)
text1=Text(f,font="CouriesNew 24",bg="white",
           relief=GROOVE, wrap=WORD,borderwidth=3)
text1.place(x=0,y=0,width=440,height=210)
scr=Scrollbar(f)
scr.pack(side='right',fill='y')
scr.configure(command=text1.yview)
text1.configure(yscrollcommand=scr.set)

com2=ttk.Combobox(root,values=lanV,font='CouriesNew 14',state='r')
com2.place(x=880,y=130)
com2.set("Select Language")

f1=Frame(root)
f1.place(x=700,y=200,width=440,height=210)
text2=Text(f1,font="CouriesNew 24",bg="white",
           relief=GROOVE, wrap=WORD,borderwidth=3)
text2.place(x=0,y=0,width=440,height=210)
scr1=Scrollbar(f1)
scr1.pack(side='right',fill='y')
scr1.configure(command=text2.yview)
text2.configure(yscrollcommand=scr1.set)
foo = ("Comic Sans MS",21)
trans=Button(root,text='Translate',font=foo,command=tris)
trans.place(x=520,y=220)

ent=Label(root,text ="Enter Text", font = "CouriesNew 16", bg ='gainsboro')
ent.place(x=50,y=165)
out=Label(root,text ="Output", font = "CouriesNew 16", bg ='gainsboro')
out.place(x=700,y=165)
fie=("Baskerville Old Face", 35)
hed=Label(root,text ="Language Translator", font = fie, bg ='gainsboro')
hed.place(x=420,y=90)

imag=PhotoImage(file="nishu.png")
imglab=Label(mnfrm,image=imag,width=193,height=150)
imglab.place(x=475,y=220)

root.mainloop()

