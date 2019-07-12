from acme import Product
import random

ADJ = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUN = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(n=30):

	return [Product(name=random.choice(ADJ) +  ' ' + random.choice(NOUN),
					price=random.randint(5, 100), weight=random.randint(5, 100),
					flammability=random.uniform(0.0, 2.5)) for _ in range(n)]


def inventory_report(products):
	unique_prods = len(set([prod.name for prod in products]))
	avg_price = sum([prod.price for prod in products]) / len(products)
	avg_weight = sum([prod.weight for prod in products]) / len(products)
	avg_flam = sum([prod.flammability for prod in products]) / len(products)

	print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
	print('Unique Products: ', unique_prods)
	print('Average Price: ', avg_price)
	print('Average Weight: ', avg_weight)
	print('Average Flammability: ', avg_flam)

if __name__ == '__main__':
	inventory_report(generate_products())






	 