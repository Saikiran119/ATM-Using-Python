# ATM-Using-Python
---

# ATM System - Python Implementation

## Overview
This project implements a basic ATM (Automated Teller Machine) system using Python. The system includes two classes:

1. **Account**: Manages individual user account details and operations.
2. **ATM**: Handles the system's core functionalities, such as managing multiple accounts and authenticating users.

---

## Features

### 1. Account Class
The `Account` class encapsulates the behavior and attributes of a bank account.

#### Attributes:
- `user_id`: A unique identifier for the account holder.
- `pin`: A personal identification number for account security.
- `balance`: The account's current balance (default is 0).
- `transaction_history`: A list to store the history of all transactions (deposits and withdrawals).

#### Methods:
- **`deposit(amount)`**: Adds the specified amount to the account balance and updates the transaction history.
- **`withdraw(amount)`**: Deducts the specified amount from the balance if sufficient funds are available, and updates the transaction history.
- **`check_balance()`**: Displays the current account balance.
- **`change_pin(new_pin)`**: Updates the account's PIN.
- **`show_transaction_history()`**: Displays all transactions for the account.

### 2. ATM Class
The `ATM` class manages the overall functionality of the ATM system.

#### Attributes:
- `accounts`: A dictionary that maps `user_id` to their respective `Account` object.

#### Methods:
- **`add_account(account)`**: Adds a new `Account` object to the system.
- **`authenticate_user(user_id, pin)`**: Authenticates a user by verifying their `user_id` and `pin`. Returns the authenticated account object if successful, otherwise prints an error message.

---

## Requirements
- Python 3.6 or higher.

---

## How to Run
1. Copy the provided code into a Python file (e.g., `atm_system.py`).
2. Run the file in a Python environment or terminal.
3. Follow the on-screen prompts to interact with the ATM system.

---

## Notes
- The system is for educational purposes and does not include advanced security features like encryption.
- Error handling is minimal; ensure inputs are correct when running the code.

Let me know if you need enhancements like advanced error handling or additional features!
