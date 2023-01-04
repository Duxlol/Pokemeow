import pyautogui
from discordwebhook import Discord
from configparser import ConfigParser
config = ConfigParser()

#load webhook url from config
config.read('config.ini')
url = config['CONFIG']['webhook']

discord = Discord(url=url)

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