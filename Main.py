import WorldInformation
import Actions
import PlayerInformation
import Adventure
import reward_generation
import Mob

class GameRunner:

    def __init__(self):
        self.reward_generator = reward_generation.RewardGenerator()

    def play(self):
        action_handler = Actions.ActionHandler()
        player = PlayerInformation.Player()
        mob = Mob.Mob

        WorldInformation.introWorld()
        action_handler.standardActions()


        print("You will now be choosing your name and your class.")
        playerName = input("What is your name: ")
        print("Welcome to the game" + playerName + "!")


        player.set_player_information(playerName)

        print("Welcome to the World Of Adventure " + player.name + " the " + player.description)

        Adventure.startTheAdventure(player, mob, action_handler)





if __name__ == "__main__":
    game_runner = GameRunner()
    game_runner.play()