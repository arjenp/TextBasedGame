class Player():

    def __init__(self, name, description, magicalPower, strenght, armor):
        self.name = name
        self.description = description
        self.magicalPower = magicalPower
        self.strenght = strenght
        self.armor = armor


    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.magicalPower, self.strenght, self.armor)



def setPlayerInformation():

    print("Please choose your class:")
    print("For the mighty warrior. Keyword: Warrior")
    print("For the magical wizard. Keyword: Wizard")
    print("For the sneaky assassin. Keyword: Assassin")
    print("For the lazy student.(Warning: This is a weak class) Keyword: Student")
    playerClass = input("What is your class").lower()

    if playerClass == "warrior":
        Player.description = "Mighty Warrior"
        Player.strenght = 10
        Player.magicalPower = 1
        Player.armor = 10

    elif playerClass == "wizard":
        Player.description = "Magical Wizard"
        Player.strenght = 2
        Player.magicalPower = 15
        Player.armor = 3

    elif playerClass == "assassin":
        Player.description = "Sneaky Assassin"
        Player.strenght = 8
        Player.magicalPower = 4
        Player.armor = 5

    elif playerClass == "student":
        Player.description = "Lazy Student"
        Player.strenght = 1
        Player.magicalPower = 1
        Player.armor = 1

    else:
        print("Please chose a viable class")
        setPlayerInformation()




