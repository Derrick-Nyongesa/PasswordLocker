import unittest
from password import User
from password import Credential

class TestUser(unittest.TestCase):
    """
    Test class that defines the test cases for the user class behaviours.

    Args:
        unittest: TestCase class that helps in creating test cases.
    """

    def setUp(self):
        """
        Set up method before each test cases.
        """
        self.new_user = User("Derrick-Nyongesa", "DN17w9S")

    def test_init(self):
        """
        This function tests if the object is initialized properly
        """
        self.assertEqual(self.new_user.username, "Derrick-Nyongesa")
        self.assertEqual(self.new_user.password, "DN17w9S")

    def test_save_user(self):
        """
        This function tests if the object is saved into the user list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


class TestCredential(unittest.TestCase):
    """
    A test class that defines test cases for credentials class

    Args:
        unittest: TestCase class that helps in creating test cases.
    """

    def setUp(self):
        """
        This function runs before each test of the account's credentials.
        """
        self.new_credential = Credential("Instagram", "Derrick-Nyongesa", "DN17w9S")

    def test_init(self):
        """
        This function tests whether  the initialization/creation of credential instances is properly done
        """
        self.assertEqual(self.new_credential.account, "Instagram")
        self.assertEqual(self.new_credential.username, "Derrick-Nyongesa")
        self.assertEqual(self.new_credential.password, "DN17w9S")

if __name__ == '__main__':
    unittest.main()
