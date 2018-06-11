from dataclass import Account
from dataclass import Passwords
def createaccount(firstname,lastname,email):
    new_account = Account(firstname,lastname,email)
    return new_account
def saveaccount(account):
     account.saveaccount()    


def createcredential(credentialname,password,email):
    new_account2 = Passwords(credentialname,password,email)
    return new_account2

def getcredential(credentialname):
    return credentialname

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

                            saveaccount(createaccount(firstname,lastname,email)) 
                            print ('\n')
                            print(f"New Contact {firstname} {lastname} created")
                            print ('\n')
                    
                    elif short_code == 'fp':

                            print("Enter the crdential you want to search for")

                            search_credential = input()
                            if getcredential(credentialname):
                                    search_credential = getcredential(credentialname)
                                    print(f"{search_credential.credentialname} {search_credential.password}")
                                    print('-' * 20)

                                    print(f"Credential.......{search_credential.phone_number}")
                                    print(f"password.......{search_credential.email}")
                            else:
                                    print("That credential does not exist")
                    
                    elif short_code == "ex":
                            print("Bye .......")
                            break





if __name__ == '__main__':

    main()

    
                            


