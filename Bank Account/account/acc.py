class Account:
    def __init__(self, acctname, filepath):
        self.filepath = filepath
        self.acctname = acctname
        try:
            with open(filepath, 'r') as file:
                self.balance = int(file.read())
        except:
            print("File read error or no balance in file")
            self.balance = 0

    def __str__(self):
        retstr = f"Account balance of '{self.acctname}' is {self.balance}"
        return retstr

    def withdraw(self,amt):
        if self.balance > amt:
            self.balance = self.balance - amt
            print(f"{amt} successfully withdrawn. Remaining balance is : {self.balance}")
        else:
            print(f"No sufficient balance. Balance : {self.balance}, Withdraw request : {amt}")

    def deposit(self, amt):
        self.balance = self.balance + amt
        print(f"{amt} successfully deposited to account. New account balance : {self.balance}")

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    type = "Checking"
    def __init__(self, acctname, filepath):
        
        Account.__init__(self,acctname, filepath)

    def transfer(self, amt, newacct):
        if self.balance > amt:
            self.balance = self.balance - amt
            newacct.balance = newacct.balance + amt
            print(f"Amount {amt} successfully transferred. Source Account balance: {self.balance}. Target account balance: {newacct.balance}")
        else:
            print(f"No sufficient funds to transfer. Account Balance: {self.balance}, Tranferred amount: {amt}")




""" 
account=Account("balance.txt")
print(account)
account.withdraw(500)
print(account)
account.deposit(1500)
print(account)
account.commit()             
"""

chkacct1 = Checking("Checking Account 1", "balance.txt")
chkacct2 = Checking("Checking Account 2", "balance.txt")
print(chkacct1)
print(chkacct2)
chkacct1.transfer(500, chkacct2)
print(chkacct1)
print(chkacct2)