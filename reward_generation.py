import random


class RewardGenerator:

    def __init__(self):
        pass

    def generate_loot(self, modifier):
        loot_base_amount = random.randint(1, 25)
        loot_final = loot_base_amount * modifier
        return loot_final


