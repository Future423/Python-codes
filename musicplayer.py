#Before starting, install pygame and mutagen
import os # to fetch songs and directories
from tkinter.filedialog import askdirectory # for selecting our song directory
import pygame # for playing music
from mutagen.id3 import ID3 # For tagging the meta data to our songs
from tkinter import * # for UI
from PIL import ImageTk, Image

root = Tk() # creates an Empty window
root.title("LN MUSIC PLAYER")

root.geometry("600x400+10+10")
root.config(bg="#ccb2e5")
root.minsize(800,400) # set size as 300 x 300 wide, Change this accordingly

listofsongs=[]
realnames=[]
global index
index=0

def directorychooser():
    directory=askdirectory()
    os.chdir(directory)
    for file in os.listdir(directory):
    	if file.endswith('.mp3'):
    		realdir=os.path.realpath(file)
    		audio=ID3(realdir)
    		realnames.append(audio['TIT2'].text[0])
    		listofsongs.append(file)
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

def stopsong(event):
    pygame.mixer.music.stop()

def nextsong(event):
    global index
    try:
        index=index+1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
    except IndexError:
        index=0
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()

def prevsong(event):
    global index
    try:
        index=index-1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
    except IndexError:
        index=len(listofsongs)-1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
def playsong(event):
    pygame.mixer.music.unpause()

def pausesong(event):
    pygame.mixer.music.pause()

def forward(event):
    try:
        t=pygame.mixer.music.get_pos()
        pygame.mixer.music.set_pos((t/500)+10)
    except:
        nextsong(event)

def rewind(event):
    try:
        t=pygame.mixer.music.get_pos()
        pygame.mixer.music.set_pos((t/1000)-20)
    except:
        prevsong(event)
def volup(event):
    t=pygame.mixer.music.get_volume()
    if t>=0.0 and t<0.9:
        pygame.mixer.music.set_volume(t+0.1)

def voldown(event):
    t=pygame.mixer.music.get_volume()
    if t>0.1 and t<=1.0:
        pygame.mixer.music.set_volume(t-0.1)

def mut(event):
    pygame.mixer.music.set_volume(0.01)

label=Label(root,text='LN Music Player',width=20,font=('arial',28,'bold'),background='cadet blue',fg='gold')
label.pack()

directorychooser()

listbox=Listbox(root,width=65,font=('arial',10,'bold'),background='#a0b4fa',fg='#ee7600')
listbox.pack()

realnames.reverse()
print(realnames)
for items in realnames:
    listbox.insert(0,items)

nextbutton = Button(root,text = '>>|',width = 16,font=('Monotype Corsiva',16,"bold"),fg="blue",background="#c0ffee")
nextbutton.place(x=500,y=290)

previousbutton = Button(root,text = '|<<',width=16,font=('Monotype Corsiva',16,"bold"),fg="blue",background="#c0ffee")
previousbutton.place(x=60,y=290)

stopbutton = Button(root,text='Stop Music',width=26,font=('Monotype Corsiva',16,"bold"),fg="blue",background="#c0ffee")
stopbutton.place(x=220,y=350)

pausebutton=Button(root,text='||',width=16,font=('Monotype Corsiva',16,"bold"),fg='blue',background="#c0ffee")
pausebutton.place(x=280,y=235)

playbutton=Button(root,text='>',width=16,font=('Monotype Corsiva',16,"bold"),fg='blue',background="#c0ffee")
playbutton.place(x=280,y=290)

fwdbutton=Button(root,text='>>',width=16,font=('Monotype Corsiva',16,"bold"),fg='blue',background="#c0ffee")
fwdbutton.place(x=500,y=235)

rwdbutton=Button(root,text='<<',width=16,font=('Monotype Corsiva',16,"bold"),fg='blue',background="#c0ffee")
rwdbutton.place(x=60,y=235)

volumeup=Button(root,text='Vol Up',width=8,font=('Monotype Corsiva',16,"bold"),fg='blue',background="#c0ffee")
volumeup.place(x=650,y=30)

volumedown=Button(root,text='Vol Down',width=8,font=('Monotype Corsiva',16,"bold"),fg='blue',background="#c0ffee")
volumedown.place(x=650,y=85)

mute=Button(root,text='Mute',width=8,font=('Monotype Corsiva',16,"bold"),fg='blue',background="#c0ffee")
mute.place(x=650,y=140)

stopbutton.bind("<Button-1>",stopsong)
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
pausebutton.bind("<Button-1>",pausesong)
playbutton.bind("<Button-1>",playsong)
fwdbutton.bind("<Button-1>",forward)
rwdbutton.bind("<Button-1>",rewind)
volumeup.bind("<Button-1>",volup)
volumedown.bind("<Button-1>",voldown)
mute.bind("<Button-1>",mut)

root.mainloop()