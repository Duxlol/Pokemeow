import tkinter as tk
import customtkinter as ctk
import sys

import functions.catch as catch
import functions.copy as copy
import functions.items as items
import functions.egg as egg
import functions.directory as dir
from tksleep import tksleep

root = ctk.CTk()

def start():  
    #copy ;p
    copy.copy()

    #make items folder
    try:
        print("Creating items folder")
        dir.mkdir()
    except:
        print("Folder already exists")
    finally:

        while True:
            #open inv and check for items + put them in config
            print("opened inventory")
            items.items()
            tksleep.tksleep(2)
            items.item_amount()
            tksleep.tksleep(2)

            for i in range (10):  
                print("catching pokemon")
                #run catch command (with webhook for sr,leg,shiny)
                catch.catch()

                #check for egg hatch
                egg.findegg()

# GUI

# --- functions ---
def exit():
    sys.exit
    
# --- classes ---

class Redirect():
    
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert('end', text)
        self.widget.see('end') # autoscroll
    def flush(self):
        pass
    
# --- main ---    
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root.geometry("500x350")
root.iconbitmap(r"app.ico")
root.title('dux<3#0767')

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Dux' Pokemeow Bot", font=("Roboto", 24))
label.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text='Run', command=start)
button.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text='Stop', command=exit)
button.pack(pady=12, padx=10)

text = ctk.CTkTextbox(frame)
text.pack()

old_stdout = sys.stdout    
sys.stdout = Redirect(text)

root.mainloop()

sys.stdout = old_stdout