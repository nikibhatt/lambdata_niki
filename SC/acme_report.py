
#!/usr/bin/env python

from random import randint, sample, uniform, choice
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_prods = 30):
    list = []
    num_prods = num_prods
    for x in range(1, num_prods+1):
        name = choice(ADJECTIVES) + ' ' + choice(NOUNS)
        price = randint(5,101)
        weight = randint(5,101)
        new_prod = Product(name, price = price, weight = weight)
        list.append(new_prod)
    return(list)

def inventory_report(list):
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Number of products', len(list))
    #print('Average price of the products', sum(list)/len(list))

if __name__ == '__main__':
    inventory_report(generate_products())
