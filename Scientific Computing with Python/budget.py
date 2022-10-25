class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.leftover = 0
    def __str__(self):
        l = ''
        for dict in self.ledger:
            amount = "{:.2f}".format(dict["amount"])
            desc = dict["description"]
            if len(desc) > 23:
                desc = desc[:23]
            space = 30
            l += desc + ' '*(space-len(desc)-len(str(amount))) + str(amount) + '\n'
        return f'{self.category}'.center(30, '*') + '\n' + l + f'Total: {self.get_balance()}'

    def deposit(self, amount, desc=''):
        self.leftover += amount
        self.ledger.append({"amount": amount, "description": desc})
    def withdraw(self, amount, desc=''):
        if self.check_funds(amount):
            self.leftover -= amount
            self.ledger.append({"amount": -amount, "description": desc})
            return True
        return False
    def get_balance(self):
        return self.leftover
    def transfer(self, amount, budget):
        if self.leftover < amount:
            return False
        else:
            self.withdraw(amount, f"Transfer to {budget.category}")
            budget.deposit(amount, f"Transfer from {self.category}")
            return True
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

def create_spend_chart(categories):
    category_l = []
    cat_spent = []
    percentage = []
    for cat in categories:
        category_l.append(cat.category)
        spent = 0
        for info in cat.ledger:
            if info['amount'] < 0:
                spent += abs(info['amount'])
        cat_spent.append(spent)
    for i in range(len(category_l)):
        percentage.append(int(((cat_spent[i] / sum(cat_spent))*100) // 10*10))

    # header
    chart = "Percentage spent by category" + '\n'
    # body
    for p in range(100,-1,-10):
        space = 3
        chart += ' '*(space-len(str(p))) + str(p) + '|'
        for perc in percentage:
            if perc >= p:
                chart += ' o '
            else:
                chart += '   '
        chart += ' \n'
    # footer
    chart += '    ' + '-'*((3*len(category_l))+1)

    # get longest category
    longest = len(category_l[0])
    for cat in category_l:
        if len(cat) > longest:
            longest = len(cat)
    for c in range(len(category_l)):
        if len(category_l[c]) < longest:
            category_l[c] += ' '*(longest-len(category_l[c]))
    for loop in range(longest):
        chart += '\n    '
        for cat in category_l:
            chart += ' ' + cat[loop] + ' '
        chart += ' '
    
    return chart