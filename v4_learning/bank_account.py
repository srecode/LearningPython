class Account():

    def __init__(self, name, balance):
        self.name    = name
        self.balance = balance

    def __str__(self):
        return f"Name of the account holder is {self.name}, he/she has a balance of {self.balance}"

    def deposite(self, deposite_amount):
        self.balance += deposite_amount
        print("Deposite accepted")

    def with_draw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print("Funds not available")
        else:
            self.balance -= withdraw_amount
            print("withdrawal accepted!!!")

acct = Account("Sam", 5000000000000000)

print(acct)
acct.deposite(100)
print(acct)
acct.with_draw(50000000000001000)
print(acct)
acct.with_draw(1000)
print(acct)