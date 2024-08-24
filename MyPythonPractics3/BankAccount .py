class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
account.withdraw(50)
print("Balance:", account.get_balance())


#BankAccount Class with Encapsulation
