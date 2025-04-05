# SEARCH
from django.contrib.auth import get_user_model
from rest_framework.exceptions import APIException

def activate_user_plan(token: str, otp_code: str):
    try:
        user = get_user_model().objects.filter(gid=token)
        return user
    except get_user_model().DoesNotExist:
        raise APIException(detail="No user found", code="no_user_found")

