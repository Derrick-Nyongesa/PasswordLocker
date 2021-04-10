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

def display_credentials():
    """
    Function that displays various account credentials and their passwords
    """
    return Credential.display_credentials()

def delete_credential(credential):
    """
    Function that takes in credential objects and calls on the delete_credential to delete
    """
    credential.delete_credential()

def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credential.find_credential(account)

def copy_credential(account):
    """
    Function to copy credential to the clipboard
    """
    return Credential.copy_credential(account)

def generate_Password():
    """
    Function that generates a random password for the user
    """
    auto_password = Credential.generate_password()
    return auto_password

def application():
    print('*' * 130)
    print("Hello, welcome to Password Locker Manager. This is a web application that will help you manage your passwords for your various accounts that you are signed into.Use the following short codes to proceed.")
    print('')

    print("A - Create Account;")

    short_code = input().upper()

    if short_code == 'A':
        print("Create an account")
        print("*"*20)

        print ("Enter your username ....")
        username = input()

        print ('\n')

        print ("Enter your password ....")
        password = input()

        save_user(create_user(username,password))
        print ('\n')
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}. WELCOME TO PASSWORD LOCKER MANAGER")
        print ('\n')
        print("*"*130)
        print('\n')

        while True:
            print("Use these short codes: B - Create a new credential; C - Display Credentials; CC - Copy Credentials; D - Delete credential; EX - Exit the application ")

            print ('\n')

            short_code = input().upper()

            if short_code == 'B':
                print("Create New Credential")
                print("."*20)

                print("Account name ....")
                account = input()

                print ('\n')

                print("Your Account username")
                userName = input()
                print('\n')
                while True:
                    print(" TP - To type your own password if you already have an account or GP - To generate random Password")
                    password_choice = input().upper()
                    if password_choice == 'TP':
                        print("Enter your password")
                        password = input()
                        break
                    elif password_choice == 'GP':
                        password = generate_Password()
                        break
                    else:
                        print("Invalid password please try again")

                save_credentials(create_credentials(account,username,password))
                print('\n')
                print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
                print('\n')
            elif short_code == 'C':
                if display_credentials():
                    print("Here's your list of acoounts: ")
                    print('_'* 30)
                    print('*' * 30)

                    for account in display_credentials():
                        print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                        print('_'* 30)
                        print('*' * 30)
                else:
                    print("You don't have any credentials saved yet..........")

            elif short_code == 'CC':
                print("Enter the account name of the Credentials you want to copy")
                searched_name = input()
                print('\n')
                copy_credential(searched_name)
                searched_credential = find_credential(searched_name)
                print(f"Your credentials for : {searched_credential.account} successfully copied!!!")


            elif short_code == 'D':
                print("Enter the account name of the Credentials you want to delete")
                search_name = input()
                if find_credential(search_name):
                    search_credential = find_credential(search_name)
                    print("_"*50)
                    search_credential.delete_credential()
                    print('\n')
                    print(f"Your credentials for : {search_credential.account} successfully deleted!!!")
                    print('\n')
                else:
                    print("That Credential you want to delete does not exist in your store yet")

            elif short_code == 'EX':
                print("Thanks for using Password Locker Manager!")
                break
            else:
                print("Wrong entry... Please use the short codes")

    else:
        print("I really didn't get that. Please use the short codes")



            


    
        

if __name__ == '__main__':
    application()