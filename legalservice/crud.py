import uuid
from django.contrib.auth import get_user_model
from rest_framework.exceptions import APIException
from rest_framework_simplejwt.tokens import RefreshToken

def activate_user_account(token: str, otp_code: str)->dict[str, str]:
    """Activate the user and return token"""
    try:
        user = get_user_model().objects.get(gid=token)
    except get_user_model().DoesNotExist:
        raise APIException(detail="No user found", code="no_user_found")
    else:
        refresh = RefreshToken.for_user(user=user)
        return {
            "id":user.gid,
            "access_token": str(refresh),
            "refresh_token": str(refresh.access_token),
            "first_name": user.first_name,
            "last_name": user.last_name,
            "user_type": user.user_type
        }