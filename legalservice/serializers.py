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
            "confirm_password",
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


class OrgProfileSerializer(serializers.ModelSerializer):
    """Fetch user information"""

    company_name = serializers.CharField(source="organisationprofile.company_name")
    phone_number = serializers.CharField(source="organisationprofile.phone_number")
    address = serializers.CharField(source="organisationprofile.address")
    contact_email = serializers.CharField(source="organisationprofile.contact_email")

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "user_type",
            "is_verified",
            "company_name",
            "phone_number",
            "address",
            "contact_email",
            "is_active",
        ]

class IndividualProfileSerializer(serializers.ModelSerializer):
    """Fetch user information"""

    identification_type = serializers.CharField(source="organisationprofile.identification_type")
    phone_number = serializers.CharField(source="organisationprofile.phone_number")
    address = serializers.CharField(source="organisationprofile.address")
    identification_number = serializers.CharField(source="organisationprofile.identification_number")

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "user_type",
            "is_verified",
            "identification_type",
            "phone_number",
            "address",
            "identification_number",
            "is_active",
        ]

class FirmProfileSerializer(serializers.ModelSerializer):
    """Fetch user information"""
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "user_type",
            "is_verified",
            "is_active",
        ]
class CreateEmergencySerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(required=True)
    user_type = serializers.CharField(required=True)

    class Meta:
        model = Emergency
        fields = ["case_summary", "user_id", "user_type", "emergency_type"]

    def validate_user_id(self, value):
        try:
            get_user_model().objects.get(gid=value)
            return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("User does not exist")

    def validate(self, attrs):
        user_type = attrs["user_type"]
        user_id = attrs["user_id"]

        user = get_user_model().objects.filter(gid=user_id, user_type=user_type).first()
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
        fields = ["case_summary", "user_id", "user_type"]

    def validate_user_id(self, value):
        try:
            get_user_model().objects.get(gid=value)
            return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("User does not exist")

    def validate(self, attrs):
        user_type = attrs["user_type"]
        user_id = attrs["user_id"]

        user = get_user_model().objects.filter(gid=user_id, user_type=user_type).first()
        if user is None:
            raise serializers.ValidationError("User does not exists")
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("user_id")
        validated_data.pop("user_type")
        return super().create(validated_data)


class CreateDraftingAgreementSerializer(serializers.ModelSerializer):
    """Drafting agreement"""

    user_id = serializers.CharField(required=True)
    user_type = serializers.CharField(required=True)

    class Meta:
        model = DraftingAgreement
        fields = ["case_summary", "user_id", "user_type"]

    def validate_user_id(self, value):
        try:
            get_user_model().objects.get(gid=value)
            return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("User does not exist")

    def validate(self, attrs):
        user_type = attrs["user_type"]
        user_id = attrs["user_id"]

        user = get_user_model().objects.filter(gid=user_id, user_type=user_type).first()
        if user is None:
            raise serializers.ValidationError("User does not exists")
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("user_id")
        validated_data.pop("user_type")
        return super().create(validated_data)


class CreateFamilyMatterSerializer(serializers.ModelSerializer):
    """Family matter"""

    user_id = serializers.CharField(required=True)
    user_type = serializers.CharField(required=True)

    class Meta:
        model = FamilyMatter
        fields = ["case_summary", "user_id", "user_type"]

    def validate_user_id(self, value):
        try:
            get_user_model().objects.get(gid=value)
            return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("User does not exist")

    def validate(self, attrs):
        user_type = attrs["user_type"]
        user_id = attrs["user_id"]

        user = get_user_model().objects.filter(gid=user_id, user_type=user_type).first()
        if user is None:
            raise serializers.ValidationError("User does not exists")
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("user_id")
        validated_data.pop("user_type")
        return super().create(validated_data)


class CreateLabourLawSerializer(serializers.ModelSerializer):
    """labour law"""

    user_id = serializers.CharField(required=True)
    user_type = serializers.CharField(required=True)

    class Meta:
        model = LabourLaw
        fields = ["case_summary", "user_id", "user_type"]

    def validate_user_id(self, value):
        try:
            get_user_model().objects.get(gid=value)
            return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("User does not exist")

    def validate(self, attrs):
        user_type = attrs["user_type"]
        user_id = attrs["user_id"]

        user = get_user_model().objects.filter(gid=user_id, user_type=user_type).first()
        if user is None:
            raise serializers.ValidationError("User does not exists")
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("user_id")
        validated_data.pop("user_type")
        return super().create(validated_data)


class CreateLandMatterSerializer(serializers.ModelSerializer):
    """land matter"""

    user_id = serializers.CharField(required=True)
    user_type = serializers.CharField(required=True)

    class Meta:
        model = LandMatter
        fields = ["case_summary", "user_id", "user_type"]

    def validate_user_id(self, value):
        try:
            get_user_model().objects.get(gid=value)
            return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("User does not exist")

    def validate(self, attrs):
        user_type = attrs["user_type"]
        user_id = attrs["user_id"]

        user = get_user_model().objects.filter(gid=user_id, user_type=user_type).first()
        if user is None:
            raise serializers.ValidationError("User does not exists")
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("user_id")
        validated_data.pop("user_type")
        return super().create(validated_data)


class CreateLegalAdviceSerializer(serializers.ModelSerializer):
    """legal advice"""

    user_id = serializers.CharField(required=True)
    user_type = serializers.CharField(required=True)

    class Meta:
        model = LegalAdvice
        fields = ["case_summary", "user_id", "user_type"]

    def validate_user_id(self, value):
        try:
            get_user_model().objects.get(gid=value)
            return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("User does not exist")

    def validate(self, attrs):
        user_type = attrs["user_type"]
        user_id = attrs["user_id"]

        user = get_user_model().objects.filter(gid=user_id, user_type=user_type).first()
        if user is None:
            raise serializers.ValidationError("User does not exists")
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("user_id")
        validated_data.pop("user_type")
        return super().create(validated_data)


class CreateOtherMatterSerializer(serializers.ModelSerializer):
    """Other matter"""

    user_id = serializers.CharField(required=True)
    user_type = serializers.CharField(required=True)

    class Meta:
        model = OtherMatter
        fields = ["case_summary", "user_id", "user_type"]

    def validate_user_id(self, value):
        try:
            get_user_model().objects.get(gid=value)
            return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("User does not exist")

    def validate(self, attrs):
        user_type = attrs["user_type"]
        user_id = attrs["user_id"]

        user = get_user_model().objects.filter(gid=user_id, user_type=user_type).first()
        if user is None:
            raise serializers.ValidationError("User does not exists")
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("user_id")
        validated_data.pop("user_type")
        return super().create(validated_data)
