from PIL import Image, ImageGrab
import cv2 as cv
import numpy as np
import time

class MainAgent:
    def __init__(self)-> None:
        self.currentImg = None
        self.currentImgHSV = None
        print("Main Agent Setup Complete")

    
def update_screen(agent):
    agent.currentImg = ImageGrab.grab()
    agent.currentImg = np.array(agent.currentImg)
    agent.currentImg = cv.cvtColor(agent.currentImg,cv.COLOR_BGR2RGB)
    agent.currentImgHSV = cv.cvtColor(agent.currentImg,cv.COLOR_RGB2HSV)
    cv.imshow("Vision",agent.currentImgHSV)

    cv.waitKey(1)
       
def print_menu():
    print("Welcome to the wheater bot for Hay Day.")
    print("Enter a key to choose option shown below.")
    print("\tw --> Start the cropping bot.")
    print("\tq --> Exit the app.")
    

if __name__=="__main__":
    print_menu()
    
    while True:
        userInput = input()
        userInput = str.lower(userInput).strip()
        if userInput=="w":
            mainAgent = MainAgent()
            update_screen(mainAgent)
        elif userInput=="q":
            print(f"You have pressed the {userInput} button.Exiting app...")
            break
        else:
            print(f"Key {userInput} is not a valid character.")
    
    
    