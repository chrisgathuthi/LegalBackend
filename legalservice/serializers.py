from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Emergency

class CreateUserSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ["email","first_name", "last_name", "user_type", "password","confirm_password"]

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data["password"] = make_password(validated_data["password"])
        return super().update(instance, validated_data)
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Password do not match")
        
        if len(attrs['password']) < 8 or  len(attrs['confirm_password']) < 8:
            raise serializers.ValidationError("Password is too short minimum length 8")
        return super().validate(attrs)
    
class ActivateUserSerializer(serializers.Serializer):
    activation_code = serializers.CharField(required=True, label='activation code')

class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Emergency
        fields = "__all__"
        read_only_fields=["created_at","ref_number"]