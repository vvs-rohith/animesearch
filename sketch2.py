# import tkinter as tk
# import Utilities as ut
# dictr=ut.load(1)
# action=ut.getAnime_list(dictr,"Action")
# root = tk.Tk()
# root.geometry("1000x800")
# root.resizable(False,True)
# height = 21
# for i in range(0,height):
#         if i==0:
#             tk.Label(root,height=2,width=64,text="Anime_Name", borderwidth=0.5, relief="solid").grid(row=i+1, column=0)
#             tk.Label(root,height=2,width=15,text="Score", borderwidth=0.5, relief="solid").grid(row=i+1, column=1)
#             tk.Label(root,height=2,width=63,text="Genre", borderwidth=0.5, relief="solid").grid(row=i+1, column=2)
#         else:
#             anime=ut.getAnime_data(action,i-1)
#             tk.Label(root,height=2,width=64,text=ut.getName(anime), borderwidth=0.5, relief="solid").grid(row=i+1, column=0)
#             tk.Label(root,height=2,width=15,text=ut.getScore(anime), borderwidth=0.5, relief="solid").grid(row=i+1, column=1)
#             tk.Label(root,height=2,width=63,text=ut.getGenere(anime), borderwidth=0.5, relief="solid").grid(row=i+1, column=2)
# tk.mainloop()

options = ["Action", "Adventure", "Ecchi", "Fantasy", "Harem", "Horror", "Psychological", "Shounen"]
for i in options:
    print(len(i))