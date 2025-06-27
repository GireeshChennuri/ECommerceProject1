from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from user.serializers import *
from user.models import User
from . import services
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated

class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_permissions(self):
        if self.action in ['login', 'create']:
            return [AllowAny()]
        return [permission() for permission in self.permission_classes]
    
    @action(detail=False,methods=['POST'],url_path='login')
    def login(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            ser=services.Login()
            user,token=ser.check_login(serializer.validated_data)
            if user:
                return Response({'status': 'success','data':serializer.data,'token':token.key})
            else:
                return Response({
                    'status': 'Invalid credentials'
                }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=400)
  
    