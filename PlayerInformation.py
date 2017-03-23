class Player:

    def __init__(self):
        self.name = ""
        self.description = ""
        self.magical_power = 0
        self.attack = 0.0
        self.strenght = 0
        self.armor = 0
        self.gold = 0
        self.hit_points = 0

    def get_strength(self):
        return self.strenght

    def set_player_information(self, player_name):
        print("\nPlease choose your class: ")
        print("For the mighty warrior. Keyword: Warrior")
        print("For the magical wizard. Keyword: Wizard")
        print("For the sneaky assassin. Keyword: Assassin")
        print("For the lazy student.(Warning: This is a weak class) Keyword: Student")

        self.name = player_name
        playerClass = input("\nWhat is your class? ").lower()

        if playerClass == "warrior":
            self.description = "Mighty Warrior"
            self.attack = 0.75
            self.strenght = 10
            self.magical_power = 1
            self.armor = 10
            self.hit_points = 100

        elif playerClass == "wizard":
            self.description = "Magical Wizard"
            self.attack = 0.50
            self.strenght = 2
            self.magical_power = 15
            self.armor = 3
            self.hit_points = 60

        elif playerClass == "assassin":
            self.description = "Sneaky Assassin"
            self.attack = 0.90
            self.strenght = 8
            self.magical_power = 4
            self.armor = 5
            self.hit_points = 80

        elif playerClass == "student":
            self.description = "Lazy Student"
            self.attack = 0.35
            self.strenght = 1
            self.magical_power = 1
            self.armor = 1
            self.hit_points = 70

        else:
            print("Please choose a viable class")
            self.set_player_information(player_name)
