
class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        super().__init__()
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print("Sorry, minimum balance must be maintained.")
        else:
            super().withdraw(amount)


normal_account = BankAccount()
print("Initial balance of normal account:", normal_account.balance)

normal_account.deposit(5)
print("Balance of normal account after deposition of 5:", normal_account.balance)

normal_account.withdraw(6)
print("Balance of normal account after withdrawal of 6:", normal_account.balance)

print()

vip_account = MinimumBalanceAccount(10)
print("Initial balance of vip account:", vip_account.balance)

vip_account.deposit(5)
print("Balance of vip account after deposition of 5:", vip_account.balance)

vip_account.withdraw(6)
print("Balance of vip account after withdrawal of 6:", vip_account.balance)
