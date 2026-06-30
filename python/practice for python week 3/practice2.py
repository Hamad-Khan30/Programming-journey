class Bankaccount:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self):
        amount=int(input("Please enter the depsoit amonut: "))
        self.balance += amount
        print("Balance deposit sucessfully ")
        return self.balance
        
    def withdraw(self):
        amount=int(input("Enter the amount to withdraw: "))
        if self.balance < amount:
            return ("Insufficent Balance")
        self.balance -= amount
        return (self.balance)
    def check_balance(self):
        return (f"current balance = {self.balance}")
Acc=Bankaccount("Hamad",1000)
Acc.check_balance()
Acc.deposit()
Acc.withdraw()

print(f"your balance = {Acc.balance}")


class savingaccount(Bankaccount):
    def __init__(self, name, balance=0, rate=0.05):
        super().__init__(name, balance)
        self.rate=rate
    def Addinterestt(self):
        self.balance += self.balance*self.rate
        return self.balance
saving=savingaccount("")