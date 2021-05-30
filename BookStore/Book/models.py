from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class Book(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    published_on = models.DateField()