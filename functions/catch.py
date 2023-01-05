import pyautogui
from PIL import Image
import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import functions.webhook as webhook
import functions.captcha as captcha

keyboard = KeyboardController()
mouse = MouseController()


def catch():


    # click and paste
    mouse.position = (400, 990)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.5)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(2)
    
    #find captcha
    captcha.find()

    # take screenshot of color
    im1 = pyautogui.screenshot('color.png', region=(384, 668, 2, 2))

    # open all colors
    im2 = Image.open('color.png')

    im3 = Image.open(r".\images\common.png")
    im4 = Image.open(r".\images\uncommon.png")
    im5 = Image.open(r".\images\rare.png")
    im6 = Image.open(r".\images\superrare.png")
    im7 = Image.open(r".\images\legendary.png")
    im8 = Image.open(r".\images\shiny.png")

    # check which one matches

    # common
    if list(im2.getdata()) == list(im3.getdata()):
        print("\033[34mCOMMON\033[0m")
        mouse.position = (416, 926)
        mouse.press(Button.left)
        mouse.release(Button.left)
        print("Used Pokeball")

    # uncommon
    if list(im2.getdata()) == list(im4.getdata()):
        print("\033[34mUNCOMMON\033[0m")
        mouse.position = (416, 926)
        mouse.press(Button.left)
        mouse.release(Button.left)
        print("Used Pokeball")

    # rare
    if list(im2.getdata()) == list(im5.getdata()):
        print("\033[31mRARE\033[0m")
        mouse.position = (484, 926)
        mouse.press(Button.left)
        mouse.release(Button.left)
        print("Used Greatball")

    # super rare
    if list(im2.getdata()) == list(im6.getdata()):
        print("\033[33mSUPER RARE\033[0m")
        mouse.position = (561, 926)
        mouse.press(Button.left)
        mouse.release(Button.left)
        print("Used Ultraball")
        print("Starting webhook")
        webhook.webhook()

    # legendary
    if list(im2.getdata()) == list(im7.getdata()):
        print("\033[33mLEGENDARY\033[0m")
        mouse.position = (630, 926)
        mouse.press(Button.left)
        mouse.release(Button.left)
        print("Used Used Premierball")
        webhook.webhook()

    # Shiny
    if list(im2.getdata()) == list(im8.getdata()):
        print("\033[33mSHINY\033[0m")
        mouse.position = (630, 926)
        mouse.press(Button.left)
        mouse.release(Button.left)
        print("Used Premierball")
        webhook.webhook()

    time.sleep(8)
