#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_identifier(self):
        """Test identifier is within the range given"""
        prod = Product('Test Product')        
        self.assertGreaterEqual(prod.identifier, 1000000)
        self.assertLessEqual(prod.identifier, 9999999)


if __name__ == '__main__':
    unittest.main()
