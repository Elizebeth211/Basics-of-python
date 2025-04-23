# Define a class BankAccount
class BankAccount:  
    # Class Variable (Shared among all instances, but not used in this example)
    bank_name = "XYZ Bank"  

    def __init__(self, account_holder, balance=0.0):
        """Instance Variables (Specific to each object)"""
        self.account_holder = account_holder  # Stores the account holder's name
        self.balance = balance  # Stores the account balance  

    def deposit(self, amount):
        """Method to deposit money (Affects the instance variable 'balance')"""
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        """Method to withdraw money (Ensures sufficient balance)"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{self.balance}")
        else:
            print("Insufficient balance or invalid amount!")

    def display_balance(self):
        """Displays account details using instance variables"""
        print(f"Account Holder: {self.account_holder}, Balance: ₹{self.balance}")

# Creating an Object (Instance of the class)
account1 = BankAccount("Liza", 5000)  # Object with instance variables

# Accessing Methods (Using the object to interact with the class)
account1.deposit(2000)  # Calls deposit method
account1.withdraw(1500)  # Calls withdraw method
account1.display_balance()  # Calls display_balance method

# Printing Class Variable
print("Bank Name:", BankAccount.bank_name)






