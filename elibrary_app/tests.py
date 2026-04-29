from django.test import TestCase
from .models import Catalog

class CatalogModelsTest(TestCase):
    ''''Тест модели каталога'''

    def setUp(self):
        self.book = Catalog(
            title='First Django Book',
            ISBN='978-3-540-8915-6',
            author='Dany Kaliberda',
            price='9.99',
            availability=True
        )

    def test_create_book(self):
        self.aaertIsInstance(self.book, Catalog)

    def test_str_representation(self):
        self.assertEqual(str(self.book), 'First Django Book')

    def test_saving_and_retriving_book(self):

