import tkinter as tk
import customtkinter as ctk
import sys
import main
root = ctk.CTkToplevel()
# --- functions ---
def exit():
    sys.exit

def tksleep(self, time:float) -> None:
    self.after(int(time*1000), self.quit)
    self.mainloop()
def sleep():
    root.tksleep()
    
# --- classes ---

class Redirect():
    
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert('end', text)
        #self.widget.see('end') # autoscroll
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

button = ctk.CTkButton(master=frame, text='Run', command=main.main)
button.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text='Stop', command=exit)
button.pack(pady=12, padx=10)

text = ctk.CTkTextbox(frame)
text.pack()

old_stdout = sys.stdout    
sys.stdout = Redirect(text)

root.mainloop()

sys.stdout = old_stdout