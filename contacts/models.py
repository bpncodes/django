from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):

    listing_id = models.IntegerField()
    user_id = models.IntegerField(blank=True)
    listing = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name