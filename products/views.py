from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny,IsAdminUser

class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[AllowAny]

    def get_serializer_class(self):
        if self.action in ['list','retrieve']:
            return ProductListSerializer  
        return ProductSerializer
    
    def get_permissions(self):
        if self.action in ['list','retrieve']:
            return [permission() for permission in self.permission_classes]
        return [IsAdminUser()]
    
        

class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[AllowAny]

    def get_serializer_class(self):
        if self.action in ['list','retrieve']:
            return ProductListSerializer 
        return ProductSerializer
    
    def get_permissions(self):
        if self.action in ['list','retrieve']:
           return [permission() for permission in self.permission_classes] 
        return [IsAdminUser()]


