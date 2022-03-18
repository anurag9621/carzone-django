from ctypes import create_unicode_buffer
from datetime import datetime

from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    message = models.TextField( blank=True , max_length=100)
    user_id = models.IntegerField(blank=True)
    create_date=models.DateTimeField(blank=True,default=datetime.now)


    def __str__(self):
        return self.email
