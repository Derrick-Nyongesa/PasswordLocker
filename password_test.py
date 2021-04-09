import unittest
from password import User
from password import Credential
import pyperclip

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

    def tearDown(self):
        """
        This function cleans up after each test case has run
        """
        Credential.credential_list = []

    def test_init(self):
        """
        This function tests whether  the initialization/creation of credential instances is properly done
        """
        self.assertEqual(self.new_credential.account, "Instagram")
        self.assertEqual(self.new_credential.username, "Derrick-Nyongesa")
        self.assertEqual(self.new_credential.password, "DN17w9S")

    def test_save_credential(self):
        """
        Function to test whether we can save our credential into the credential list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_credentials(self):
        """
        Function to test whether we can save multiple user credentials in our credential list
        """
        self.new_credential.save_credential()
        test_credential = Credential("Twitter", "Derrick-Daniel", "MFW673r")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    def test_delete_credential(self):
        """
        Function to test if we can remove a user credential from the credential list
        """
        self.new_credential.save_credential()
        test_credential = Credential("Twitter", "Derrick-Daniel", "MFW673r")
        test_credential.save_credential()
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_find_credential(self):
        """
        Function to test if we can find a credential in the credential_list
        """
        self.new_credential.save_credential()
        test_credential = Credential("Twitter", "Derrick-Daniel", "MFW673r")
        test_credential.save_credential()
        found_credential = Credential.find_credential("Twitter")
        self.assertEqual(found_credential.account, test_credential.account)

    def test_credential_exists(self):
        """
        Function to check if we can return a Boolean if we cannot find the credential.
        """
        self.new_credential.save_credential()
        test_credential = Credential("Twitter", "Derrick-Daniel", "MFW673r")
        test_credential.save_credential()
        credential_exists = Credential.credential_exist("Twitter")
        self.assertTrue(credential_exists)

    def test_display_all_credentials(self):
        """
        Function that returns all credentials saved
        """
        self.assertEqual(Credential.display_credentials(), Credential.credential_list)

    def test_copy_credential(self):
        """
        Function that tests to check if the copy a credential made is successful
        """
        self.new_credential.save_credential()
        twitter = Credential("Twitter", "Derrick-Nyongesa", "MFW673r")
        twitter.save_credential()
        find_credential = None
        for credential in Credential.credential_list:
            find_credential = Credential.find_credential(credential.account)
            return pyperclip.copy(find_credential.password)
        Credential.copy_credential(self.new_credential.account)
        self.assertEqual("MFW673r", pyperclip.paste())
        print(pyperclip.paste())
        

if __name__ == '__main__':
    unittest.main()
