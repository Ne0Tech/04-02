class BankAccount:
    bank_name = "Fred's Bank"
    num_account = 0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        BankAccount.num_account += 1

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    @classmethod
    def display_bank_info(cls):
        print(f"Bank: {cls.bank_name}")
        print(f"Total accounts: {cls.num_account}")


account_1 = BankAccount("Charlie", 100)
account_2 = BankAccount("Mike", 200)
BankAccount.display_bank_info()

account_1.deposit(50)
account_2.withdraw(30)