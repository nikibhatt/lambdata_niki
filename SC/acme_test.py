#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS, inventory_report


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

    def test_functions(self):
        """Test explode and stealability methods"""
        prod = Product('A Cool Toy')
        self.assertEqual(prod.stealability(), 'Kinda stealable')
        self.assertEqual(prod.explode(), '...boom!')


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme Reports are accurate!"""

    def test_default_num_products(self):
        """Test default generate_product produces 30 products"""
        len_list = len(generate_products())
        self.assertEqual(len_list, 30)

if __name__ == '__main__':
    unittest.main()
