from pygame import mixer
from tkinter import *

app = Tk()
app.title("Music Player")

def music():
    mixer.init()
    mixer.music.load("C:\\Users\\Lenovo\\OneDrive\\Masaüstü\\projeler\\tepki.mp3")
    mixer.music.play()

Button(app,text="Music Play",command=music).pack()

app.mainloop()