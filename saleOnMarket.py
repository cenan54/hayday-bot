import cv2 as cv
import pyautogui
import interactionFunctions



marketOnStreet = cv.imread("./imgs/marketOnStreet.png")
colorModeMarketOnStreet = "rgb"
thresholdMarketOnStreet = 0.6

soldItem = cv.imread("./imgs/sold.png")
colorModeSoldItem = "rgb"
thresholdSoldItem = 0.8


def clickOnStreetMarket():
    marketLocation=interactionFunctions.findTheLocation(marketOnStreet,colorModeMarketOnStreet,thresholdMarketOnStreet)
    pyautogui.moveTo(marketLocation)
    interactionFunctions.humanLikeClick()


interactionFunctions.waitSecondsInRange(5,6,1)#TEMPORARY CODE  Delete this codeeeee

def collectAllSoldItems():
    while True:
        soldItemLocation = interactionFunctions.findTheLocation(soldItem,colorModeSoldItem,thresholdSoldItem)
        if soldItemLocation == None:
            print("There is no sold item on shop!")
            break
        else:
            pyautogui.moveTo(soldItemLocation)
            interactionFunctions.humanLikeClick()
        interactionFunctions.waitSecondsInRange(1,2,1)



#loop for create new sales
#put advertise one of them wheat
#wait 1 minute




