import WorldInformation
import PlayerInformation

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
    print("Choose an action:")
    if PlayerInformation.Player.description == "Mighty Warrior":
        print("I am a Mighty Warrior I chose to FIGHT. Keyword: Fight")
        print("Today I am not so mighty. Keyword: Run")
    elif PlayerInformation.Player.description == "Magical Wizard":
        print("I will destroy this monster with my mighty spells. Keyword: Fight")
        print("Today I am not so wizardly. Keyword: Run")
    elif PlayerInformation.Player.description == "Sneaky Assassin":
        print("I will kill you without you even knowing it. Keyword: Fight")
        print("Today I am going to be extra sneaky. Keyword: Run")
    elif PlayerInformation.Player.description == "Lazy Student":
        print("I geuss ill fight.. Keyword: Fight")
        print("What the hell am i doing here. Keyword: Run")

    action = input("Action: ").lower()

    #todo make it better and more stuff with it
    if action == "fight":
        print("fight")
    elif action == "run":
        print("run")
    else:
        print("Not an action")
        fightOrDie()
