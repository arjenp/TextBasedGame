import random
import WorldInformation


class ActionHandler:

    def getUserInput(self,text):
        return input(text).lower()

    def standardActions(self):
        print(" ")
        print("You can choose between the following actions:")
        print("Get information about the world. Keyword: worldinformation")
        print("Get specific information about an object or beast. Keyword: info Object/beast name")
        print("Continue with the adventure. Keyword: continue")
        print("Exit the game. All progress will be lost. Keyword: Exit")
        standard_action = ActionHandler.getUserInput(self,"action: ")

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
        action = ActionHandler.getUserInput(self,"Choose yes or no: ")
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

        return ActionHandler.getUserInput(self,"Action")

    def combat_loop(self, player, mob):
        fatality = -1
        while fatality < 0:
            fatality = self._handle_combat(player, mob)
            if fatality < 0:
                fatality = self._handle_combat(mob, player)
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
        if damage_dealt < 0:
            damage_dealt = 0
        print("The attack deals " + str(damage_dealt) + " damage!")
        defender.hit_points -= damage_dealt
        print(defender.name + " has " + str(defender.hit_points) + " hit points remaining.")
        if defender.hit_points <= 0:
            print(defender.name + " dies!")
            print(attacker.name + " is victorious!\n")
            try:
                return defender.loot_modifier
            except Exception:
                return 0
        return -1

    def shoppingTime(self, player):
        print("The shopkeeper has the following items for sale:")
        print("A shield that boost armor with 5 for 4 gold. Keyword: Shield")
        print("A powerful staff that boosts magic with 6 for 5 gold. Keyword: Staff")
        print("A bucket of water that gives you 2 extra hit points for 2 gold (it's better than nothing). Keyword: Bucket")
        print("Your current gold is: " + str(player.gold))
        itemToBuy = ActionHandler.getUserInput(self,"What to buy: ")
        if itemToBuy == "shield" and player.gold >= 4:
            player.armor += 5
            player.gold -= 4
            print("You feel more powerful with the shield and your armor has increased by 5 to " + str(player.armor))

        elif itemToBuy == "staff" and player.gold >= 5:
            player.magical_power += 6
            player.gold -= 5
            print(
                "You feel more powerful with the staff and your magical power has increased by 6 to " + str(player.magical_power))

        elif itemToBuy == "bucket" and player.gold >= 2:
            player.hit_points += 2
            player.gold -= 2
            print("You feel refreshed and can take more hits! Your hit points have increased by 2 to " + str(player.hit_points))
        else:
            "This isn't an item to buy!"
            self.shoppingTime(player)
        print("Your current gold is: " + str(player.gold))

    def timeToWinOrLose(self):
        winningNumber = random.randint(1, 20)
        if winningNumber == 15:
            print("The tile falls slightly behind you and hits an enemy who was sneaking up on you.")
            print("You see that it is the necromancer!")
            print("He appears to be dead... You have won the game!!")
        else:
            print("The tile was the accursed Roof Tile of Hero Slaying +5!")
            print("YOU HAVE DIED.")
        print("THE END.")
        quit()





