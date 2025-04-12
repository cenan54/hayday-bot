import pyautogui
import cv2 as cv
import time
import sys

def main():
    #Initialized pyautogui 
    pyautogui.FAILSAFE = True

    #Countdown timer before starting the app
    print("Uygulama 10 saniye sonra basliyor",end="")
    for i in range(0,10):
        print(".",end="")
        sys.stdout.flush()#forces to appear dots in real time
        time.sleep(1)
    print("Basla")

    #Clicks center of screen print("App starting",end="")
    for i in range(0,10):
        print(".",end="")
    screenWidht,screenHeight = pyautogui.size()
    centerWidth = screenWidht // 2
    centerHeigth = screenHeight // 2

    pyautogui.click(centerWidth,centerHeigth)


if __name__=="__main__":
    main()