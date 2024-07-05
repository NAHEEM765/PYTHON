from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sarah = BankAccount(2000, "Sarah")

Dave.getBalance()
Sarah.getBalance()

Sarah.deposit(3000)
Dave.deposit(2000)

Dave.withdraw(11000)
Sarah.withdraw(1000)

Sarah.transfer(22000, Dave)
Dave.transfer(2000, Sarah)

Jim = InterestRewardsAcct(1000, "Jim")
Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Dave)

Dame = SavingsAcct(1000, "Dame")

Dame.getBalance()

Dame.deposit(150)

Dame.transfer(2650, Sarah)
Dame.transfer(650, Sarah)