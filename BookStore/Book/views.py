from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from .models import Book
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.views import APIView
# Create your views here.

# Creating using APIView
class BooksAPI(APIView):
    def get(self, request):
        bookquery = Book.objects.all()
        serializer = BookSerializer(bookquery, many = True)
        return Response({'status' : 200, 'payload' : serializer.data})

    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':201, 'payload':serializer.data,'message': 'Data created successfully'})
        return Response(serializer.errors, status=502)

    def delete(self,request):
        try:
            book_obj = Book.objects.get(id = id)
            book_obj.delete()
            
            return Response({'status':200, 'message': 'Data deleted successfully'})
            
        except Exception as e:
            return Response({'status':403,'message':'invalid id'})

    def put(Self,request):
        try:
            book_obj = Book.objects.get(id = id)
            serializer = BookSerializer(book_obj,data = request.data)
            if serializer.is_valid():   
                serializer.save()
                return Response({'status':201, 'payload':serializer.data,'message': 'Data updated successfully'})
            return Response(serializer.errors, status=502)
        except Exception as e:
            return Response({'status':403,'message':'invalid id'})
    



# Using @api_view decorators
# @api_view(['GET'])
# def bookQuery(request):
#     bookquery = Book.objects.all()
#     serializer = BookSerializer(bookquery, many = True)

#     return Response({'status' : 200, 'payload' : serializer.data})

# @api_view(['POST'])
# def bookcreate(request):
    
#     serializer = BookSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'status':201, 'payload':serializer.data,'message': 'Data created successfully'})
#     return Response(serializer.errors, status=502)


# @api_view(['PUT']) 
# def updateBook(request,id):
#     try:
#         book_obj = Book.objects.get(id = id)
#         serializer = BookSerializer(book_obj,data = request.data)
#         if serializer.is_valid():   
#             serializer.save()
#             return Response({'status':201, 'payload':serializer.data,'message': 'Data updated successfully'})
#         return Response(serializer.errors, status=502)
#     except Exception as e:
#         return Response({'status':403,'message':'invalid id'})

# @api_view(['DELETE']) 
# def deletebook(request,id):
#     try:
#         book_obj = Book.objects.get(id = id)
#         book_obj.delete()
        
#         return Response({'status':200, 'message': 'Data deleted successfully'})
        
#     except Exception as e:
#         return Response({'status':403,'message':'invalid id'})

# 'books/'
# def books_api(request):
#     books_query = Book.objects.all()
#     books_list = list(books_query.values())
#     response = JsonResponse(
#         books_list,
#         safe = False,
#         status = 200
#     )
#     return response

# 'book/create/'
# def book_create_api(request):
#     book_obj = Book.objects.create(
#         name = request.POST.get('name'),
#         author = request.POST.get('author'),
#         published_on = request.POST.get('published_on'),
#     )
#     book_dirt = model_to_dict(book_obj)
#     response = JsonResponse(book_dirt,
#     safe = False,
#     status = 201)
#     return response