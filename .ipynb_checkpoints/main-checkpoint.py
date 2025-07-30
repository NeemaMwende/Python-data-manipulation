class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self.transactions.append(f"Deposited: KES {amount}")
        print(f"Deposited KES {amount}. New Balance: KES {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        self.transactions.append(f"Withdrew: KES {amount}")
        print(f"Withdrew KES {amount}. New Balance: KES {self.balance}")

    def check_balance(self):
        print(f"Current Balance: KES {self.balance}")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
            return
        print("\nTransaction History:")
        for t in self.transactions:
            print("-", t)

# App Runner
def run_bank_app():
    print("Welcome to Python Bank 💰")
    name = input("Enter your name: ")
    account = BankAccount(name)

    while True:
        print("\nWhat would you like to do?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            account.show_transactions()
        elif choice == "5":
            print(f"Thank you, {account.owner}. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1–5.")

if __name__ == "__main__":
    run_bank_app()
