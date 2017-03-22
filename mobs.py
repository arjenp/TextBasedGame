import random


class Mob:

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

    def get_strength(self):
        return self.strength
