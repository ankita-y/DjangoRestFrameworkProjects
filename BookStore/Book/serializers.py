from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import Field
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'
    # name = serializers.CharField(max_length = 100)
    # author = serializers.CharField(max_length = 100)
    # published_on = serializers.DateField()

    # custom validation
    def validate(self,data):
        if data['name']:
            for i in data['name'].split():
                if i.isdigit():
                    raise serializers.ValidationError({'error':"Name should be in string format"})

        return data