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

def savecredential(password):
     password.savepassword()     

def getcredential(credentialname):
    return Passwords.find_by_credential(credentialname)

def main():
    print("Hello Welcome to your password list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cc - create a new account, cr - create credential, fp -find a password, ex -exit the contact list ")

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
                            if getcredential(search_credential):
                                    check_existing_credential = getcredential(search_credential)
                                    print(f"{check_existing_credential.credentialname} {check_existing_credential.password}")
                                    print('-' * 20)

                                    print(f"Credential.......{search_credential.phone_number}")
                                    print(f"password.......{search_credential.email}")
                            else:
                                    print("That credential does not exist")
                    
                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    

                    elif short_code == 'cr':
                            print("New credential")
                            print("-"*10)

                            print ("Firstname ....")
                            credentialname = input()

                            print("Last name ...")
                            password = input()

                            print("email ...")
                            email = input()

                            savecredential(createcredential(credentialname,password,email)) 
                            print ('\n')
                            print(f"New Contact {credentialname} {password} created")
                            print ('\n')




if __name__ == '__main__':

    main()

    
                            


