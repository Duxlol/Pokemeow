import functions.catch as catch
import functions.copy as copy
import functions.items as items
import functions.egg as egg
import functions.directory as dir
import customtkinter as ctk
import customtkinter as ctk
root = ctk.CTk()

def tksleep(self, time:float) -> None:
    self.after(int(time*1000), self.quit)
    self.mainloop()

def main():
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
            root.tksleep(2.5)
            items.item_amount()
            root.tksleep(2)

            for i in range (10):  
                print("catching pokemon")
                #run catch command (with webhook for sr,leg,shiny)
                catch.catch()

                #check for egg hatch
                egg.findegg()