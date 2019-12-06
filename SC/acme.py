class Product:
    """
    Acme Corporation Product details
    """

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        import random as rand
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = rand.randint(1000000, 10000000)

    def stealability(self):
        """ Check the stealability based on the price divided by the weight"""
        ratio = self.price/self.weight
        if ratio < 0.5:
            message = 'Not so stealable...'
        elif ratio >= 0.5 and ratio < 1.0:
            message = 'Kinda stealable'
        else:
            message = 'Very stealable!'
        return message

    def explode(self):
        """ Check the explosiveness based on the flammability and weight"""
        prod = self.flammability * self.weight
        if prod < 10:
            message = '...fizzle'
        elif prod >= 10 and prod < 50:
            message = '...boom!'
        else:
            message = '...BABOOM!!'
        return message


class BoxingGlove(Product):
    """ BoxingGlove Product details"""

    def __init__(self, name, weight=10):
        self.name = name
        super(BoxingGlove, self).__init__(self.name)
        self.weight = weight

    def explode(self):
        """BoxingGlove explosiveness"""
        return('...its a glove.')

    def punch(self):
        if self.weight < 5:
            message = 'That tickles'
        elif self.weight >= 5 and self.weight < 15:
            message = 'Hey that hurt!'
        else:
            message = 'OUCH!'
        return message
