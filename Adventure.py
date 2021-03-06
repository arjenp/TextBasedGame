import bestiary
from reward_generation import generate_loot


def startTheAdventure(player, mob, action_handler):
    player_full = player.name + " the " + player.description
    print("\nThe adventure is beginning: ")
    print(player_full + " starts walking to the woods of doom.")
    print("Here he will find the evil Necromancer.")
    print("But before he gets there he has a long way to go.")
    print("What is there behind that not suspiciously looking rock?")
    print("Do you want to go check it out?")
    action = action_handler.choose_yes_or_no()
    if action == "yes":
        mob.init_mob(bestiary.RAT)
        print('"Yes, some action!" you proclaim.')
        print("You walk over there and find a beast. Not sure what it is you poke it with the stick you just found.")
        print("The beast RAAWRS and stands ready to attack!")
        outcome = action_handler.fight_or_die(player, mob)
        if outcome > 0:
            player.gold += generate_loot(outcome)
            continueTheAdventure(player, action_handler, player_full)
        else:
            print("Alas, you died. Better luck next time!")
            quit()
    else:
        print("You avoid all plot hooks and finish the adventure without anything peculiar happening. "
              "Boring! Just go to the damned rock, would you?")
        startTheAdventure(player, mob, action_handler)


def continueTheAdventure(player, action_handler, player_full):
    print(player_full + " starts walking away after his encounter. In the distance he sees a shop.")
    print("Pretty weird to have a shop in the middle of nowhere. But you enter anyway.")
    action_handler.shoppingTime(player)
    print("Happy with your shopping you continue your journey.")
    print("You merrily slam the door behind you, dislodging a roof tile...")
    action_handler.timeToWinOrLose()
