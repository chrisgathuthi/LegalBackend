import uuid
from django.contrib.auth import get_user_model
from rest_framework.exceptions import APIException
from rest_framework_simplejwt.tokens import RefreshToken
import time
from .models import CaseTray, FirmStaffProfile, OrganisationProfile, IndividualProfile
from . import serializers

def validate_otp_code(gid: str, otp_code: int):
    """validate otp code """

    try:
        user = get_user_model().objects.get(gid=gid)
    except get_user_model().DoesNotExist:
        raise APIException(detail="No user found", code="no_user_found")
    else:
        time_now = time.time()
        elapsed_time = time_now - user.otp_created_at.timestamp()
        if elapsed_time > 3600:
            user.reset_otp_code()
            raise APIException(detail="OTP code expired", code="expired_otp_code")
        if user.verification_code != otp_code:
            user.reset_otp_code()
            raise APIException(detail="Invalid OTP code", otp_code="otp_code")
        # activate verify user
        user.is_verified = True
        user.save()        
        

def activate_user_account(gid: str)->dict[str, str]:
    """Activate the user and return token"""
    try:
        user = get_user_model().objects.get(gid=gid)
    except get_user_model().DoesNotExist:
        raise APIException(detail="No user found", code="no_user_found")
    else:
        refresh = RefreshToken.for_user(user=user)
        return {
            "Gid":user.gid,
            "AccessToken": str(refresh.access_token),
            "RefreshToken": str(refresh),
            "FirstName": user.first_name,
            "LastName": user.last_name,
            "UserType": user.user_type
        }


def search_user_profile(user_id:str, user_type:str):
    """search user profile"""
    
    user = get_user_model().objects.get(gid=user_id)
    if user_type == "ORG":
        return OrganisationProfile.objects.get(user=user)
    elif user_type == "IND":
        return IndividualProfile.objects.get(user=user)
    elif user_type == "INT":
        return FirmStaffProfile.objects.get(user=user)
    

def get_admin_inbox():
    tray =  CaseTray.objects.get(name="inbox")
    emergency = tray.emergency_set.all()
    affidavit = tray.draftingaffidavit_set.all()
    agreement = tray.draftingagreement_set.all()
    family = tray.familymatter_set.all()
    labour = tray.labourlaw_set.all()
    land = tray.landmatter_set.all()
    legal = tray.legaladvice_set.all()
    other = tray.othermatter_set.all()
    emergencies = serializers.EmergencyReadSerializer(emergency,many=True)
    affidavits = serializers.DraftingAffidavitReadSerializer(affidavit, many=True)
    families = serializers.FamilyMatterReadSerializer(family,many=True)
    agreements = serializers.DraftingAgreementReadSerializer(agreement, many=True)
    labours = serializers.LabourLawReadSerializer(labour,many=True)
    lands = serializers.LandLawReadSerializer(land,many=True)
    legals = serializers.LegalAdviceReadSerializer(legal, many=True)
    others = serializers.OtherMatterReadSerializer(other, many=True)
    return {
        "Emergency":emergencies.data,
        "DraftingAffidavit":affidavits.data,
        "DraftingAgreement":agreements.data,
        "FamilyMatters":families.data,
        "LabourLaws":labours.data,
        "LandMatters":lands.data,
        "LegalAdvice":legals.data,
        "OtherMatters":others.data
    }