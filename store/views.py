from django.shortcuts import render
from products.models import Category, Product
# Create your views here.
from rest_framework import viewsets
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products. models import *
from .serializers import ProductSerializer

class ProductsByCategoryView(APIView):
    def get(self, request, slug):
        try:
            category = Category.objects.get(slug=slug)
            products = Product.objects.filter(category=category)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({'detail': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)
