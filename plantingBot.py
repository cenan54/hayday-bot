import cv2 as cv
import pyautogui
import random
import interactionFunctions


emptyField = cv.imread("./imgs/emptyField.png")
colorModeEmptyField = "hsv"
thresholdEmptyField = 0.5

wheatIcon = cv.imread("./imgs/wheatIcon.png")
colorModeWheatIcon = "rgb"
thresholdWheatIcon = 0.6


def plantCrop(xLoc,yLoc,cropIcon:cv.typing.MatLike,cropColorMode,cropThreshold):
    locationCropIcon = interactionFunctions.findTheLocation(cropIcon,cropColorMode,cropThreshold)
    if locationCropIcon == None:
        print("There is no wheat icon found on screen!")
    else:
        pyautogui.moveTo(locationCropIcon[0],locationCropIcon[1])
        pyautogui.mouseDown()
        pyautogui.moveTo(xLoc,yLoc,round(random.uniform(1,2),1))
        pyautogui.move(280,150,round(random.uniform(2,3),1))
        pyautogui.mouseUp()

def plantCropToAllField(cropIcon:cv.typing.MatLike,colorModeCropIcon:str,thresholdCropIcon:float):
        print("Entering planting loop. Press q to exit.")
        while True:
            emptyFieldLoc = interactionFunctions.findTheLocation(emptyField,colorModeEmptyField,thresholdEmptyField)
            if emptyFieldLoc == None:
                print("There is no empty field on screen! Skipping planting process...")
                break
            else:
                pyautogui.moveTo(emptyFieldLoc[0]+50,emptyFieldLoc[1]+30)
                interactionFunctions.humanLikeClick()
                interactionFunctions.waitSecondsInRange(1,2,1)
                plantCrop(emptyFieldLoc[0],emptyFieldLoc[1],cropIcon,colorModeCropIcon,thresholdCropIcon)
                interactionFunctions.waitSecondsInRange(1,2,1)
            interactionFunctions.waitSecondsInRange(1,2,1)
        
        print("Planting process ended.")
   
def run():
    plantCropToAllField(wheatIcon,colorModeWheatIcon,thresholdWheatIcon)