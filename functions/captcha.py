from PIL import Image
import pyautogui
import cv2
import functions.webhook as webhook
from pytesseract import pytesseract as tess
from python_imagesearch.imagesearch import imagesearch
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from tksleep import tksleep
keyboard = KeyboardController()
mouse = MouseController()

def find():
    pos = imagesearch(".\images\captcha.png")
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        
        #click on captcha image
        mouse.position = (462, 806)
        mouse.press(Button.left)
        mouse.release(Button.left)
        tksleep.tksleep(2)

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
        webhook.captcha()