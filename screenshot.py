import pyautogui
import time
import tkinter as tk

def screenshot():

    name = int(round(time.time() * 10000))
    name = 'D:\Repo\Python\ScreenShot-python\data/{}.png'.format(name)


    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

    
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text='Take Screenshot',
    command=screenshot
)

button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text='Quit',
    command=quit
)
close.pack(side=tk.LEFT)

root.mainloop()