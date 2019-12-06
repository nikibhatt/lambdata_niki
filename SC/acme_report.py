
#!/usr/bin/env python

from random import randint, sample, uniform, choice
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_prods=30):
    list = []
    num_prods = num_prods
    for x in range(1, num_prods+1):
        name = choice(ADJECTIVES) + ' ' + choice(NOUNS)
        price = randint(5, 101)
        weight = randint(5, 101)
        new_prod = Product(name, price=price, weight=weight)
        list.append(new_prod)
    return(list)


def inventory_report(list):
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Number of products: ', len(list))
    sum_price = 0
    for obj in list:
      sum_price += obj.price
      ave_price = sum_price/len(list)
    print('Average price: ', ave_price)
    sum_weight = 0
    for obj in list:
      sum_weight += obj.weight
      ave_weight = sum_weight/len(list)
    print('Average weight: ', ave_weight)
    sum_flammability = 0
    for obj in list:
      sum_flammability += obj.flammability
      ave_flammability = sum_flammability/len(list)
    print('Average flammability: ', ave_flammability)

if __name__ == '__main__':
    inventory_report(generate_products())
