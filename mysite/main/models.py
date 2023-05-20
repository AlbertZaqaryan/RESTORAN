from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField('Category name', max_length=60)

    def __str__(self):
        return self.name
    
class Product_Type(models.Model):
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_type')
    name = models.CharField('Category name', max_length=60)

    def __str__(self):
        return f'{self.id}, {self.name}'