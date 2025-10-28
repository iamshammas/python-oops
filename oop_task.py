# You’ll create a BankAccount class that can:

# 1. Store account_number, holder_name, and balance.


# 2. Have methods:

# deposit(amount) → adds money

# withdraw(amount) → subtracts money (only if balance is enough)

# display_balance() → prints the current balance


class BankAccount:
    def __init__(self,account_number,holder_name,balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            res = f'{amount} has been credited to your account'
            return res
        else:
            print('Enter amount greater than 0')

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            res = f'{amount} has been debited from your account'
            return res
        else:
            return 'Your account does not have enough balance'

    def display_balance(self):
        out = f'AN: {self.account_number} \nHOLDER: {self.holder_name} \nBalance: {self.balance}'
        return out
    

p1 = BankAccount(123,'Shamsu')
print('==========================')
print(p1.display_balance())
print('==========================')
print(p1.deposit(750))
print('==========================')
print(p1.display_balance())
print('==========================')
print(p1.withdraw(500))
print('==========================')
print(p1.display_balance())
print('==========================')