from tkinter import *
import pygame, os, random
pygame.mixer.init()
songs = (pygame.mixer.music.load("A.mp3"),
     pygame.mixer.music.load("B.mp3"),
     pygame.mixer.music.load("C.mp3"),
     pygame.mixer.music.load("D.mp3"))
window=Tk()
window.geometry("175x150")
class Player:
    def __init__(self):
        pass
    def play(init):
        selected_song = random.choice(songs)
        #pygame.mixer.music.play(selected_song) #uncomment this
        print(selected_song) #comment this
        return selected_song

a = Player()
l1=Label(window,text="Music Player",font="times 20")
l1.grid(row=1,column=1)

b1=Button(window,text="Play",width=20,command=a.play)
b1.grid(row=4,column=1)
b2=Button(window,text="Pause",width=20,command=stop)

#song_list=os.listdir()
#song_listbox=StringVar(window)
#song_listbox.set("select songs")
#menu=OptionMenu(window,song_listbox,*song_list)
#menu.grid(row=4,column=4)
window.mainloop()