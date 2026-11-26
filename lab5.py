class BankAccount:
    def __init__(self, id, owner_name, balance=0):
        self.id = id
        self.owner_name = owner_name
        self.balance = balance

    def __del(self):
        print("Balance", self.id, "deleted")

    def get_balance(self):
        return self.balance

    def deposit(self, amount):  
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("problem")
        else:
            s
            elf.balance -= amount

    def showAccount(self):
        print("ID:", self.id, "| Owner:", self.owner_name, "|  Balancee:", self.balance)


class Bank:
    def __init__(self):
        self.accounts = []

    def __del__(self):
        print("Bank closed")

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, id):
        for acc in self.accounts:
            if acc.id == id:
                self.accounts.remove(acc)
                return

    def sort_by_balance(self):
        self.accounts.sort(key=lambda acc: acc.balance)

    def show_all(self):
        for acc in self.accounts:
            acc.showAccount()


def main():
    bank = Bank()
    bank.add_account(BankAccount(6324, "Ostap", 500))
    bank.add_account(BankAccount(7656, "Andriy", 100))
    bank.add_account(BankAccount(4355, "Oleh", 300))

    print("All balance:")
    bank.show_all()

    bank.accounts[0].deposit(200)      
    bank.accounts[1].deposit(50.5)     
    bank.accounts[2].withdraw(1000)    
    print("\nAfter:")
    bank.show_all()

    bank.sort_by_balance()
hhj
    print("\nDelete account 2:")
    bank.remove_account(2)
    bank.show_all()
    bank_new = Bank()132213333wZZ


main()
