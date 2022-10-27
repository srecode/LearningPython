# Object Oriented Programming Challenge
# For this challenge, create a bank account class that has two attributes:

# owner
# balance
# and two methods:

# deposit
# withdraw
# As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

from time import sleep
from traceback import print_tb
from unicodedata import name


class BackAccount:

    deposit = 0

    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance

    def __str__(self) -> str:
        return f"Account Summary:\n     Account owner: {self.owner}\n     Account balance: {self.balance}"

    def deposit(self, deposit):
        # self.deposit = deposit
        self.balance = self.balance + deposit
        return f"After deposit of {deposit} new balance is {self.balance}"

    def withdraw(self, withdraw):
        # self.withdraw = withdraw
        if withdraw > self.balance:
            return f"Withdrawal cannot not be more than balanace {self.balance}"
        else:
            self.balance = self.balance - withdraw
            return f"After withdrawal of {withdraw} new balance is {self.balance}"
    

acct1 = BackAccount("Sam", 200)

print(acct1)

print(acct1.deposit(100))
print(acct1.withdraw(250))
print(acct1.withdraw(100))