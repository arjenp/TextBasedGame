import Actions

def introWorld():
    print("Welcome to the World Of Adventures.")
    print("In this world there are mighty beasts and the necromancer.")
    print("The goal of the game is to kill the necromancer.")
    print("But watch out! There are a lot of things that can kill you in the game.")


def getInfo(searchField):
    if searchField == "necromancer":
        print("The necromancer haunts the World Of Adventure since the beginning")
        print("So far no adventurer has been able to kill him.. Can you do what they couldn't?")
        print("The necromancer has 3 core abilities:")
        print("Death touch: The targeted player will die in 5 turns if the necromancer is still alive.")
        print("Summon undead: The necromancer tries to summon and undead minion.")
        print("Evil laugh: He just laughs at you since you clearly are just a nobody.")

    else:
        print("Not a real item..")

    Actions.standardActions()

