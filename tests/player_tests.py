import unittest
import PlayerInformation


class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.player = PlayerInformation.Player()

    def test_initial_assignment(self):
        self.assertTrue(self.player.get_strength() == 0)


if __name__ == '__main__':
    player_test = PlayerTest()
    player_test.setUp()
    player_test.test_initial_assignment()