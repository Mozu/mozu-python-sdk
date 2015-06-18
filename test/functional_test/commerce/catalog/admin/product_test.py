import unittest
import logging;
from mozurestsdk import mozuclient;
from mozurestsdk.apicontext import ApiContext;
from mozurestsdk.commerce.catalog.admin.product import Product;

class Product_Test(unittest.TestCase):
	def setUp(self):
		logging.basicConfig(level=logging.DEBUG);
		client = mozuclient.configure(config="c:\projects\mozuconfig.txt");
		
	def test_getProduct(self):
		apiContext = ApiContext(catalogId=1,masterCatalogId=1);
		product = Product(apiContext);
		p = product.getProduct("test");
		self.assertIsNone(p);
			

if __name__ == '__main__':
    unittest.main()
