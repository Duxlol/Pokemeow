import pyautogui
from PIL import Image
from configparser import ConfigParser
from configparser import RawConfigParser
from pytesseract import pytesseract as tess
import cv2
from tksleep import tksleep
config = RawConfigParser()

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()


def items():
    #move and click on discord
    mouse.position = (400, 990)
    mouse.press(Button.left)
    mouse.release(Button.left)
    tksleep.tksleep(1)
    #move and click on discord
    mouse.position = (400, 990)
    mouse.press(Button.left)
    mouse.release(Button.left)
    tksleep.tksleep(0.5)
    
    #type ;inv
    keyboard.type(";inv")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    tksleep.tksleep(2)

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
        tksleep.tksleep(1)

    #GREATBALLS
    if int(greatballs) <= 10:
        print("Buying greatballs because there's less than 10")
        keyboard.type(";shop buy gb 10")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        tksleep.tksleep(1)
    #ULTRABALLS
    if int(ultraballs) <= 2:
        print("Buying ultraballs because there's less than 2")
        keyboard.type(";shop buy ub 3")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        tksleep.tksleep(1)
    #PREMIERBALLS
    if int(ultraballs) <= 0:
        print("Buying premierballs because there's less than 1")
        keyboard.type(";event buy 2")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        tksleep.tksleep(1)