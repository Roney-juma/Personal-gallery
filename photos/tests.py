from django.test import TestCase
from .models import Location,Image,Category


# Create your tests here.
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.roney= Category(name = 'Roney')

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.roney,Category))

        # Testing Save Method
    def test_save_method(self):
        self.roney.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)