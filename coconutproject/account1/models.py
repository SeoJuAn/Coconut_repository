from django.db import models

# Create your models here.
class Customer(models.Model):
    user_id = models.CharField(max_length=200, default='')
    password = models.CharField(max_length=200, default='')
    email = models.EmailField(max_length=200, default='')
    point = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    nickname = models.CharField(max_length=200, default='')
    user_name = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')
    phonenumber = models.CharField(max_length=200, default='')
    subdate = models.CharField(max_length=200, default='')
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=200, default='')
    coupon = models.IntegerField(default=0)
    photo = models.CharField(max_length=200, default='')
    sns = models.CharField(max_length=200, default='')
    likestore = models.CharField(max_length=200, default='')
    likecommunity = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.user_id

class StoreOwner(models.Model):
    user_id = models.CharField(max_length=200, default='')
    password = models.CharField(max_length=200, default='')
    email = models.EmailField(max_length=200, default='')
    point = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    nickname = models.CharField(max_length=200, default='')
    user_name = models.CharField(max_length=200, default='')
    phonenumber = models.CharField(max_length=200, default='')
    subdate = models.CharField(max_length=200, default='')
    sns = models.CharField(max_length=200, default='')
    likecommunity = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.user_id
    
class ProductCompany(models.Model):
    user_id = models.CharField(max_length=200, default='')
    password = models.CharField(max_length=200, default='')
    email = models.EmailField(max_length=200, default='')
    phonenumber = models.CharField(max_length=200, default='')
    accountnumber = models.CharField(max_length=200, default='')
    companyname = models.CharField(max_length=200, default='')
    productcategory = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')
    operationtime = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.user_id
        