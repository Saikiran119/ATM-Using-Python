class Account:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            print(f"Withdrew: {amount}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")


    def change_pin(self, new_pin):
        self.pin = new_pin
        print("PIN changed successfully.")

    def show_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)

class ATM:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.user_id] = account

    def authenticate_user(self, user_id, pin):
        account = self.accounts.get(user_id)
        if account and account.pin == pin:
            return account
        else:
            print("Authentication failed.")
            return None

# Example usage
atm = ATM()
account1 = Account(user_id="user1", pin="1234", balance=2000)
atm.add_account(account1)

user_account = atm.authenticate_user("user1", "1234")
if user_account:
    user_account.check_balance()
    user_account.deposit(int(input("Enter Deposit Amount:")))
    user_account.withdraw(int(input("Enter Withdraw Amount:")))
    user_account.change_pin(int(input("Enter Pin Number:")))
    user_account.show_transaction_history()
