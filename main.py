import cv2 as cv
from PIL import Image,ImageGrab
import time
import numpy as np
import pyautogui
import random


sickle = cv.imread("./imgs/sickle.png")
colorModeSickle = "rgb"
thresholdSickle = 0.5

emptyField = cv.imread("./imgs/emptyField.png")
colorModeEmptyField = "hsv"
thresholdEmptyField = 0.5

grownWheat = cv.imread("./imgs/wheatGrown.png")
colorModeGrownWheat = "rgb"
thresholdGrownWheat = 0.4

marketplaceOnStreet = cv.imread("./imgs/marketplace.png")
colorModeMarketplace = "rgb"
thresholdMarketplace = 0.6

def main():
    #for mouse error control (to stop move mouse to up left corner)
    pyautogui.FAILSAFE = True

    time.sleep(10)

    #takes screenshot of screen and returns array of screen hsv or rgb syle
    def takeScreenshot(colorMode):
        screenshot = ImageGrab.grab()
        screenshot = np.array(screenshot)
        if colorMode == "rgb":
            screenshotRGB = cv.cvtColor(screenshot,cv.COLOR_BGR2RGB)
            return screenshotRGB
        elif colorMode == "hsv":
            screenshotHSV = cv.cvtColor(screenshot,cv.COLOR_BGR2HSV)
            return screenshotHSV
        
    #finds location of target object on screeen (takeScreenhot func inluden in)
    def findTheLocation(target,colorMode,threshold):
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
        sickleLocX, sickleLocY = findTheLocation(sickle,colorModeSickle,thresholdSickle)
        pyautogui.moveTo(sickleLocX,sickleLocY)
        pyautogui.mouseDown()
        pyautogui.moveTo(xLoc,yLoc,round(random.uniform(1,2),1))
        pyautogui.move(400,-270,round(random.uniform(2,5),1))
        pyautogui.mouseUp()
        time.sleep(round(random.uniform(1,2),1))

    
  

    locWheat = findTheLocation(grownWheat,colorModeGrownWheat,thresholdGrownWheat)
    if locWheat == None:
        print("There is no grown wheat on screen!")
    else:
        pyautogui.moveTo(locWheat)
        humanLikeClick()
        time.sleep(round(random.uniform(1,2),1))
        harvest(locWheat[0],locWheat[1])
    time.sleep(3)

    locEmptyField = findTheLocation(emptyField,colorModeEmptyField,thresholdEmptyField)
    if locEmptyField == None:
        print("There is no empty field on screen!")
    else:
        pyautogui.moveTo(locEmptyField)

    time.sleep(3)

    # pyautogui.click()
    # time.sleep(round(random.uniform(1,3),1))
    # moveMouseToLocation(sickle,colorModeSickle)
    # pyautogui.mouseDown(button="left")
    # time.sleep(round(random.uniform(1,2),1))
    # pyautogui.move(200,150,1)
    # pyautogui.move(400,-300,3)
    # pyautogui.mouseUp()
    


    # #minVal,maxVal,minLoc,maxLoc = findTheLocation(marketplaceOnStreet,colorModeMarketplace)
    # def harvest():
    #     minValWheat,maxValWheat,minLocWheat,maxLocWheat = findTheLocation(grownWheat,colorModeGrownWheat)
    #     if(maxVal<0.4):
    #         return
    #     else:
    #         pyautogui.moveTo(maxLocWheat[0],maxLocWheat[1])
    #         pyautogui.click()
    #         time.sleep(round(random.uniform(1,3)))
                
    #         print("Entering harvesting loop. Press q to exit.")
    #         while True:
    #             userInput = input()
    #             userInput = str.lower(userInput).strip()
    #             if userInput == "q":
    #                 print(f"You have pressed the {userInput} button.Exiting app...")
    #                 break
    #             else:
    #                 print(f"The {userInput} key is not valid.")

                
            


        


    
    # if(maxLoc!=None):
    #     pyautogui.moveTo(maxLoc[0],maxLoc[1])
    #     pyautogui.click()
    # time.sleep(1)




    

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
    
    
    