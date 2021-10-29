from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import Utilities as ut

class NewWindow(Toplevel):

    def __init__(self, master = None,title="ANIME"):

        super().__init__(master = master)
        self.title(title)
        self.geometry("1000x800")
        self.resizable(False,True)
        dictr=ut.load(1)
        action=ut.getAnime_list(dictr,"Ecchi")
        height = 21
        for i in range(0,height):
            if i==0:
                tk.Label(self,height=2,width=64,text="Anime_Name", borderwidth=0.5, relief="solid").grid(row=i+1, column=0)
                tk.Label(self,height=2,width=15,text="Score", borderwidth=0.5, relief="solid").grid(row=i+1, column=1)
                tk.Label(self,height=2,width=63,text="Genre", borderwidth=0.5, relief="solid").grid(row=i+1, column=2)
            else:
                anime=ut.getAnime_data(action,i-1)
                tk.Label(self,height=2,width=64,text=ut.getName(anime), borderwidth=0.5, relief="solid").grid(row=i+1, column=0)
                tk.Label(self,height=2,width=15,text=ut.getScore(anime), borderwidth=0.5, relief="solid").grid(row=i+1, column=1)
                tk.Label(self,height=2,width=63,text=ut.getGenere(anime), borderwidth=0.5, relief="solid").grid(row=i+1, column=2)




# creates a Tk() object
master = Tk()
 
# sets the geometry of
# main root window
master.geometry("200x200")
 
label = Label(master, text ="This is the main window")
label.pack(side = TOP, pady = 10)
 
# a button widget which will
# open a new window on button click
btn = Button(master,
             text ="Click to open a new window")
 
# Following line will bind click event
# On any click left / right button
# of mouse a new window will be opened
btn.bind("<Button>",lambda e: NewWindow(master,title="Action"))
 
btn.pack(pady = 10)
 
# mainloop, runs infinitely
mainloop()