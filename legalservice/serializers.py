from rest_framework import serializers
from .models import User

class CreateUserSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ["email","first_name", "last_name", "user_type", "password"]