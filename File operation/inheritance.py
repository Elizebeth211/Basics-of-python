# Parent Class
class BankAccount:  
    bank_name = "XYZ Bank"  # Class Variable
    
    def __init__(self, account_holder, balance=0.0):
        """Instance Variables"""
        self.account_holder = account_holder  
        self.balance = balance  

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{self.balance}")
        else:
            print("Insufficient balance or invalid amount!")

    def display_balance(self):
        """Displays account details"""
        print(f"Bank: {BankAccount.bank_name}")  
        print(f"Account Holder: {self.account_holder}, Balance: ₹{self.balance}")

# Child Class (Inherits from BankAccount)
class SavingsAccount(BankAccount):  
    def __init__(self, account_holder, balance=0.0, interest_rate=5.0):
        """Initialize SavingsAccount using Parent Constructor"""
        super().__init__(account_holder, balance)  # Calls parent class __init__
        self.interest_rate = interest_rate  # New attribute specific to SavingsAccount

    def add_interest(self):
        """Calculate and add interest"""
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        print(f"Interest of ₹{interest} added. New balance: ₹{self.balance}")

#Creating an Object of SavingsAccount
savings = SavingsAccount("Liza", 5000)  

#Using Inherited Methods
savings.deposit(2000)  
savings.withdraw(1500)  
savings.display_balance()  

#Using Child Class Method
savings.add_interest()  
