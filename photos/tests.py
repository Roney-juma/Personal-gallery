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

class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(name = "Nairobi")
        self.location.save()
        self.category = Category (name = "The universe")
        self.category.save()
        self.img1 = Image(image_name = 'The moon', image_description = 'Blue in color', image_location = self.location, image_category = self.category, pub_date = '2020-10-07' )
        self.img1.save_image()
    
    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

        # Testing Instances
    def test_instance(self):
        self.assertTrue(isinstance(self.img1,Image))

        # Testing Save Method
    def test_save_method(self):
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
         
        # Testing Get-Pics Method
    def test_get_pics_today(self):
        today_pics = Image.todays_pics()
        self.assertTrue(len(today_pics) > 0)

        # Testing Delete Method
    def test_delete_method(self):
        self.img1.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

        # Testing Update Method
    def test_update_method(self):
        updated_rows = Image.update_image(self.img1.id, image_name = 'The sun')
        self.assertTrue(updated_rows == 1)

    def test_search_Image_category(self):
        pic = Image.search_by_category("The universe")
        self.assertTrue(pic.first().id == self.img1.id)
    
    def test_filter_Image_location(self):
        area = Image.search_by_location("Nairobi")
        self.assertTrue(area.first().id == self.img1.id)