class User:
    """
    Class that generates new instances of the user
    """

    user_list = []

    def __init__(self, username, password):
        """
        Method to define the properties for each user object will hold.

        Args:
            username: Users username
            password: Users password
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        This method saves user objects into user_list
        """
        User.user_list.append(self)


class Credential():
    """
    Class to create  account credentials, generate passwords and save their information
    """
    credential_list = []

    @classmethod
    def user_exist(cls, username, password):
        """
        Function that checks if the user exists

        Args:
            username: search if the username exists
            password: search if the password exists
        """
        current_user = ''
        for user in cls.user_list:
            if (user.username == username and user.password == password):
                current_user == username
        return False

    def __init__(self, account, username, password):
        """
        Method that helps us define properties for our objects
        """
        self.account = account
        self.username = username
        self.password = password

    def save_credential(self):
        """
        Function that saves user credentials into credential list
        """
        Credential.credential_list.append(self)