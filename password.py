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