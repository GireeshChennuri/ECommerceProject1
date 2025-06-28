from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny

class OrderAdminViewSet(ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes=[AllowAny]
class OrderViewSet(ModelViewSet):
   serializer_class=OrderSerializer
   permission_classes=[AllowAny]

   def get_queryset(self):
      if self.request.user:
        user=self.request.user
        return Order.objects.filter(user=user)
      return None
  
    
