class ATM:

    def __init__(self, user_name, balance = 0):
        self.user_name = user_name
        self.balance = balance

    def get_balance(self):
        print(self.balance)


    def deposit(self, money):
        self.balance += money

        with open("transactions.txt", "a") as f:
            f.write(f"Successfully deposited {money} azn. The balance is {self.balance} azn.\n")



    def withdraw(self, amount):
        
        if amount <= self.balance:
            self.balance -= amount        
        else:
            print("You do not have sufficient amount to withdraw!")
        
        self.get_balance()
        
        with open("transactions.txt", "a") as f:
            f.write(f"Successfully wihdrawed {amount} azn. The balance is {self.balance} azn.\n")

    def transactions(self):
        
        with open("transactions.txt", "r") as f:
            for line in f.readlines():
                print(line)



abb = ATM('samirrasul')
abb.deposit(121)
abb.deposit(12)
abb.withdraw(120)
abb.deposit(123)
print(abb.balance)
abb.transactions()
