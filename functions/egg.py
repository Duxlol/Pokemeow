from python_imagesearch.imagesearch import imagesearch
import configparser
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import gui

keyboard = KeyboardController()
mouse = MouseController()
config = configparser.ConfigParser()

def findegg():
    pos = imagesearch(".\images\egg.png")
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        print("Egg is ready to hatch!")
        gui.sleep(1)
        keyboard.type(";egg hatch")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        gui.sleep(7)

        #check if there's eggs in inventory
        config.read('config.ini')
        amt = config['CONFIG']['egg']
        if int(amt) >= 1:
            keyboard.type(";egg hold")
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            gui.sleep(2)