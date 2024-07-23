class Budget:

    def __init__(self, name, amount):
        self.name = name
        self.amount = round(amount, 2)
    
    def __repr__(self):
        return f"Budget: {self.name}, Total: {self.amount}"