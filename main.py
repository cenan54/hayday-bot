import harvestingBot,plantingBot,saleOnMarket
import interactionFunctions
import menu
import time


def main():
    menu.print_menu()
    while True:
        userInput = input()
        userInput = str.lower(userInput).strip()
        if userInput=="w":
            print("Bot will be started in 10 seconds...")
            time.sleep(10)
            while True:
                loopCount = 0
                harvestingBot.run()
                interactionFunctions.waitSecondsInRange(2,5,1)
                plantingBot.run()
                interactionFunctions.waitSecondsInRange(2,5,1)
                saleOnMarket.run()
                interactionFunctions.waitSecondsInRange(2,5,1)
                loopCount += 1
                print(f'{loopCount}. loop ended. Starting{loopCount+1}. loop in about 1 minute.')
                interactionFunctions.waitSecondsInRange(60,70,1)
            menu.print_menu()
        elif userInput=="q":
            print(f"You have pressed the {userInput} button.Exiting app...")
            break
        else:
            print(f"Key {userInput} is not a valid character.")



if __name__=="__main__":
    main()



    

# if __name__=="__main__":
#     print_menu()
    

    
    
    