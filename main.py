import functions.catch as catch
import functions.copy as copy
import functions.items as items
import functions.egg as egg
import functions.directory as dir
import customtkinter as ctk
import gui
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
            gui.sleep()
            items.item_amount()
            gui.sleep(2)

            for i in range (10):  
                print("catching pokemon")
                #run catch command (with webhook for sr,leg,shiny)
                catch.catch()

                #check for egg hatch
                egg.findegg()