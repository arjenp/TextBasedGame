import random

class Mob:

    RAT = ["Rat", 15, 0.25, 3, 0, 0.2]
    TROLL = ["Troll", 60, 0.35, 16, 5, 2.0]
    NECROMANCER = ["NECROMANCER", 999, 0.95, 99, 30, 50.0]

    MOB_NAME = 0
    MOB_HIT_POINTS = 1
    MOB_ATTACK = 2
    MOB_STRENGTH = 3
    MOB_ARMOR = 4
    MOB_LOOT_MODIFIER = 5

    def __init__(self):
        self.name = ""
        self.hit_points = 1
        self.attack = 0
        self.strength = 1
        self.armor = 1
        self.loot_modifier = None

    def init_mob(self, attributes):
        self.name = attributes[self.MOB_NAME]
        self.hit_points = attributes[self.MOB_HIT_POINTS]
        self.attack = attributes[self.MOB_ATTACK]
        self.strength = attributes[self.MOB_STRENGTH]
        self.armor = attributes[self.MOB_ARMOR]
        self.loot_modifier = attributes[self.MOB_LOOT_MODIFIER]

    def process_damage(self, damage):
        self.hit_points -= (damage - random.randint(0, self.armor))
        if self.hit_points <= 0:
            print("The " + self.name + " dies!")
            return self.loot_modifier


