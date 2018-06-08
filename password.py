from dataclass import Account
def ceateaccount(firstname,lastname,email):
    new_account = Account(firstname,lastname,email)
    return new_account
from dataclass import Passwords
def createcredential(account,password):
    new_account2 = Passwords(account,password)
    return new_account2

def generatecredentials(accountname):
    return Password.find(input)
