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

    #made premade user acc with username and funds to it to test
    @patch('builtins.input', side_effect=['user_1', '50'])
    def test_deposit_funds(self, mock_input):

        #what the machine is going to add
        test_user = {"user_1": 100}

        deposit_funds(test_user)

        #tests if the machine added 50 dollars
        self.assertEqual(test_user['user_1'], 150)

        #makes sure the username is not an empty value
        self.assertIsNotNone(test_user['user_1'])


    #made premade user acc with username and funds to it to test
    @patch('builtins.input', side_effect=['user_2', '50'])
    def test_withdraw_funds(self, mock_input):

        #what the machine is going to subtract
        test_user = {"user_2": 100}

        withdraw_funds(test_user)

        #tests if the machine subtrcted 50 dollars
        self.assertEqual(test_user['user_2'], 50)

        #makes sure the update values didnt stay the same
        self.assertIsNot(test_user['user_2'], 100)


if __name__ == '__main__':
    unittest.main()




