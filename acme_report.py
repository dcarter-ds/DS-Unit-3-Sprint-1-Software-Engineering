from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    rand_adj = []
    rand_noun = []

    for _ in range(1, num_products+1):
        rand_adj.append(random.choice(ADJECTIVES))

    for _ in range(1, num_products+1):
        rand_noun.append(random.choice(NOUNS))

    products = ["%s%02s" % t for t in zip(rand_adj, rand_noun)]

    return products


def inventory_report(products):
    prices = []
    weights = []
    flams = []

    unique_products = len(set(products))

    for i in range(0, 30):
        prices.append(Product(products[i]).price)

    average_price = sum(prices) / 30

    for i in range(0, 30):
        weights.append(Product(products[i]).weight)

    average_weights = sum(weights) / 30

    for i in range(0, 30):
        flams.append(Product(products[i]).flammability)

    average_flams = sum(flams) / 30


if __name__ == '__main__':
    inventory_report(generate_products())
