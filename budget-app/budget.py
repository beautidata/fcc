class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0.00

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=''):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": (amount * -1), "description": description})
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name

    def get_ledger(self):
        return self.ledger

    def transfer(self, amount, category):
        if category.check_funds(amount) is True:
            self.deposit(amount, f"Transfer from {category.get_name()}")
        return category.withdraw(amount, f"Transfer to {self.get_name()}")

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False

    def __str__(self):
        mystring = ""
        star_num = int((30 - len(self.get_name())) // 2)
        for n in range(star_num):
            mystring += "*"
            mystring += self.get_name()
        while len(mystring) < 30:
            mystring += "*"
        mystring += "\n"
        for x in range(len(self.get_ledger())):
            mystring += self.ledger[x]['description']
            mystring += " "
            mystring += str(self.ledger[x]['amount'])
            mystring += "\n"
        mystring += f"Total: {self.get_balance()}"
        return mystring



def create_spend_chart(categories):
    print('spend chart created.')