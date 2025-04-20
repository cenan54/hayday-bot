import harvestingBot,plantingBot
import interactionFunctions
import menu
import time


def main():
    menu.print_menu()
    while True:
        userInput = input()
        userInput = str.lower(userInput).strip()
        if userInput=="w":
            time.sleep(10)
            harvestingBot.run()
            interactionFunctions.waitSecondsInRange(2,5,1)
            plantingBot.run()
        elif userInput=="q":
            print(f"You have pressed the {userInput} button.Exiting app...")
            break
        else:
            print(f"Key {userInput} is not a valid character.")



if __name__=="__main__":
    main()



    

# if __name__=="__main__":
#     print_menu()
    

    
    
    