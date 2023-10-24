from __future__ import annotations
import sys
from datetime import datetime

class User:
    def __init__(self, name: str, pin: int, password: str):
        self.name = name
        self.pin = pin
        self.password = password 

    def change_name(self, new_name: str):
        self.name = new_name
        user_input = input(f"Would you like to change your name to {self.name}? [Y/N] >> ")
        if(user_input.upper() == "Y"):
            if(self.name != None):
                self.name = new_name
                print(f"Your name has been updated to {new_name} successfully.")
            elif(self.name == None):
                return None
        if(user_input.upper() != "Y"):
            print(f"Your name will not be updated to {new_name}, as of now.")
        

    def change_pin(self, new_pin: int):
        self.pin = new_pin
        if(self.pin == None): 
            return None
        else:
            self.pin = new_pin
    

    def change_password(self, new_pw: str):
        self.password = new_pw
        pw_requirements = True
        while True:
            if len(self.password) < 8: 
                pw_requirements = False
                print(f"{self.password} is not a valid password, it must be atleast 8-characters long. Try again.")
            if(len(self.password) >= 8):
                pw_requirements = True
                timestamp = datetime.now()
                print(f"Password has been authorized and changed. ({timestamp}).\n")
                self.password = new_pw
                break

        
class BankUser(User):
    def __init__(self, name: str, pin: int, password: str):
        super().__init__(name, pin, password)
        self.balance = 0
        self.credit_report = False

    def show_balance(self): print(f"{self.name} has a balance of, ${self.balance:.2f}.")

    def withdraw(self, amount: int):
        if(amount > self.balance):
            print(f"Unable to withdraw ${amount:.2f} from your bank account.\n")
        if(amount <= self.balance):
            print(f"Successfully withdrawn ${amount:.2f} from your bank account.\n")

    def deposit(self, amount: int):
        total = (self.balance + amount)
        if(amount >= 10000):
            self.credit_report = True
            print(f"You have been flagged for potentially suspicious activity to the FDIC. Status == {self.credit_report} Report ")
            self.balance = total
        elif(amount < 10000):
            self.balance = total
            print(f"Deposit successful. ${self.balance:.2f} is now in your bank account.\n")
    
    def amount_validation(amount):
        if(amount >= 0):
            return True
        if(amount < 0):
            return False
    
    def transfer_money(self, user: BankUser, amount: int) -> bool:
        # ----------Task Five ----------
        # Create more methods for the BankUser class:
        #    * transfer_money
        #        - Transfers money to another User if
        #        - correct PIN is given for transferring User
        if BankUser.amount_validation(amount) == False:
            print(f"${amount:.2f} is an invalid transfer amount.")
            return None
        if(amount > self.balance): 
            print(f"Transfer balance is ${self.balance:.2f}. Insufficient funds. ") 
            return None
        input_transfer = input(f"Would you like to transfer ${amount:.2f} to the recipient, {user.name}? [Y/N] >> ")
        if(input_transfer.upper() == "Y"):
            print(f"Authentication of {self.name} is now required. Complete immediately for a successful transfer. ")
        if(input_transfer.upper() != "Y" ):
            sys.exit()
        tc_pin = int(input("Enter your PIN: "))
        if(tc_pin == self.pin):
            self.balance -= amount
            user.balance += amount
            print("\n=================================")
            timestamp = datetime.now()
            print("Successfully authorized transfer.")
            print(f"Transferring ${amount} to {user.name} at {timestamp}")
            return True
        if(tc_pin != self.pin):
            print("Denied Transfer.")
            return False
    
    def request_receipt(self, user: BankUser):
        print(f"{user.name} now has a balance of ${user.balance:.2f} in their bank account.")

    def request_money(self, user: BankUser, amount: float) -> bool:
        if BankUser.amount_validation(amount) == False:
            print(f"${amount:.2f} is an invalid transfer amount.")
            return None
        transfer_i = input(f"Would you like to request ${amount:.2f} from user, {user.name}? [Y/N] >> ")
        if(transfer_i.upper() == "Y"):
            print(f"Authentication of {self.name} is now required. Complete immediately for a successful request. ")
        if(transfer_i.upper() != "Y" ):
            timestamp = datetime.now()
            print(f"System closing on [{timestamp}]")
            sys.exit()
        pin_i = int(input(f"Enter {user.name}'s PIN: "))
        while True:
            if(pin_i == user.pin):
                self.balance -= amount
                user.balance += amount
                BankUser.request_receipt(self, user)
                break
            else:
                print("\nIncorrect PIN entered, please try again.")
                pin_i = int(input(f"Enter {user.name}'s PIN: "))
        

print(BankUser.amount_validation(120))
bankuser1 = BankUser("Bob", 1234, "password")
bankuser2 = BankUser("Michigan", 4321, "Wolverine")
print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)
BankUser.show_balance(bankuser1)
BankUser.deposit(bankuser1, 9500)
BankUser.show_balance(bankuser1)
BankUser.transfer_money(bankuser1, bankuser2, 12)
BankUser.request_money(bankuser1, bankuser2, 1)
