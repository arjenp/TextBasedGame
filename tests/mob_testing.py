import unittest
import mobs
import bestiary


class MobTest(unittest.TestCase):

    def setUp(self):
        self.mob = mobs.Mob()
        self.mob.init_mob(bestiary.RAT)

    def test_mob_assignment(self):
        self.mob.strength = 3

def main():
    unittest.main()

if __name__ == '__main__':
    main()