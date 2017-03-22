import WorldInformation

def standardActions():
    print(" ")
    print("You can choose between the following actions:")
    print("Get information about the world. Keyword: worldinformation")
    print("Get specific information about an object or beast. Keyword: info Object/beast name")
    print("Continue with the adventure. Keyword: continue")
    print("Exit the game. All progress will be lost. Keyword: Exit")
    standard_action = input("Action: ").lower()

    if standard_action == "worldinformation":
        WorldInformation.introWorld()
        standardActions()

    elif standard_action[:4] == "info":
        WorldInformation.getInfo(standard_action[5:])
        standardActions()

    elif standard_action == "exit":
        print("Goodbye!")
        quit()

    elif standard_action == "continue":
        return

    else:
        print("Come one select one that is asked above. Let's try again")
        standardActions()



def playerActions():
    print("balasld")



def throwTheMagicDice():
    print("adsa")

def chooseYesOrNo():
    action = input("Choose yes or no: ").lower()
    if action == "yes" or action == "no":
        return action
    else:
        chooseYesOrNo()


def fightOrDie():
    print("You are not sure what to do")