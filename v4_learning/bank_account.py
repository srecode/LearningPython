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

#write a unit test for above code for negetive test case
# class TestAccount(unittest.TestCase):
#     def test_withdraw(self):
#         acct = Account("Sam", 500)
#         acct.with_draw(600)
#         self.assertEqual(acct.balance, 500)
#      acct.with_draw(500)
#         self.assertEqual(acct.balance, 0)
#     def test_deposite(self):
#         acct = Account("Sam", 500)
#         acct.deposite(100)
#         self.assertEqual(acct.balance, 600)
# if __name__ == '__main__':
#     unittest.main()
    
class TestAccount(unittest.TestCase):
    def test_deposite(self):
        acct = Account("Sam", 5000000000000000)
        acct.deposite(100)
        self.assertEqual(acct.balance, 5000000000000100)
    def test_withdraw(self):
        acct = Account("Sam", 5000000000000000)
        acct.with_draw(50000000000001000)
        self.assertEqual(acct.balance, 0)
    def test_withdraw2(self):
        acct = Account("Sam", 5000000000000000)
        acct.with_draw(1000)
        self.assertEqual(acct.balance, 4999999999999000)
if __name__ == '__main__':
    unittest.main()
