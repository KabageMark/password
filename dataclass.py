class Account:
    account_list = []
    def _init_(self,firstname,lastname,email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def saveaccount(self):
        Account.account_list.append(self)

class Passwords:
    password_list = []
    def _init_(self,password,email):
        self.password = password
        self.email = email

    def savepassword(self):
        Passwords.password_list.append(self)          
  
    

# class  crededntial:
#     name,password    