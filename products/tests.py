from django.test import TestCase
from .views import all_products, product_item
from django.core.urlresolvers import resolve
from .models import Product

# Create your tests here.
class HomePageTest(TestCase):   
        
    def test_products_page_status_code_is_ok(self):
        page = self.client.get('/products/')
        self.assertEqual(page.status_code, 200)

    def test_products_page_resolves(self):
            page = resolve('/products/')
            self.assertEqual(page.func, all_products)
            
    def test_product_exists(self):
        product = Product(name="A Product", price=10)        
        product.save()
        page = self.client.get('/products/1')
        self.assertEqual(page.status_code, 200)

    def test_product_page_resolves(self):
            product = Product(name="Product_1", price=20)
            product.save()
            page = resolve('/products/1')
            self.assertEqual(page.func, product_item)

            
    def test_product_does_not_exist(self):
        page = self.client.get('/products/1')
        self.assertEqual(page.status_code, 404)
        
    