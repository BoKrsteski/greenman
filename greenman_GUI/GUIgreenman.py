from greenmancore import *
import tkinter as tk
from tkinter import ttk
import sys
import os

# TODO icon: https://www.pythontutorial.net/tkinter/tkinter-window/

def isInMEIPASS(item):
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        item_path = os.path.join(sys._MEIPASS, item)
        return item_path if os.path.exists(item) else False



root=tk.Tk()
root.title("Greenman")
root.geometry('600x400+50+50')
root.configure(bg="#1e1e1e")
root.resizable(False,False)
def blockFullscreen(event):
    return "break"
root.bind("<F11>",blockFullscreen)
root.bind("<Alt-Return>",blockFullscreen)
root.attributes('-topmost', 1)
z = isInMEIPASS("greenman.ico")

iconLoc = z if z else os.path.join(os.path.dirname(os.path.abspath(__file__)),"data","icons","greenman.ico")
if os.name == 'nt':
    root.iconbitmap(iconLoc)
else:
    root.iconphoto(True, tk.PhotoImage(file=iconLoc.replace('.ico', '.png')))
style = ttk.Style()
style.theme_use("default")
title=tk.Label(root,text="Greenman",font=("Segoe UI",20,"bold"),bg="#1e1e1e",fg="green")
title.pack(pady=5)
author=tk.Label(root,text="made by Bo",font=("Segoe UI",7),bg="#1e1e1e",fg="gray")
author.pack(pady=2.5)
root.mainloop()
