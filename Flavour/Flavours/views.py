from django.shortcuts import render
from .models import IcecreamFlavour
from .serializers import IcecreamSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

def Flavourlist(request):
    # complex datatype
    l = IcecreamFlavour.objects.get(id=1)
    serializer = IcecreamSerializer(l)
    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data,content_type = 'application/json')

