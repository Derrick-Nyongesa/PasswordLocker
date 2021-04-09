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

def save_users(user):
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

def create_credentials(account, username, password):
    """
    Function to create new user credentials

    Args:
        account: Account type
        username: New username
        password: New password
    """
    new_credential = Credential(account, username, password)
    return new_credential

def save_credentials(credential):
    """
    Function to save a new user credential
    """
    credential.save_credential()

def dis_credentials():
    """
    Function that displays various account credentials and their passwords
    """
    return Credential.display_credentials()

def del_credential(credential):
    """
    Function that takes in credential objects and calls on the delete_credential to delete
    """
    credential.delete_credential()