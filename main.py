import time
import functions.catch as catch
import functions.copy as copy
import functions.items as items
import functions.egg as egg
import functions.directory as dir


#copy ;p
copy.copy()

#make items folder
dir.mkdir()


while True:
    #open inv and check for items + put them in config
    items.items()
    time.sleep(2.5)
    items.item_amount()
    time.sleep(2)

    for i in range (10):  

        #run catch command (with webhook for sr,leg,shiny)
        catch.catch()

        #check for egg hatch
        egg.findegg()
    