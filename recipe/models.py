from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=10)
    
    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=50) 

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=60)
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='recipe/', blank= True, null=True)
    ingredients = models.TextField(max_length=200)
    instructions = models.TextField(max_length=1000)
    categories = models.ManyToManyField('Category', verbose_name=("categories"))

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"pk": self.pk})
    
    
