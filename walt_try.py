class Wallet:
    def __init__(self,balance=0):
        self.balance = balance

    def show_balance(self):
        print(f'Current Balance: {self.balance}')

    def add_money(self,amount):
        if amount>0:
            self.balance += amount
            print(f'{amount} credited. New balance: {self.balance}')
        print('Enter positive amount')
    
    def withdrawal(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f'{amount} has been withdrawn. New Balance: {self.balance}')

class User:
    def __init__(self,name):
        self.name = name
        self.wallet = Wallet()

u1 = User('Arun')

u1.wallet.show_balance()
u1.wallet.add_money(200)
u1.wallet.withdrawal(50)