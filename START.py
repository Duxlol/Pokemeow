#copy
import pyperclip as pc

#items
import pyautogui
from PIL import Image
from configparser import ConfigParser
from configparser import RawConfigParser
from pytesseract import pytesseract as tess
import cv2
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()
config = RawConfigParser()

#tkinter
import tkinter as tk
import customtkinter as ctk
import sys
from tkinter.scrolledtext import *

#webhooks
from discordwebhook import Discord
#   load webhook url from config
config.read('config.ini')
url = config['CONFIG']['webhook']
discord = Discord(url=url)
from python_imagesearch.imagesearch import imagesearch

#directory
import os
directory = "items"
parent_dir = "./"
path = os.path.join(parent_dir, directory)





def tksleep(self, time:float) -> None:
        self.after(int(time*1000), self.quit)
        self.mainloop()
tk.Misc.tksleep = tksleep
root = ctk.CTk()

def copy():
    spawn = ";p"
  
    # copying text to clipboard
    pc.copy(spawn)
    print("Successfully copied ;p")

def items():
    #move and click on discord
    mouse.position = (400, 990)
    mouse.press(Button.left)
    mouse.release(Button.left)
    root.tksleep(1)
    #move and click on discord
    mouse.position = (400, 990)
    mouse.press(Button.left)
    mouse.release(Button.left)
    root.tksleep(0.5)
    
    #type ;inv
    keyboard.type(";inv")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    root.tksleep(2)

    #take screenshot of each ball individually
    #pokeball
    pyautogui.screenshot(r'.\items\pokeball.png', region=(419,627, 25, 18))
    
    im2 = cv2.imread(r".\items\pokeball.png")

    (h, w) = im2.shape[:2]
    im2 = cv2.resize(im2, (w*3, h*3))
    gry = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
    thr = cv2.threshold(gry, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    amount = tess.image_to_string(thr, config='--psm 10 -c tessedit_char_whitelist=0123456789')

    print(amount, "pokeball(s)")
    config.read('config.ini')
    config.set('CONFIG', 'pokeball', amount)
    with open('config.ini', 'w') as f:
        config.write(f)


    #greatball
    im3 = pyautogui.screenshot(r'.\items\greatball.png', region=(419,647, 18, 13))
    im4 = cv2.imread(r".\items\greatball.png")
    
    (h2, w2) = im4.shape[:2]
    im4 = cv2.resize(im4, (w2*3, h2*3))
    gry2 = cv2.cvtColor(im4, cv2.COLOR_BGR2GRAY)
    thr2 = cv2.threshold(gry2, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    amount2 = tess.image_to_string(thr2, config='--psm 10 -c tessedit_char_whitelist=0123456789')
    print(amount2, "greatball(s)")

    config.set('CONFIG', 'greatball', amount2)
    with open('config.ini', 'w') as f:
        config.write(f)

    
    #ultraball
    im5 = pyautogui.screenshot(r'.\items\ultraball.png', region=(419,665, 11, 13))
    im6 = cv2.imread(r".\items\ultraball.png")

    (h3, w3) = im6.shape[:2]
    im6 = cv2.resize(im6, (w3*3, h3*3))
    gry3 = cv2.cvtColor(im6, cv2.COLOR_BGR2GRAY)
    thr3 = cv2.threshold(gry3, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    amount3 = tess.image_to_string(thr3, config='--psm 10 -c tessedit_char_whitelist=0123456789')    
    
    print(amount3, "ultraball(s)")

    config.set('CONFIG', 'ultraball', amount3)
    with open('config.ini', 'w') as f:
        config.write(f)


    #premierball
    im7 = pyautogui.screenshot(r'.\items\premierball.png', region=(569,485, 9, 14))
    im8 = cv2.imread(r".\items\premierball.png")
    
    (h4, w4) = im8.shape[:2]
    im8 = cv2.resize(im8, (w4*3, h4*3))
    gry4 = cv2.cvtColor(im8, cv2.COLOR_BGR2GRAY)
    thr4 = cv2.threshold(gry4, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    amount4 = tess.image_to_string(thr4, config='--psm 10 -c tessedit_char_whitelist=01234')    
    print(amount4, "premierball(s)")
    four = '4'
    one = 1
    if amount4 == four:
        config.set('CONFIG', 'premierball', one)
    else:
        config.set('CONFIG', 'premierball', amount4)
        with open('config.ini', 'w') as f:
            config.write(f)

    #egg
    im9 = pyautogui.screenshot(r'.\items\egg.png', region=(570,683, 10, 11))
    im10 = cv2.imread(r".\items\egg.png")

    (h5, w5) = im8.shape[:2]
    im10 = cv2.resize(im10, (w5*3, h5*3))
    gry5 = cv2.cvtColor(im10, cv2.COLOR_BGR2GRAY)
    thr5 = cv2.threshold(gry5, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    amount5 = tess.image_to_string(thr5, config='--psm 10 -c tessedit_char_whitelist=0123456789')    
    print(amount5, "egg(s)")

    config.set('CONFIG', 'egg', amount5)
    with open('config.ini', 'w') as f:
        config.write(f)

def item_amount():
    pokeballs = config['CONFIG']['pokeball']
    greatballs = config['CONFIG']['greatball']
    ultraballs = config['CONFIG']['ultraball']
    premierballs = config['CONFIG']['premierball']

    #POKEBALLS
    if int(pokeballs) <= 100:
        print("Buying pokeballs because there's less than 100")
        keyboard.type(";shop buy pb 12")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        root.tksleep(1)

    #GREATBALLS
    if int(greatballs) <= 10:
        print("Buying greatballs because there's less than 10")
        keyboard.type(";shop buy gb 10")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        root.tksleep(1)
    #ULTRABALLS
    if int(ultraballs) <= 2:
        print("Buying ultraballs because there's less than 2")
        keyboard.type(";shop buy ub 3")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        root.tksleep(1)
    #PREMIERBALLS
    if int(ultraballs) <= 0:
        print("Buying premierballs because there's less than 1")
        keyboard.type(";event buy 2")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        root.tksleep(1)

def webhook():
    #take screenshot
    im1 = pyautogui.screenshot('screen.png', region=(0,0, 1920, 1080))
    print("Screenshot taken")

    discord.post(file={
            "file1": open("screen.png", "rb"),
        },
    )
    print("Screenshot sent thru webhook")

def captcha():
    im2 = pyautogui.screenshot('captcha.png', region=(0,0, 1920, 1080))
    print("Captcha screenshot taken")

    allowed_mentions = {
    "users": ["@dux<3#0767"]
}
    discord.post(file={
            "file1": open("captcha.png", "rb"),
        }, content="<@266173480729444353>",
    )

    print("Pinged user")    

def find():
    pos = imagesearch(".\images\captcha.png")
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        
        #click on captcha image
        mouse.position = (462, 806)
        mouse.press(Button.left)
        mouse.release(Button.left)
        root.tksleep(2)

        #take screenshot of image
        im1 = pyautogui.screenshot(r'.\captcha\solver.png', region=(890, 492, 140, 57))
        print("Image screenshot taken") 
       
        #open, transform and type the solving
        im2 = cv2.imread(r".\captcha\solver.png")

        (h, w) = im2.shape[:2]
        im2 = cv2.resize(im2, (w*3, h*3))
        gry = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
        thr = cv2.threshold(gry, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        number = tess.image_to_string(thr, config='--psm 10 -c tessedit_char_whitelist=0123456789')
        print(number)
        captcha()

def catch():


    # click and paste
    mouse.position = (400, 990)
    mouse.press(Button.left)
    mouse.release(Button.left)
    root.tksleep(0.5)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    root.tksleep(2)
    
    #find captcha
    find()

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
        webhook()

    # legendary
    if list(im2.getdata()) == list(im7.getdata()):
        print("\033[33mLEGENDARY\033[0m")
        mouse.position = (630, 926)
        mouse.press(Button.left)
        mouse.release(Button.left)
        print("Used Used Premierball")
        webhook()

    # Shiny
    if list(im2.getdata()) == list(im8.getdata()):
        print("\033[33mSHINY\033[0m")
        mouse.position = (630, 926)
        mouse.press(Button.left)
        mouse.release(Button.left)
        print("Used Premierball")
        webhook()

    root.tksleep(8)

def mkdir():
    os.mkdir(path)

def findegg():
    pos = imagesearch(".\images\egg.png")
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        print("Egg is ready to hatch!")
        root.tksleep(1)
        keyboard.type(";egg hatch")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        root.tksleep(7)

        #check if there's eggs in inventory
        config.read('config.ini')
        amt = config['CONFIG']['egg']
        if int(amt) >= 1:
            keyboard.type(";egg hold")
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            root.tksleep(2)
    
def start():  
    #copy ;p
    copy()

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
            items()
            root.tksleep(2)
            item_amount()
            root.tksleep(2)

            for i in range (10):  
                print("catching pokemon")
                #run catch command (with webhook for sr,leg,shiny)
                catch()

                #check for egg hatch
                findegg()

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
text.yview(tk.END)
text.pack()


old_stdout = sys.stdout    
sys.stdout = Redirect(text)

root.mainloop()

sys.stdout = old_stdout