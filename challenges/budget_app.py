class Category:
    
    def __init__(self):
        self.ledger = []
        
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

testing = Category()
print(testing.ledger, testing.get_balance())
testing.deposit(100, 'tx1')
print(testing.ledger, testing.get_balance())
testing.withdraw(50, 'tx2')
print(testing.ledger, testing.get_balance())
testing.withdraw(150, 'tx3')
print(testing.ledger, testing.get_balance())



