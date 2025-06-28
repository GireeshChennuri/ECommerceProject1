from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from products.serializers import ProductSerializer

class OrderItemSerializer(ModelSerializer):
    item_subtotal = serializers.ReadOnlyField()
    class Meta:
        model=OrderItem
        fields='__all__'

class OrderSerializer(ModelSerializer):
    items=OrderItemSerializer(many=True)

    class Meta:
        model=Order
        fields='__all__'