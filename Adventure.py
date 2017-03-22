import PlayerInformation
import random
import Actions

playerName = PlayerInformation.Player.name
playerClass = PlayerInformation.Player.description
player = playerName + " the " + playerClass

def startTheAdventure():
    print("The adventure is beginning: ")
    print(player + " starts walking to the woods of doom")
    print("Here he will find the evil Necromancer.")
    print("But before he gets there he has a long way to go.")
    print("What is there behind that not suspiciously looking rock?")
    print("Do you want to go check it out?")
    action = Actions.chooseYesOrNo()
    if action == "yes":
        print("Yes some action you proclaim!")
        print("You walk over there and find a beast. Not sure what it is you poke it with te stick you just found.")
        print("The beast RAAWRS and stand ready for the attack!")
        Actions.fightOrDie()
    else:
        print("Well your loss lets continue")

