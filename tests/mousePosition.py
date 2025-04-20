import pyautogui
import time
import keyboard

def mousePostion():
    pyautogui.FAILSAFE = True
    x = True
    while x:
        print(pyautogui.position())
        time.sleep(5)
        if keyboard.is_pressed("q"):
            x = False

#280x  y150

if __name__ == "__main__":
    mousePostion()