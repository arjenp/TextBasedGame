import random


def generate_loot(modifier):
    loot_base_amount = random.randint(10, 26)
    loot_final = int(loot_base_amount * modifier)
    return loot_final



