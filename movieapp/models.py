from django.db import models

# Create your models here.
#three types of models here 1. movies (release), 2. upcoming 3. registrations 

class Movies(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics',default='default.jpg')
    date = models.DateField()
    durations = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    language  =models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    cast = models.TextField()
    trailer = models.CharField(max_length=150)
    up = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.name
    
    
class Movies2(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics',default='default.jpg')
    date = models.DateField()
    durations = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    language  =models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    cast = models.TextField()
    trailer = models.CharField(max_length=150)
    up = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    
    
class Registration(models.Model):
    email = models.EmailField(max_length=250)
    name = models.CharField(max_length=150)
    mobile = models.IntegerField()
    age = models.IntegerField()
    seats = models.IntegerField()
    