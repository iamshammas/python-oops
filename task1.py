# Define a class BankAccount with deposit and withdraw methods and a balance attribute.

class BankAccount:
    def __init__(self):
        self.balance =0
    def deposit(self,deposit_amount):
        self.deposit_amount = deposit_amount
        self.balance+=deposit_amount
        return self.balance
    def withdraw(self,withdraw_amount):
        self.withdraw_amount = withdraw_amount
        self.balance -= withdraw_amount
        return f'{self.withdraw_amount} has been withdrawn \n{self.balance} is your current balance'
    def balance(self):
        return self.balance

acc = BankAccount()
print(acc.deposit(500))
print(acc.withdraw(200))
# print(acc.balance)