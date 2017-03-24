import unittest
from unittest.mock import patch
import Actions
import PlayerInformation


class ActionTest(unittest.TestCase):

    @patch('Actions.ActionHandler.getUserInput', return_value='run')
    def test_run_or_fight(self,input):
        action_handler = Actions.ActionHandler()
        output = action_handler._handle_input("Lazy Student")
        assert output == 'run'

    @patch('Actions.ActionHandler.getUserInput', return_value='shield')
    def test_shopping_time(self,input):
        action_handler = Actions.ActionHandler()
        self.player = PlayerInformation.Player()
        self.player.gold = 5
        action_handler.shoppingTime(self.player)
        self.assertEquals(self.player.gold,1)

    @patch('Actions.ActionHandler.getUserInput', return_value='yes')
    def test_choose_yes_or_no(self,input):
        action_handler = Actions.ActionHandler()
        self.assertEquals(action_handler.choose_yes_or_no(),"yes")




if __name__ == '__main__':
    action_test = ActionTest()
    action_test.test_shopping_time()
    action_test.test_run_or_fight()
    action_test.test_choose_yes_or_no