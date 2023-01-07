import tkinter as tk
import customtkinter as ctk

root = ctk.CTk()

def tksleep(root, time:float) -> None:
        root.after(int(time*1000), root.quit)
        root.mainloop()
tk.Misc.tksleep = tksleep