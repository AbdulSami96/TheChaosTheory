from distutils.command.upload import upload
from django.db import models

# Create your models here.
class contactdetails(models.Model):
    Name = models.CharField("Name",max_length=100)
    PhoneNumber = models.CharField("Phone Number",max_length=100)
    Email = models.EmailField("Email",max_length=100)
    Message = models.TextField("Message",max_length=100)
    def __str__(self):
        return self.Name

class Product(models.Model):
    name = models.CharField('name',max_length=120)
    price = models.CharField('price',max_length=120)
    ingredients = models.TextField('ingredients',max_length=300)
    def __str__(self):
        return self.name
    

class productinfo(models.Model):
    image = models.ImageField('image', null=True ,blank=True ,upload_to="pictures/images")
    name = models.CharField('name',max_length=120)
    description = models.TextField('description',max_length=2000)
    def __str__(self):
        return self.name

class review(models.Model):
    name = models.CharField('name',max_length=120)
    review = models.TextField('review',max_length=500)
    def __str__(self):
        return self.name


    

    

