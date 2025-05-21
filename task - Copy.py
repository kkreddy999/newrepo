import json
import os
import getpass
from datetime import datetime

DATA_FILE = 'accounts.txt'

def load_accounts():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_accounts(accounts):
    with open(DATA_FILE, 'w') as file:
        json.dump(accounts, file, indent=4)

def register(accounts):
    username = input("Enter a new username: ").strip()
    if username in accounts:
        print("Username already exists.")
        return
    pin = getpass.getpass("Set your 4-digit PIN: ")
    if not pin.isdigit() or len(pin) != 4:
        print("PIN must be 4 digits.")
        return
    accounts[username] = {
        'pin': pin,
        'balance': 0.0,
        'history': [],
        'locked': False,
        'login_attempts': 0
    }
    save_accounts(accounts)
    print("Registration successful!")

def login(accounts):
    username = input("Enter username: ").strip()
    if username not in accounts:
        print("Username does not exist.")
        return None
    if accounts[username]['locked']:
        print("Account is locked due to too many failed login attempts.")
        return None
    for attempt in range(3):
        pin = getpass.getpass("Enter PIN: ")
        if pin == accounts[username]['pin']:
            accounts[username]['login_attempts'] = 0
            save_accounts(accounts)
            print("Login successful!\n")
            return username
        else:
            print("Incorrect PIN.")
            accounts[username]['login_attempts'] += 1
            if accounts[username]['login_attempts'] >= 3:
                accounts[username]['locked'] = True
                print("Account locked due to 3 failed attempts.")
                break
            save_accounts(accounts)
    return None

def record_transaction(account, action, amount, target=None):
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    record = f"{time} - {action}: ${amount:.2f}"
    if target:
        record += f" to {target}"
    account['history'].append(record)

def atm_menu(username, accounts):
    while True:
        print(f"\n--- ATM Menu for {username} ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            print(f"Current Balance: ${accounts[username]['balance']:.2f}")
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            accounts[username]['balance'] += amount
            record_transaction(accounts[username], "Deposit", amount)
            save_accounts(accounts)
            print("Deposit successful.")
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            if accounts[username]['balance'] >= amount:
                accounts[username]['balance'] -= amount
                record_transaction(accounts[username], "Withdrawal", amount)
                save_accounts(accounts)
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        elif choice == '4':
            target = input("Enter recipient username: ").strip()
            amount = float(input("Enter amount to transfer: "))
            if target not in accounts:
                print("Target user does not exist.")
            elif accounts[username]['balance'] < amount:
                print("Insufficient funds.")
            else:
                accounts[username]['balance'] -= amount
                accounts[target]['balance'] += amount
                record_transaction(accounts[username], "Transfer", amount, target)
                record_transaction(accounts[target], "Received", amount, username)
                save_accounts(accounts)
                print("Transfer successful.")
        elif choice == '5':
            print("\nTransaction History:")
            for entry in accounts[username]['history']:
                print(entry)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

def main():
    accounts = load_accounts()
    while True:
        print("\n--- Welcome to the ATM System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            register(accounts)
        elif choice == '2':
            username = login(accounts)
            if username:
                atm_menu(username, accounts)
        elif choice == '3':
            print("Exiting system. Have a good day!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
