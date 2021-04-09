import unittest
from password import User

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

if __name__ == '__main__':
    unittest.main()
