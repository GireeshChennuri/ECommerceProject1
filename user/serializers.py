from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User



class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        extra_kwargs = {
            'username': {'required': False},
            'password': {'required': False, 'write_only': True},
            'phone_number': {'required': False},
        }
    
    #to make username,password,phone number required only for creation 
    def validate(self, attrs):
        if self.instance is None:
            required_fields = ['username', 'password', 'phone_number']
            missing_fields = [field for field in required_fields if not attrs.get(field)]
            if missing_fields:
                raise serializers.ValidationError({
                    field: 'This field is required.' for field in missing_fields
                })
        return attrs
       
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  
        user.save()
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)