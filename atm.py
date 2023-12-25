class ATM:
    def _init_(self, user_id, pin):
        if len(str(user_id)) == 4 and len(str(pin)) == 4:
            self.user_id = user_id
            self.pin = pin
            self.balance = 1000  # Initial balance for demonstration purposes
            self.transaction_history = []
        else:
            raise ValueError("User ID and PIN must be 4-digit numbers.")
    def display_menu(self):
        print("1. Transactions History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

    def show_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdraw: ${amount}")
            print(f"Withdrawal successful. Remaining balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: ${amount}")
            print(f"Deposit successful. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def transfer(self, amount, recipient_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Transfer to {recipient_account}: ${amount}")
            print(f"Transfer successful. Remaining balance: ${self.balance}")
        else:
            print("Invalid transfer amount or insufficient balance.")
user_id = input("Enter User ID (4 digits): ")
pin = input("Enter PIN (4 digits): ")

try:
    atm = ATM(int(user_id), int(pin))
except ValueError as e:
    print(e)

while True:
    atm.display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        atm.show_transaction_history()
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: $"))
        atm.withdraw(amount)
    elif choice == "3":
        amount = float(input("Enter deposit amount: $"))
        atm.deposit(amount)
    elif choice == "4":
        amount = float(input("Enter transfer amount: $"))
        recipient_account = input("Enter recipient's account: ")
        atm.transfer(amount, recipient_account)
    elif choice == "5":
        print("Exiting ATM. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
