from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Emergency

class CreateUserSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ["email","first_name", "last_name", "user_type", "password"]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data["password"] = make_password(validated_data["password"])
        return super().update(instance, validated_data)

class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Emergency
        fields = "__all__"
        read_only_fields=["created_at","ref_number"]