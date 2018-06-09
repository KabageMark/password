from dataclass import Account
from dataclass import Passwords
def ceateaccount(firstname,lastname,email):
    new_account = Account(firstname,lastname,email)
    return new_account
    

def createcredential(password,email):
    new_account2 = Passwords(password,email)
    return new_account2

def main():
    print("Hello Welcome to your password list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cc - create a new account,  fp -find a password, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New account")
                            print("-"*10)

                            print ("Firstname ....")
                            firstname = input()

                            print("Last name ...")
                            lastname = input()

                            print("email ...")
                            email = input()

                            new_account(Account(firstname,lastname,email)) # create and save new contact.
                            print ('\n')
                            print(f"New Contact {firstname} {lastname} created")
                            print ('\n')





if __name__ == '__main__':

    main()
                            


