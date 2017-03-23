import random
import WorldInformation


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

    def choose_yes_or_no(self):
        action = input("Choose yes or no: ").lower()
        if action == "yes" or action == "no":
            return action
        else:
            self.choose_yes_or_no()

    def fight_or_die(self, player, mob):
        action = self._handle_input(player.description)
        print(action)
        outcome = 0
        if action == "You run.":
            print("Your foe is relentless, you cannot escape! (you pansy)")
            action = "fight"
        if action == "fight":
            outcome = self._combat_loop(player, mob)
        else:
            self.fight_or_die(player, mob)
        return outcome

    def _handle_input(self, player_description):
        print("Choose an action: ")
        if player_description == "Mighty Warrior":
            print("I am a Mighty Warrior, I choose to FIGHT. Keyword: Fight")
            print("Today I am not so mighty. Keyword: Run")
        elif player_description == "Magical Wizard":
            print("I will destroy this monster with my mighty spells. Keyword: Fight")
            print("Today I am not so wizardly. Keyword: Run")
        elif player_description == "Sneaky Assassin":
            print("I will kill you without you even knowing it. Keyword: Fight")
            print("Today I'm going to be extra sneaky. Keyword: Run")
        elif player_description == "Lazy Student":
            print("I guess I'll fight... Keyword: Fight")
            print("NOPE! Keyword: Run")
        return input("Action: ").lower()

    def _combat_loop(self, player, mob):
        participants = [player, mob]
        attacker = 0
        defender = 1
        fatality = -1
        print(fatality)
        while fatality < 0:
            fatality = self._handle_combat(participants[attacker], participants[defender])
            switch_container = attacker
            attacker = defender
            defender = switch_container
        return fatality

    def _handle_combat(self, attacker, defender):
        print(attacker.name + " attacks!")
        if self._attack_hit(attacker.attack):
            return self._process_attack_result(attacker, defender)
        else:
            print("The attack was ineffective!")
            return -1

    def _attack_hit(self, hit_chance):
        return random.uniform(0, 1) < hit_chance

    def _process_attack_result(self, attacker, defender):
        damage_dealt = (attacker.get_strength() - random.randint(0, defender.armor))
        print("The attack deals " + str(damage_dealt) + " damage!")
        defender.hit_points -= damage_dealt
        print(defender.name + " has " + str(defender.hit_points) + " hit points remaining.")
        if defender.hit_points <= 0:
            print(defender.name + " dies!")
            print(attacker.name + " is victorious!")
            try:
                return defender.loot_modifier
            except Exception:
                return 0
        return -1
