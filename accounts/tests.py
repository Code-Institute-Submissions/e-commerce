from django.test import TestCase
from .views import login, logout, register, profile
from django.core.urlresolvers import resolve

# Create your tests here.
class HomePageTest(TestCase):   
        
    def test_products_page_status_code_is_ok(self):
        page = self.client.get('/accounts/login/')
        self.assertEqual(page.status_code, 200)

    def test_products_page_resolves(self):
            page = resolve('/accounts/login/')
            self.assertEqual(page.func, login)
            
    def test_products_page_status_code_is_fine(self):
        page = self.client.get('/accounts/logout/')
        self.assertEqual(page.status_code, 302)

    def test_products_page_resolves_1(self):
            page = resolve('/accounts/logout/')
            self.assertEqual(page.func, logout)
            
        
    def test_products_page_status_code_is_alright(self):
        page = self.client.get('/accounts/register/')
        self.assertEqual(page.status_code, 200)

    def test_products_page_resolves_2(self):
            page = resolve('/accounts/register/')
            self.assertEqual(page.func, register)
            
    def test_products_page_status_code_is_(self):
        page = self.client.get('/accounts/profile/')
        self.assertEqual(page.status_code, 200)

    def test_products_page_resolves_3(self):
            page = resolve('/accounts/profile/')
            self.assertEqual(page.func, profile)
    