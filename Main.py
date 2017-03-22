import WorldInformation
import Actions
import PlayerInformation
import Adventure

def play():


    WorldInformation.introWorld()
    Actions.standardActions()


    print("You will now be choosing your name and your class.")
    playerName = input("What is your name:")
    print("Welcome to the game" + playerName + "!")
    PlayerInformation.Player.name = playerName

    PlayerInformation.setPlayerInformation()

    print("Welcome to the World Of Adventure "+ PlayerInformation.Player.name + " the " + PlayerInformation.Player.description)

    Adventure.startTheAdventure()





if __name__ == "__main__":
    play()