import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
        
    def test_default_product_weight(self):
        """Test default product weight being 20"""
        prod = Product('Another Product')
        self.assertEqual(prod.price, 20)
        
    def test_stealability(self):
        """Testing if stealability method returns correct statement"""
        expensive_product = Product(name='Expensive Product', price=30)
        self.assertEqual(expensive_product.stealability(), "Very stealable!")
        
    def test_explode(self):
        """Testing if explode method returns correct statement"""
        explosive_prod = Product(name='Explosive Product', flammability=100)
        self.assertEqual(explosive_prod.explode(), "...BABOOM!!")
        
class AcmeReportTests(unittest.TestCase):
    """Test report"""
    
    def test_default_num_products(self):
        """Testing that the number of products is 30"""
        self.assertEqual(len(generate_products()), 30)
        
    def test_legal_names(self):
        """Testing legal names"""
        pass
                         
                                            


if __name__ == '__main__':
    unittest.main()
