class Bank:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.acc_pass=acc_pass
    def account(self):
        print("Your account number is:",self.acc_no)
    def __password(self):#private method
        print("Your account password is:",self.acc_pass)

B1 = Bank(1234567890,1234)
print(B1.account())
print(B1.password())#it will give error because password is private method