#!/usr/bin/env python3.9

from password import User
from password import Credential

def create_user(username, password):
    """
    Function to create a new user account

    Args:
        username: New username
        password : New password
    """
    new_user = User(username, password)
    return new_user

def save_user(user):
    """
    Function to save new user
    """
    user.save_user()

def verify_user(username, password):
    """
    Function that verifies the existance of the user before creating credentials
    """
    check_user = Credential.user_exist(username, password)
    return check_user

