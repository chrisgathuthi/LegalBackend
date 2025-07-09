from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import (
    User,
    Emergency,
    DraftingAffidavit,
    DraftingAgreement,
    FamilyMatter,
    LabourLaw,
    LandMatter,
    LegalAdvice,
    OtherMatter,
)
from django.contrib.auth import get_user_model
class CreateUserSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    user_type = serializers.CharField(required=True)
   
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "user_type",
            "password",
            "confirm_password"
        ]

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "password" in validated_data:
            validated_data["password"] = make_password(validated_data["password"])
        return super().update(instance, validated_data)

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("Password do not match")

        if len(attrs["password"]) < 8 or len(attrs["confirm_password"]) < 8:
            raise serializers.ValidationError("Password is too short minimum length 8")
        return super().validate(attrs)


class ActivateUserSerializer(serializers.Serializer):
    activation_code = serializers.CharField(required=True, label="activation code")

class UserInformationSerializer(serializers.ModelSerializer):
    """Fetch user information"""
    class Meta:
        model = User
        fields = "__all__"
        exclude = ["password"]

class CreateEmergencySerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(required=True)
    user_type = serializers.CharField(required=True)

    class Meta:
        model = Emergency
        fields = ["case_summary","user_id","user_type","emergency_type"]
    
    def validate_user_id(self, value):
        try:
            get_user_model().objects.get(gid=value)
            return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        
    def validate(self, attrs):
        user_type = attrs["user_type"]
        user_id = attrs["user_id"]

        user = get_user_model().objects.filter(gid=user_id,user_type=user_type).first()
        if user is None:
            raise serializers.ValidationError("User does not exists")
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop("user_id")
        validated_data.pop("user_type")
        return super().create(validated_data)
class CreateDraftingAffidavtiSerializer(serializers.ModelSerializer):
    """Drafting affidavit"""

    user_id = serializers.CharField(required=True)
    user_type = serializers.CharField(required=True)
    class Meta:
        model = DraftingAffidavit
        fields = ["case_summary","user_id","user_type"]

    def validate_user_id(self, value):
        try:
            get_user_model().objects.get(gid=value)
            return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        
    def validate(self, attrs):
        user_type = attrs["user_type"]
        user_id = attrs["user_id"]

        user = get_user_model().objects.filter(gid=user_id,user_type=user_type).first()
        if user is None:
            raise serializers.ValidationError("User does not exists")
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop("user_id")
        validated_data.pop("user_type")
        return super().create(validated_data)

class CreateDraftingAgreementSerializer(serializers.ModelSerializer):
    """Drafting agreement"""

    class Meta:
        model = DraftingAgreement
        fields = ["case_summary","user_id","user_type"]

    def validate_user_id(self, value):
        try:
            get_user_model().objects.get(gid=value)
            return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        
    def validate(self, attrs):
        user_type = attrs["user_type"]
        user_id = attrs["user_id"]

        user = get_user_model().objects.filter(gid=user_id,user_type=user_type).first()
        if user is None:
            raise serializers.ValidationError("User does not exists")
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop("user_id")
        validated_data.pop("user_type")
        return super().create(validated_data)
    
class CreateFamilyMatterSerializer(serializers.ModelSerializer):
    """Family matter"""

    class Meta:
        model = FamilyMatter
        fields = ["case_summary","user_id","user_type"]

    def validate_user_id(self, value):
        try:
            get_user_model().objects.get(gid=value)
            return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        
    def validate(self, attrs):
        user_type = attrs["user_type"]
        user_id = attrs["user_id"]

        user = get_user_model().objects.filter(gid=user_id,user_type=user_type).first()
        if user is None:
            raise serializers.ValidationError("User does not exists")
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop("user_id")
        validated_data.pop("user_type")
        return super().create(validated_data)
    
class CreateLabourLawSerializer(serializers.ModelSerializer):
    """labour law"""

    class Meta:
        model = LabourLaw
        fields = ["case_summary","user_id","user_type"]

    def validate_user_id(self, value):
        try:
            get_user_model().objects.get(gid=value)
            return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        
    def validate(self, attrs):
        user_type = attrs["user_type"]
        user_id = attrs["user_id"]

        user = get_user_model().objects.filter(gid=user_id,user_type=user_type).first()
        if user is None:
            raise serializers.ValidationError("User does not exists")
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop("user_id")
        validated_data.pop("user_type")
        return super().create(validated_data)

class CreateLandMatterSerializer(serializers.ModelSerializer):
    """land matter"""

    class Meta:
        model = LandMatter
        fields = ["case_summary","user_id","user_type"]

    def validate_user_id(self, value):
        try:
            get_user_model().objects.get(gid=value)
            return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        
    def validate(self, attrs):
        user_type = attrs["user_type"]
        user_id = attrs["user_id"]

        user = get_user_model().objects.filter(gid=user_id,user_type=user_type).first()
        if user is None:
            raise serializers.ValidationError("User does not exists")
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop("user_id")
        validated_data.pop("user_type")
        return super().create(validated_data)


class CreateLegalAdviceSerializer(serializers.ModelSerializer):
    """legal advice"""

    class Meta:
        model = LegalAdvice
        fields = ["case_summary","user_id","user_type"]
    def validate_user_id(self, value):
        try:
            get_user_model().objects.get(gid=value)
            return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        
    def validate(self, attrs):
        user_type = attrs["user_type"]
        user_id = attrs["user_id"]

        user = get_user_model().objects.filter(gid=user_id,user_type=user_type).first()
        if user is None:
            raise serializers.ValidationError("User does not exists")
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop("user_id")
        validated_data.pop("user_type")
        return super().create(validated_data)

class CreateOtherMatterSerializer(serializers.ModelSerializer):
    """Other matter"""

    class Meta:
        model = OtherMatter
        fields = ["case_summary","user_id","user_type"]
    def validate_user_id(self, value):
        try:
            get_user_model().objects.get(gid=value)
            return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        
    def validate(self, attrs):
        user_type = attrs["user_type"]
        user_id = attrs["user_id"]

        user = get_user_model().objects.filter(gid=user_id,user_type=user_type).first()
        if user is None:
            raise serializers.ValidationError("User does not exists")
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop("user_id")
        validated_data.pop("user_type")
        return super().create(validated_data)