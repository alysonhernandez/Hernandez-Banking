#------------------------
#Imports
from bank import check_balence, deposit_funds, withdraw_funds, create_acc, delete_acc, modify_acc
import unittest
from unittest.mock import patch


class TestingBankSys(unittest.TestCase):

    #testing the check balence function
    def test_check_balence(self):

        #making test users with usernames and funds
        test_users = [("user_1", 100), ("user_2", 200)]

        result = check_balence(test_users)

        self.assertEqual(result, ["Funds for: ('user1', 100) dollars.", "Funds for: ('user2', 200) dollars."])

    @patch('builtins.input', side_effect=['user_1', '50'])
    def test_deposit_funds(self, mock_input):

        test_user = {"user_1": 100}

        deposit_funds(test_user)

        self.assertEqual(test_user['user_1'], 150)

        self.assertIsNotNone(test_user['user_1'])


    @patch('builtins.input', side_effect=['user_2', '50'])
    def test_withdraw_funds(self, mock_input):

        #making test user
        test_user = {"user_2": 100}

        withdraw_funds(test_user)


        self.assertEqual(test_user['user_2'], 50)

        self.assertIsNot(test_user['user_2'], 100)


if __name__ == '__main__':
    unittest.main()




