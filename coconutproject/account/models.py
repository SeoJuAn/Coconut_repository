from django.db import models

# Create your models here.
class Customer(models.Model):
    user_id = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    point = models.IntegerField()
    count = models.IntegerField()
    user_name = models.CharField(max_length=200)
    def __str__(self):
        return self.user_id

class StoreOwner(models.Model):
    user_id = models.CharField(max_length=200)

class ProductCompany(models.Model):
    user_id = models.CharField(max_length=200)
        