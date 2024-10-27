class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited. New balance: ${self.balance:.2f}")
        else:
            print("Please enter a valid amount to deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            print("Please enter a valid amount to withdraw.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")


def main():
    # Create a bank account instance
    account_number = input("Enter your account number: ")
    account = BankAccount(account_number)

    while True:
        print("\nOptions:")
        print("a) Deposit money")
        print("b) Withdraw money")
        print("c) Check balance")
        print("d) Exit")
        
        choice = input("Choose an option (a/b/c/d): ").strip().lower()

        if choice == 'a':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 'b':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 'c':
            account.check_balance()
        elif choice == 'd':
            print("Thank you for using our banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()