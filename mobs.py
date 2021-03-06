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

    def init_mob(self, mob_type):
        self.name = mob_type[self.MOB_NAME]
        self.hit_points = mob_type[self.MOB_HIT_POINTS]
        self.attack = mob_type[self.MOB_ATTACK]
        self.strength = mob_type[self.MOB_STRENGTH]
        self.armor = mob_type[self.MOB_ARMOR]
        self.loot_modifier = mob_type[self.MOB_LOOT_MODIFIER]

    def get_strength(self):
        return self.strength
