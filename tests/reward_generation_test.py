import unittest
import reward_generation


class RewardGenerationTest(unittest.TestCase):

    def test_reward_generation(self):
        modifier = 2
        self.assertTrue( modifier * 10 <=reward_generation.generate_loot(modifier) <=modifier* 26)

if __name__ == '__main__':
    reward_test = RewardGenerationTest()
    reward_test.test_reward_generation()