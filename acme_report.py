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


def inventory_report(products):
    for prod in products:
      return Products(prod)


if __name__ == '__main__':
    inventory_report(generate_products())
