class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount

    def check_balance(self):
        return (f"Current Balance = {self.balance}")


class SavingAccount(BankAccount):

    def __init__(self, name, balance=0, rate=0.05):
        super().__init__(name, balance)
        self.rate = rate

    def add_interest(self):
        self.balance += self.balance * self.rate
        return self.balance


saving = SavingAccount("Hamad", 1000)

saving.deposit(500)

print(saving.check_balance())

saving.add_interest()

print(saving.check_balance())