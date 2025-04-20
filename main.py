import cv2 as cv
from PIL import Image,ImageGrab
import time
import numpy as np
import pyautogui
import random
import keyboard

sickle = cv.imread("./imgs/sickle.png")
colorModeSickle = "rgb"
thresholdSickle = 0.5

emptyField = cv.imread("./imgs/emptyField.png")
colorModeEmptyField = "hsv"
thresholdEmptyField = 0.5

grownWheat = cv.imread("./imgs/wheatGrown.png")
colorModeGrownWheat = "rgb"
thresholdGrownWheat = 0.4

wheatIcon = cv.imread("./imgs/wheatIcon.png")
colorModeWheatIcon = "rgb"
thresholdWheatIcon = 0.6

marketplaceOnStreet = cv.imread("./imgs/marketplace.png")
colorModeMarketplace = "rgb"
thresholdMarketplace = 0.6

def main():
    #for mouse error control (to stop move mouse to up left corner)
    pyautogui.FAILSAFE = True

    time.sleep(10)

    def waitSecondsInRange(minSec:int,maxSec:int,floatDigitAfterComma:int):
        time.sleep(round(random.uniform(minSec,maxSec),floatDigitAfterComma))

    #takes screenshot of screen and returns array of screen hsv or rgb syle
    def takeScreenshot(colorMode:str):
        screenshot = ImageGrab.grab()
        screenshot = np.array(screenshot)
        if colorMode == "rgb":
            screenshotRGB = cv.cvtColor(screenshot,cv.COLOR_BGR2RGB)
            return screenshotRGB
        elif colorMode == "hsv":
            screenshotHSV = cv.cvtColor(screenshot,cv.COLOR_BGR2HSV)
            return screenshotHSV
        
    #finds location of target object on screeen (takeScreenhot func inluded in)
    def findTheLocation(target:cv.typing.MatLike,colorMode:str,threshold:float):
        response = cv.matchTemplate(takeScreenshot(colorMode),target,cv.TM_CCOEFF_NORMED)
        response = np.array(response)
        minVal,maxVal,minLoc,maxLoc = cv.minMaxLoc(response)
        if maxVal < threshold:
            return None
        else:
            return maxLoc
    
    def humanLikeClick():
        pressTime = random.uniform(0.05,0.2)
        releaseTime = random.uniform(0.05,0.2)
        pyautogui.mouseDown()
        time.sleep(pressTime)
        pyautogui.mouseUp()
        time.sleep(releaseTime)
        

    def harvest(xLoc,yLoc):
        sickleLoc= findTheLocation(sickle,colorModeSickle,thresholdSickle)
        if sickleLoc == None:
            print("Couldn't find the sickle!")
        else:
            pyautogui.moveTo(sickleLoc[0],sickleLoc[1])
            pyautogui.mouseDown()
            pyautogui.moveTo(xLoc,yLoc,round(random.uniform(1,2),1))
            pyautogui.move(280,150,round(random.uniform(2,3),1))
            pyautogui.mouseUp()
            



    def plantCrop(xLoc,yLoc,cropIcon:cv.typing.MatLike,cropColorMode,cropThreshold):
        locationCropIcon = findTheLocation(cropIcon,cropColorMode,cropThreshold)
        if locationCropIcon == None:
            print("There is no wheat icon found on screen!")
        else:
            pyautogui.moveTo(locationCropIcon[0],locationCropIcon[1])
            pyautogui.mouseDown()
            pyautogui.moveTo(xLoc,yLoc,round(random.uniform(1,2),1))
            pyautogui.move(280,150,round(random.uniform(2,3),1))
            pyautogui.mouseUp()
            
        

## TODOS
# While loop excape func will be fixed

# Plant loop will be added in future

    #harvesting loop that harvests multiple time
    def harvestAllCrops(crop:cv.typing.MatLike,colorModeCrop:str,thresholdGrownCrop:float):
        print("Entering harvesting loop. Press q to exit.")
        while True:
            locCrop = findTheLocation(crop,colorModeCrop,thresholdGrownCrop)
            if locCrop == None:
                print("There is no grown wheat on screen! Skipping harvesting process...")
                break
            else:
                pyautogui.moveTo(locCrop[0]+50,locCrop[1]+30)
                humanLikeClick()
                waitSecondsInRange(1,2,1)
                harvest(locCrop[0]+50,locCrop[1]+30)
                waitSecondsInRange(1,2,1)
            #wait for the disappear xp and wheat icons after harvest
            waitSecondsInRange(3,4,1)
            if keyboard.is_pressed("q"):
                print("Pressed q quiting harvest loop.")
                break
        
        print("Harvest proccess ended.")
        
    def plantCropToAllField(cropIcon:cv.typing.MatLike,colorModeCropIcon:str,thresholdCropIcon:float):
        print("Entering planting loop. Press q to exit.")
        while True:
            emptyFieldLoc = findTheLocation(emptyField,colorModeEmptyField,thresholdEmptyField)
            if emptyFieldLoc == None:
                print("There is no empty field on screen! Skipping planting process...")
                break
            else:
                pyautogui.moveTo(emptyFieldLoc[0]+50,emptyFieldLoc[1]+30)
                humanLikeClick()
                waitSecondsInRange(1,2,1)
                plantCrop(emptyFieldLoc[0],emptyFieldLoc[1],cropIcon,colorModeCropIcon,thresholdCropIcon)
                waitSecondsInRange(1,2,1)
            waitSecondsInRange(1,2,1)
            if keyboard.is_pressed("q"):
                    print("Pressed q quiting harvest loop.")
                    break
   



    harvestAllCrops(grownWheat,colorModeGrownWheat,thresholdGrownWheat)
    waitSecondsInRange(3,5,1)
    plantCropToAllField(wheatIcon,colorModeWheatIcon,thresholdWheatIcon)
        

if __name__=="__main__":
    main()


# def print_menu():
#     print("Welcome to the wheater bot for Hay Day.")
#     print("Enter a key to choose option shown below.")
#     print("\tw --> Start the cropping bot.")
#     print("\tq --> Exit the app.")
    

# if __name__=="__main__":
#     print_menu()
    
#     while True:
#         userInput = input()
#         userInput = str.lower(userInput).strip()
#         if userInput=="w":
#             pass
#         elif userInput=="q":
#             print(f"You have pressed the {userInput} button.Exiting app...")
#             cv.destroyAllWindows()
#             break
#         else:
#             print(f"Key {userInput} is not a valid character.")
    
    
    