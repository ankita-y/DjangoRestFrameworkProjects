from django.contrib import admin
from .models import IcecreamFlavour
# Register your models here.
@admin.register(IcecreamFlavour)
class IcecreamDetails(admin.ModelAdmin):
    list_date = ['title','slug','scoop_remaining']
