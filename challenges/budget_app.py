class Category:
    
    def __init__(self, category_name):
        self.ledger = []
        self.category_name = category_name
    
    def __str__(self):
        lines = []
        line_length = 30
        half_line_length = line_length / 2
        len_category = len(self.category_name)
        stars_left = int((half_line_length - len_category / 2))
        if len_category % 2 == 0:
            stars_right = stars_left
        else:
            stars_right = stars_left + 1
        lines.append(stars_left * "*" + self.category_name + stars_right * "*")
        for i, item in enumerate(self.ledger):
            if i == 0:
                lines.append("deposit" + " " * 16 + f"{item['amount']:.2f}")
            else:
                num_padding = 7 - len(f"{item['amount']:.2f}")
                if (len_desc := len(item['description'])) > 23:
                    description = item['description'][:23]
                    description_padding = 0
                else:
                    description = item['description']
                    description_padding = 23 - len_desc
                padding = int(description_padding + num_padding) * " "
                lines.append(description + padding + f"{item['amount']:.2f}")
        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)
            
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.deposit(-amount, description)
            return True
        return False
        
    def get_balance(self):
        return sum(map(lambda tx: tx['amount'], self.ledger))
    
    def transfer(self, amount, destination_category):
        if self.check_funds(amount):
            destination_category.deposit(amount, description=f"Transfer from {self.category_name}")
            self.withdraw(amount, description=f"Transfer to {destination_category.category_name}")
            return True
        return False
        
    def check_funds(self, amount):
        if not (amount > self.get_balance()):
            return True
        return False

def create_spend_chart(categories):
    # Calculate percentage spend for each category
    withdrawals = []
    for category in categories:
        filtered_tx = filter(lambda c: c['amount'] < 0 and "Transfer" not in c["description"], category.ledger)
        category_withdrawals = sum(tx['amount'] for tx in filtered_tx)
        withdrawals.append(category_withdrawals)
        print(withdrawals)
    total_spend = sum(withdrawals)
    percentage_spend = [round((withdrawal / total_spend * 100) // 10) * 10 for withdrawal in withdrawals]
    
    # Draw chart
    num_cols = len(categories) * 3 + 1
    bar_chart = 'Percentage spent by category\n'
    for ylabel in range(100, -10, -10):
        bar_chart += str(ylabel).rjust(3) + '| '
        for percent in percentage_spend:
            if ylabel <= percent:
                bar_chart += 'o  '
            else:
                bar_chart += '   '
        bar_chart += '\n'
        
    bar_chart += '    ' + '-' * num_cols + '\n'

    category_names = [category.category_name for category in categories]
    longest_cat_name = max(len(name) for name in category_names)
    for i in range(longest_cat_name):
        bar_chart += '     '
        for category_name in category_names:
            if i < len(category_name):
                bar_chart += category_name[i] + '  '
            else:
                bar_chart += '   '
        if i == longest_cat_name - 1:
            break
        bar_chart += '\n'
    
    return bar_chart



food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)

clothing.deposit(2000, "deposit")
clothing.withdraw(20.20, "jumper")
clothing.withdraw(10.12, "jeans")

categories = [food, clothing]
print(create_spend_chart(categories))