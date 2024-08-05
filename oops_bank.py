print("Welcome to oops Bank.")
class Bank():
    def __init__(self,acc,balance,operation):
        self.acc=acc
        self.balance=balance
        balance = 5000
        self.operation=operation
    def show_balance(self):
        print(f"Your account balance is {self.balance}")
    def credit(self,ammount):
        self.balance += ammount
        print(F"Your current balance is {self.balance}")
    def debit(self,ammount):
        self.balance -= ammount
        print(F"Your current balance is {self.balance}")   

account_no = input("Enter your account number:")
operation = input("Enter the operation you want to perform: credit/debit/balance")
ammount = int(input("Enter the ammount:"))

c1 = Bank(account_no,5000,operation)

if operation == "credit":
    c1.credit(ammount) 
elif operation == "debit":
    c1.debit(ammount)
elif operation == "balance":
    c1.balance()
else:
    print("Invalid operation")


