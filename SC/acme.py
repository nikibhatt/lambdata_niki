class Product:
    """
    Acme Corporation Product details
    """
    def __init__(self, name, price = 10, weight =20, flammability = 0.5):
        import random as rand
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = rand.randint(1000000,10000000)
