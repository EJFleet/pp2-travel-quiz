class Budget:
    def__init__(self, name, amount):
        self.name = name
        self.amount = amount
    
    def__repr__(self):
        return f"Budget: {self.name}, Total: {self.amount}"