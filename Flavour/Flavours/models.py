from django.db import models

# Create your models here.
class IcecreamFlavour(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    scoop_remaining = models.IntegerField(default=0)