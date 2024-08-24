class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your balance is: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")
        else:
            print("Insufficient balance")

atm = ATM()
while True:
    action = input("Enter action (balance, deposit, withdraw, exit): ").lower()
    if action == 'balance':
        atm.check_balance()
    elif action == 'deposit':
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)
    elif action == 'withdraw':
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)
    elif action == 'exit':
        break
    else:
        print("Invalid action")


# SimpleATMSimulator