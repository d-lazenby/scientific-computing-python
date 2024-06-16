class Category:
    
    def __init__(self, category):
        self.ledger = []
        self.category = category
    
    def __str__(self):
        pass
        
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        
    def withdraw(self, amount, description=''):
        if amount > self.get_balance():
            print("Withdrawal amount greater than remaining balance")
            return False
        else:
            self.deposit(-amount, description)
            return True
        
    def get_balance(self):
        return sum(map(lambda tx: tx['amount'], self.ledger))
    
    def transfer(self, destination_category, amount):
        if type(destination_category) == type(self):
            self.withdraw(amount, description=f"Transfer to {destination_category.category}")
            destination_category.deposit(amount, description=f"Transfer from {self.category}")
        else:
            raise TypeError
            
            

testing = Category("Food")
testing2 = Category("Clothes")
print(testing.ledger, testing.get_balance())
testing.deposit(1000, 'tx1')
testing2.deposit(2000, 'tx1')
print(testing.ledger, testing2.ledger)
testing.transfer(testing2, 100)
print(testing.ledger, testing2.ledger)




