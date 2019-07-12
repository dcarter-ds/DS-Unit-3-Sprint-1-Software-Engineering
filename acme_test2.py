import unittest
from acme import Product
from acme_report import generate_products, ADJ, NOUN

class AcmeProductTests(unittest.TestCase):
	"""Making sure Acme products are the tops!"""
	def test_default_product_price(self):
		"""Test default product price being 10"""
		prod = Product('Test Product')
		self.assertEqual(prod.price, 10)

	def test_default_product_weight(self):
		"""Test default weight price being 20"""
		prod = Product('Test Product')
		self.assertEqual(prod.weight, 20)

	def test_default_product_flam(self):
		"""Test default flammability being 0.5"""
		prod = Product('Test Product')
		self.assertEqual(prod.flammability, 0.5)

	def test_large_explode(self):
		"""Test response for high explode value"""
		prod = Product('Test Product', weight=100, flammability=100)
		self.assertEqual(prod.explode(), '...BABOOM!!')

	def test_low_stealability(self):
		"""Test response for low stealability value"""
		prod = Product('Test Product', price=1, weight=3)
		self.assertEqual(prod.stealability(), 'Not so stealable!')

class AcmeReportTests(unittest.TestCase):
	"""Making sure Acme Reporting is great!"""
	def test_default_num_products(self):
		"""Test default product number is 30"""
		self.assertEqual(len(generate_products()), 30)

	def test_legal_name(self):
		"""Test quality of product names"""
		products = generate_products()

		for product in products:
			adj = product.name.split()[0]
			noun = product.name.split()[1]

			self.assertIn(adj, ADJ)
			self.assertIn(noun, NOUN)





if __name__ == '__main__':
	unittest.main()
