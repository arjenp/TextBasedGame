import WorldInformation
import Actions
import PlayerInformation
import Adventure
import mobs


class GameRunner:

    def __init__(self):
        pass

    def play(self):
        action_handler = Actions.ActionHandler()
        player = PlayerInformation.Player()
        mob = mobs.Mob()

        WorldInformation.introWorld()
        action_handler.standardActions()


        print("You will now be choosing your name and your class.")
        player_name = input("What is your name: ")
        print("Welcome to the game" + player_name + "!")

        player.set_player_information(player_name)

        print("Welcome to the World Of Adventure " + player.name + " the " + player.description)

        Adventure.startTheAdventure(player, mob, action_handler)


if __name__ == "__main__":
    game_runner = GameRunner()
    game_runner.play()