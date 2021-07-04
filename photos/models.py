from django.db import models
import datetime as dt

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()


class Location (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()


class Image (models.Model):
    image = models.ImageField(upload_to = 'articles/', null=True)
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =200)
    image_location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    image_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


    @classmethod
    def update_image(cls, image_id, **kwargs):
        rows = 0
        if kwargs is not None:
            rows = cls.objects.filter(id = image_id).update(**kwargs)

        return rows

    
    class Meta:
        ordering = ['image_name']   

    