import pyautogui
import time
import sys
import random

CONFIDENCE_OF_FINDING_CROP = 0.7
COUNT_DOWN_SECONDS_BEFORE_START = 10
SECONDS_BEETWEEN_ACTIONS = 1
grownCropFilePath = './imgs/wheatGrown.png'

def main():
    #Initialized pyautogui 
    pyautogui.FAILSAFE = True
    #Countdown timer before starting the app
    countDownBeforeStart(COUNT_DOWN_SECONDS_BEFORE_START)

    #Finds location grownCrop on the screen
    PosX,PosY = findLocationGrownCropOnTheScreen()
    pyautogui.click(PosX,PosY)
    time.sleep(random.randint(1,3))
    pyautogui.moveTo(PosX-120,PosY-100)


    waitForNextAction(SECONDS_BEETWEEN_ACTIONS)





def countDownBeforeStart(seconds = 10):
    print(f"Uygulama {seconds} saniye sonra basliyor",end="")
    for i in range(0,seconds):
        print(".",end="")
        sys.stdout.flush()#forces to appear dots in real time
        time.sleep(1)
    print("Basla")

def findLocationGrownCropOnTheScreen():
    wheatPositionOnScreen = pyautogui.locateOnScreen(grownCropFilePath,confidence=CONFIDENCE_OF_FINDING_CROP,grayscale=True)
    wheatPositionOnScreen = pyautogui.center(wheatPositionOnScreen)
    wheatPosX,wheatPosY = wheatPositionOnScreen
    return wheatPosX,wheatPosY
 

def waitForNextAction(seconds=1):
    time.sleep(seconds)    


if __name__=="__main__":
    main()