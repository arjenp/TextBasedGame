import WorldInformation
import PlayerInformation


class ActionHandler:

    def standardActions(self):
        print(" ")
        print("You can choose between the following actions:")
        print("Get information about the world. Keyword: worldinformation")
        print("Get specific information about an object or beast. Keyword: info Object/beast name")
        print("Continue with the adventure. Keyword: continue")
        print("Exit the game. All progress will be lost. Keyword: Exit")
        standard_action = input("Action: ").lower()

        if standard_action == "worldinformation":
            WorldInformation.introWorld()
            self.standardActions()

        elif standard_action[:4] == "info":
            WorldInformation.getInfo(standard_action[5:])
            self.standardActions()

        elif standard_action == "exit":
            print("Goodbye!")
            quit()

        elif standard_action == "continue":
            return

        else:
            print("Come one select one that is asked above. Let's try again")
            self.standardActions()


    def player_actions(self):
        print("balasld")


    def throw_magic_dice(self):
        print("adsa")


    def choose_yes_or_no(self):
        action = input("Choose yes or no: ").lower()
        if action == "yes" or action == "no":
            return action
        else:
            self.choose_yes_or_no()

    def fight_or_die(self, player, mob):
        action = self._handle_input(player.description)

        # todo make it better and more stuff with it
        if action == "fight":
            print("fight")
        elif action == "run":
            print("run")
        else:
            print("Not an action")
            self.fight_or_die(player, mob)

    def _handle_input(self, player_description):
        print("You are not sure what to do")
        print("Choose an action: ")
        if player_description == "Mighty Warrior":
            print("I am a Mighty Warrior I choose to FIGHT. Keyword: Fight")
            print("Today I am not so mighty. Keyword: Run")
        elif player_description == "Magical Wizard":
            print("I will destroy this monster with my mighty spells. Keyword: Fight")
            print("Today I am not so wizardly. Keyword: Run")
        elif player_description == "Sneaky Assassin":
            print("I will kill you without you even knowing it. Keyword: Fight")
            print("Today I am going to be extra sneaky. Keyword: Run")
        elif player_description == "Lazy Student":
            print("I guess I'll fight.. Keyword: Fight")
            print("What the hell am I doing here. Keyword: Run")

        return input("Action: ").lower()