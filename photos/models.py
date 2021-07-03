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