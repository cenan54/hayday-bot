import cv2 as cv
import pyautogui
import interactionFunctions


marketOnStreet = cv.imread("./imgs/marketOnStreet.png")
colorModeMarketOnStreet = "rgb"
thresholdMarketOnStreet = 0.6

crateEmptyMarket = cv.imread("./imgs/crateEmptyMarket.png")
colorModeCrateEmptyMarket = "hsv"
thresholdCrateEmptyMarket = 0.7

soldItem = cv.imread("./imgs/sold.png")
colorModeSoldItem = "hsv"
thresholdSoldItem = 0.8

wheatIconOnShop = cv.imread("./imgs/wheatIconOnShop.png")
colorModeWheatIconOnShop = "rgb"
thresholdWheatIconOnShop = 0.6

wheatIncreaseButton = cv.imread("./imgs/wheatIncreaseQuantityButton.png")
colorWheatIncreaseButton = "rgb"
thresholdWheatIncreaseButton = 0.7

priceDecreaseButton = cv.imread("./imgs/priceDecreaseButton.png")
colorModePriceDecreaseButton = "rgb"
thresholdPriceDecreaseButton = 0.7

putOnSaleButton = cv.imread("./imgs/putOnSaleButton.png")
colorModePutOnSaleButton = "rgb"
thresholdPutOnSaleButton = 0.7

closeButton = cv.imread("./imgs/closeButton.png")
colorModeCloseButton = "rgb"
thresholdCloseButton = 0.7

interactionFunctions.waitSecondsInRange(5,6,1)#TEMPORARY CODE  Delete this codeeeee

def clickOnStreetMarket():
    marketLocation=interactionFunctions.findTheLocation(marketOnStreet,colorModeMarketOnStreet,thresholdMarketOnStreet)
    pyautogui.moveTo(marketLocation)
    interactionFunctions.humanLikeClick()

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

def createNewSale():
    while True:    
        crateEmptyLoc = interactionFunctions.findTheLocation(crateEmptyMarket,colorModeCrateEmptyMarket,thresholdCrateEmptyMarket)
        #checking for any empty box on roadside shop
        if crateEmptyLoc == None:
            print("There is no empty crate on screen!")
            break
        else:
            pyautogui.moveTo(crateEmptyLoc)
            interactionFunctions.humanLikeClick()
            interactionFunctions.waitSecondsInRange(1,1,1)
            wheatIconLoc = interactionFunctions.findTheLocation(wheatIconOnShop,colorModeWheatIconOnShop,thresholdWheatIconOnShop)
            #checking for is any wheat left on silo
            if wheatIconLoc == None:
                print("There is no wheat on screen or on your silo!")
                #first close x button
                closeButtonLoc = interactionFunctions.findTheLocation(closeButton,colorModeCloseButton,thresholdCloseButton)
                pyautogui.moveTo(closeButtonLoc[0],closeButtonLoc[1])
                interactionFunctions.humanLikeClick()
                break
            else:
                pyautogui.moveTo(wheatIconLoc[0]+10,wheatIconLoc[1])
                interactionFunctions.humanLikeClick()
                interactionFunctions.waitSecondsInRange(1,2,1)
                #increase crop quantity
                wheatIncreaseButtonLoc = interactionFunctions.findTheLocation(wheatIncreaseButton,colorWheatIncreaseButton,thresholdWheatIncreaseButton)
                pyautogui.moveTo(wheatIncreaseButtonLoc[0]+100,wheatIncreaseButtonLoc[1]+23)
                for i in range(0,11):
                    interactionFunctions.humanLikeClick()
                #setting crop value to 1 coin
                priceDecreaseButtonLoc = interactionFunctions.findTheLocation(priceDecreaseButton,colorModePriceDecreaseButton,thresholdPriceDecreaseButton)
                pyautogui.moveTo(priceDecreaseButtonLoc[0]+20,priceDecreaseButtonLoc[1]+20)
                interactionFunctions.humanLikeClick()
                interactionFunctions.waitSecondsInRange(1,1,1)
                #final button press for putting on sale
                putOnSaleButtonLoc = interactionFunctions.findTheLocation(putOnSaleButton,colorModePutOnSaleButton,thresholdPutOnSaleButton)
                pyautogui.moveTo(putOnSaleButtonLoc[0],putOnSaleButtonLoc[1])
                interactionFunctions.humanLikeClick()







