
from django.test import TestCase



from products.views import all_products
from django.core.urlresolvers import resolve
 
class HomePageTest(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, all_products)
        
    def test_home_page_status_code_is_ok(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)