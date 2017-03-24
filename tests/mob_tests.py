import unittest
import mobs
import bestiary


class MobTest(unittest.TestCase):

    _INITIAL_HP = 1
    _RAT_STRENGTH = 3

    def setUp(self):
        self.mob_init = mobs.Mob()
        self.mob_rat = mobs.Mob()
        self.mob_rat.init_mob(bestiary.RAT)

    def test_mob_initialization(self):
        """
        determine if the base mob class was initialized correctly by checking its base hit points
        """
        self.assertTrue(self.mob_init.hit_points == self._INITIAL_HP)

    def test_mob_assignment(self):
        """
        determine if the assignment of the mob type went correctly by checking its strength
        """
        self.assertTrue(self.mob_rat.strength == self._RAT_STRENGTH)


def main():
    unittest.main()

if __name__ == '__main__':
    main()