from rest_framework import serializers

class IcecreamSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    slug = serializers.SlugField(max_length=100)
    scoop_remaining = serializers.IntegerField(default=0)