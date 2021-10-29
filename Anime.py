from tkinter import *
import tkinter as tk
import Utilities as ut


########################################################################################################################
class NewWindow(Toplevel):

    def __init__(self, master=None, title="ANIME",num=0):

        super().__init__(master=master)
        self.title(title)
        self.geometry("1000x800")
        self.resizable(False, True)
        data_dtr = ut.load(num)
        self.data = ut.getAnime_list(data_dtr, title)
        for i in range(0, 21):
            if i == 0:
                tk.Label(self, height=2, width=64, text="Anime_Name", borderwidth=0.5, relief="solid").grid(row=i + 1,
                                                                                                            column=0)
                tk.Label(self, height=2, width=15, text="Score", borderwidth=0.5, relief="solid").grid(row=i + 1,
                                                                                                       column=1)
                tk.Label(self, height=2, width=63, text="Genre", borderwidth=0.5, relief="solid").grid(row=i + 1,
                                                                                                       column=2)
            else:
                anime = ut.getAnime_data(self.data, i - 1)
                tk.Label(self, height=2, width=64, text=ut.getName(anime), borderwidth=0.5, relief="solid").grid(
                    row=i + 1, column=0)
                tk.Label(self, height=2, width=15, text=ut.getScore(anime), borderwidth=0.5, relief="solid").grid(
                    row=i + 1, column=1)
                tk.Label(self, height=2, width=63, text=ut.getGenere(anime), borderwidth=0.5, relief="solid").grid(
                    row=i + 1, column=2)


#########################################################################################################################
# def select():
#     anime_name=clicked.get()


root = Tk()
root.title('Anime heaven')
root.geometry('700x394')
root.resizable(False, False)
bg1 = PhotoImage(file="dibba.png")
bglabel = Label(root, image=bg1)
bglabel.place(x=0, y=0)
scle=3
options = ["Action"+" "*7*scle, "Adventure"+" "*4*scle, "Ecchi"+" "*8*scle, "Fantasy"+" "*6*scle, "Harem"+" "*8*scle, "Horror"+" "*7*scle, "Psychological"+" "*scle, "Shounen"+" "*6*scle]
clicked = StringVar()
clicked.set("Action"+" "*7*scle)

drop = OptionMenu(root, clicked, *options)
drop.place(x=250, y=150)

search_image = PhotoImage(file="—Pngtree—vector search icon_4278283 (1).png")
search_button = Button(root, image=search_image, bd=0, cursor='hand2', background='grey', activebackground='white')
search_button.place(x=430, y=150)
search_button.bind("<Button>",lambda e: NewWindow(root,title=str(clicked.get()).replace(" ",""),num=0))

exit_image = PhotoImage(file="icons8-exit-50.png")
exit_button = Button(root, image=exit_image, bd=0, cursor='hand2', background='grey', activebackground='grey',command=root.destroy)
exit_button.place(x=430, y=320)

root.mainloop()
