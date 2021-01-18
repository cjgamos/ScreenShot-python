import pyautogui
import time

def screenshot():

    name = int(round(time.time() * 10000))
    name = '{}.png'.format(name)


    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

    
screenshot()