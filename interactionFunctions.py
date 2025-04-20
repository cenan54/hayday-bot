import cv2 as cv
from PIL import Image,ImageGrab
import time
import numpy as np
import pyautogui
import random

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
    
