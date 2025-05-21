import json
from datetime import datetime

class Transaction:
    def __init__(self, trans_id, trans_type, amount, category, description, date):
        self.id = trans_id
        self.trans_type = trans_type
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.trans_type,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

class UserFinanceManager:
    def __init__(self, filename="finance_data.json"):
        self.filename = filename
        self.transactions = []
        self.load_transactions()

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.save_transactions()

    def list_transactions(self):
        if not self.transactions:
            print("No transactions available.")
        for t in self.transactions:
            print(f"{t.id}. {t.trans_type} - {t.amount} ({t.category}) - {t.description} on {t.date}")

    def summarize(self):
        income = sum(t.amount for t in self.transactions if t.trans_type.lower() == "income")
        expenses = sum(t.amount for t in self.transactions if t.trans_type.lower() == "expense")
        print(f"Total Income: {income}")
        print(f"Total Expenses: {expenses}")
        print(f"Balance: {income - expenses}")

    def update_transaction(self, trans_id):
        for t in self.transactions:
            if t.id == trans_id:
                print("Leave field empty to keep current value.")
                new_type = input(f"Type [{t.trans_type}]: ") or t.trans_type
                new_amount = input(f"Amount [{t.amount}]: ")
                new_amount = float(new_amount) if new_amount else t.amount
                new_category = input(f"Category [{t.category}]: ") or t.category
                new_description = input(f"Description [{t.description}]: ") or t.description
                new_date = input(f"Date [{t.date}]: ") or t.date

                t.trans_type = new_type
                t.amount = new_amount
                t.category = new_category
                t.description = new_description
                t.date = new_date
                self.save_transactions()
                print("Transaction updated.")
                return
        print("Transaction not found.")

    def delete_transaction(self, trans_id):
        self.transactions = [t for t in self.transactions if t.id != trans_id]
        self.save_transactions()
        print("Transaction deleted.")

    def save_transactions(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump([t.to_dict() for t in self.transactions], f, indent=4)
        except Exception as e:
            print(f"Error saving transactions: {e}")

    def load_transactions(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.transactions = [Transaction(**t) for t in data]
        except FileNotFoundError:
            self.transactions = []
        except Exception as e:
            print(f"Error loading transactions: {e}")
            self.transactions = []

def main():
    manager = UserFinanceManager()
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Transaction\n2. View Transactions\n3. Summarize\n4. Update Transaction")
        print("5. Delete Transaction\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                trans_id = len(manager.transactions) + 1
                trans_type = input("Type (Income/Expense): ").capitalize()
                amount = float(input("Amount: "))
                category = input("Category: ")
                description = input("Description: ")
                date = input("Date (YYYY-MM-DD): ")
                datetime.strptime(date, "%Y-%m-%d")  # Validate format
                t = Transaction(trans_id, trans_type, amount, category, description, date)
                manager.add_transaction(t)
            except Exception as e:
                print(f"Invalid input: {e}")

        elif choice == '2':
            manager.list_transactions()

        elif choice == '3':
            manager.summarize()

        elif choice == '4':
            try:
                trans_id = int(input("Enter transaction ID to update: "))
                manager.update_transaction(trans_id)
            except ValueError:
                print("Invalid ID.")

        elif choice == '5':
            try:
                trans_id = int(input("Enter transaction ID to delete: "))
                manager.delete_transaction(trans_id)
            except ValueError:
                print("Invalid ID.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
