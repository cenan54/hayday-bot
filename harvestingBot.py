import cv2 as cv
import pyautogui
import interactionFunctions
import random


sickle = cv.imread("./imgs/sickle.png")
colorModeSickle = "rgb"
thresholdSickle = 0.5

grownWheat = cv.imread("./imgs/wheatGrown.png")
colorModeGrownWheat = "rgb"
thresholdGrownWheat = 0.4


def harvest(xLoc,yLoc):
    sickleLoc= interactionFunctions.findTheLocation(sickle,colorModeSickle,thresholdSickle)
    if sickleLoc == None:
        print("Couldn't find the sickle!")
    else:
        pyautogui.moveTo(sickleLoc[0],sickleLoc[1])
        pyautogui.mouseDown()
        pyautogui.moveTo(xLoc,yLoc,round(random.uniform(1,2),1))
        pyautogui.move(280,150,round(random.uniform(1,2),1))
        pyautogui.mouseUp()

#harvesting loop that harvests multiple time
def harvestAllCrops(crop:cv.typing.MatLike,colorModeCrop:str,thresholdGrownCrop:float):
    print("Entering harvesting loop. Press q to exit.")
    while True:
        locCrop = interactionFunctions.findTheLocation(crop,colorModeCrop,thresholdGrownCrop)
        if locCrop == None:
            print("There is no grown wheat on screen! Skipping harvesting process...")
            break
        else:
            pyautogui.moveTo(locCrop[0]+50,locCrop[1]+30)
            interactionFunctions.humanLikeClick()
            interactionFunctions.waitSecondsInRange(1,2,1)
            harvest(locCrop[0]+50,locCrop[1]+30)
            interactionFunctions.waitSecondsInRange(1,2,1)
        #wait for the disappear xp and wheat icons after harvest
        interactionFunctions.waitSecondsInRange(3,4,1)
    
    print("Harvest proccess ended.")

def run():
    harvestAllCrops(grownWheat,colorModeGrownWheat,thresholdGrownWheat)