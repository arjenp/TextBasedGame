import Actions


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
        print(mob.RAT)
        rat = mob.RAT
        mob.init_mob(rat)
        print("Yes some action you proclaim!")
        print("You walk over there and find a beast. Not sure what it is you poke it with the stick you just found.")
        print("The beast RAAWRS and stand ready to attack!")
        action_handler.fight_or_die(player, mob)
    else:
        print("You avoid all plot hooks and finish the adventure without anything peculiar happening. "
              "Boring! Just go to the damned rock, would you?")
        startTheAdventure(player)


    print(player_full + " starts walkin away after his encounter. In the distance he sees a shop.")
    print("Pretty weird to have a shop in the middle of nowhere. But you enter anyway")
    action_handler.shoppingTime(player)
    print("Happy with your shopping you continue")
    print("You slam the door behind you and a rooftile falls")
    action_handler.timeToWinOrLose(player)

