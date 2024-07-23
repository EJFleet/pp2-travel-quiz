class Expense:
    def __init__(self, category, name, amount, budget_name):
        self.category = category
        self.name = name
        self.amount = amount
        self.budget_name = budget_name

    def __repr__(self):
        return f"Expense added: {self.name} for {self.amount:.2f} in {self.category} for {self.budget_name}"
