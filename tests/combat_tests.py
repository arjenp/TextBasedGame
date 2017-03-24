import unittest
import mobs
import bestiary
from Actions import ActionHandler


class CombatTest(unittest.TestCase):

    _DEAD = 0
    _ONLY_ONE = 1
    _COMBATANT_ONE = 0
    _COMBATANT_TWO = 1

    def setUp(self):
        action_handler = ActionHandler()
        mob_rat_one = mobs.Mob()
        mob_rat_two = mobs.Mob()
        mob_rat_one.init_mob(bestiary.RAT)
        mob_rat_two.init_mob(bestiary.KOBOLD)
        combatants = [mob_rat_one, mob_rat_two]
        action_handler.combat_loop(combatants[self._COMBATANT_ONE], combatants[self._COMBATANT_TWO])
        self.combat_result = self._get_survivors(combatants)

    def test_combat(self):
        """
        Determine if only one out of two mobs survived combat
        """
        self.assertTrue(len(self.combat_result) == self._ONLY_ONE)

    def _get_survivors(self, combatants):
        """
        Determine who survived combat
        :param combatants: list of mob objects
        :return: list with mob objects with hp > self._DEATH
        """
        survivors = list()
        for combatant in combatants:
            if combatant.hit_points > self._DEAD:
                survivors.append(combatant)
        return survivors


def main():
    unittest.main()

if __name__ == '__main__':
    main()
