from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class ProductSerializer(ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model=Product
        fields='__all__'

class ProductListSerializer(ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model=Product
        fields='__all__'


