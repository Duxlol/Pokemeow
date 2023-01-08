import customtkinter as ctk
import time

root = ctk.CTk()

#def tksleep(root, time:float) -> None:
#        root.after(int(time*1000), root.quit)
#        root.mainloop()
#tk.Misc.tksleep = tksleep
class tksleep():
        def tksleep(secs: float):
                start_time = time.time()
                root.withdraw()
                while time.time() - start_time < secs:
                        root.update()
                        root.after(1)