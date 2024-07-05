# OOP PROJECT
class BalanceException(Exception):    # Exception class
    pass


class BankAccount:
    def __init__(self, initialAmount, acctName):    # Takes and prints initial bal. and acc. name
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created. \nBalance = '${self.balance:.2f}'")

    def getBalance(self):      # Prints name, account balance
        print(f"\nAccount '{self.name}' Balance = '{self.balance:.2f}'")

    def deposit(self, amount):     # Updates initial bal. with amount, prints deposit complete, calls get balance function
        self.balance += amount
        print(f"\nDeposit complete")
        self.getBalance()

    def viableTransaction(self, amount):    # verifies if transaction is possible
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Sorry account '{self.name}' only has a balance of '${self.balance}'")

    def withdraw(self, amount):      # Withdrawal
        try:
            self.viableTransaction(amount)    # Verifies if next line runs
            self.balance = self.balance - amount
            print("\nWithdrawal Complete")
            self.getBalance()
        except BalanceException as error:     # Catches the error, not in the try statement
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):     #Transfer 'amount' to 'account'
        try:
            print('\n**********\n\nBeginning Transfer...🚀🚀🚀🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete 👌✅\n\n**********")
        except BalanceException as error:
            print(f"\nSorry, this transfer was interrupted. ❌ {error}")


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance += 1.05*amount       #adds ammount with bonus of 5%
        print("\nDeposit complete")
        self.getBalance()


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)   # The total withdrawn amount - with the fee
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}.")
