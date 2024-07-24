class Budget:

    def __init__(self, name=None, amount=0):
        self.name = name if name is not None else "Unnamed"
        self.amount = round(amount, 2)
    
    def __repr__(self):
        return f"Budget: {self.name}, Total: {self.amount}"