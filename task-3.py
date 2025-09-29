class Menu:
    def __init__(self):
        self.options = [
            "Open a new account",
            "Deposit money",
            "Withdraw money",
            "Add interest",
            "Show balance",
            "Delete account",
            "Quit"
        ]

    def get_input(self):
        print("\n--- Bank Menu ---")
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")
        try:
            return int(input("Choose (1-7): "))
        except ValueError:
            return 0


class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} NOK added.")
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} NOK withdrawn.")
        else:
            print("Not enough balance.")

    def add_interest(self, rate=0.02):
        self.balance += self.balance * rate
        print("Interest added.")

    def show_balance(self):
        print(f"{self.name}'s balance: {self.balance:.2f} NOK")


def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: That is not a number. Try again.")


def main():
    menu = Menu()
    account = None

    while True:
        choice = menu.get_input()

        if choice == 1:
            if account:
                print("Account exists. Delete it first.")
            else:
                name = input("Enter account name: ")
                account = BankAccount(name)
                print("\n🏦✨ Welcome to ⭐ GLOBAL NoSteal BANK ⭐, the best bank on Earth!")
                print(f"🎉 Hello {name}! Your account is now ready to make money! 💸\n")

        elif choice in [2, 3, 4, 5, 6] and not account:
            print("No account. Create one first.")
            continue

        elif choice == 2:
            amount = get_valid_number("Deposit amount: ")
            account.deposit(amount)

        elif choice == 3:
            amount = get_valid_number("Withdraw amount: ")
            account.withdraw(amount)

        elif choice == 4:
            account.add_interest()

        elif choice == 5:
            account.show_balance()

        elif choice == 6:
            confirm = input("Delete account? (yes/no): ").lower()
            if confirm == "yes":
                account = None
                print("Account deleted.")

        elif choice == 7:
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
