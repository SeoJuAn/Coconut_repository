from django.db import models

# Create your models here.
class Community(models.Model):
    writer = models.CharField(max_length=200, default='')
    title = models.CharField(max_length=200, default='')
    content = models.CharField(max_length=200, default='')
    subdate = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.title