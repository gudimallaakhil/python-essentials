
# Question 1
# For this challenge, create a bank account class that has two attributes:
# *ownerName
# *Balance
# And two methods
# *deposit
# *withdraw
# As an added requirement, withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn


class Bank_Account:
    def __init__(self):
        self.ownerName = ""
        self.balance = 0

    def set_ownerName(self):
        name = input("\nEnter the Name: ")
        self.ownerName = name

    def get_ownerName(self):
        print("Welcome ", self.ownerName)

    def deposit(self):
        amount = float(input("\nEnter amount to be Deposited: "))
        self.balance += amount
        print("Amount Deposited : ", amount)

    def withdraw(self):
        amount = float(input("\nEnter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("You Withdrew : ", amount)
            print("Have a Great Day !")
        else:
            print("Insufficient balance  ")
            chk_bal = input("\nCheck Available Balance (Y/N): ")
            if chk_bal.lower() == "y":
                print("Net Available Balance : ", self.balance)
                print("Have a Great Day !")
            else:
                print("Have a Great Day !")
s = Bank_Account()

s.set_ownerName()
s.get_ownerName()
s.deposit()
s.withdraw()

p = Bank_Account()

p.set_ownerName()
p.get_ownerName()
p.deposit()
p.withdraw()
