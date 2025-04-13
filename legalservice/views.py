from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateUserSerializer, EmergencySerializer
from utilities.utils import otp_generator
from rest_framework.exceptions import APIException
from django.utils.datastructures import MultiValueDictKeyError
from utilities.exceptions import LegalServiceException
from .crud import activate_user_account
import logging
from rest_framework.permissions import IsAuthenticated

logger = logging.getLogger(__name__)
class CreateUserView(APIView):
    permission_classes = []

    def post(self, request, format=None):
        """
        Return user token
        """
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(verification_code= otp_generator())
            logger.info("A user has been created successfully")
        return Response(data={"message":"success today"})
    

class ActivateUserView(APIView):
    permission_classes = []

    """Activate user account"""
    def post(self, request, format=None):
        """
        Return user token
        """
        # send query params
        try:
            token = request.query_params["token"]
        except MultiValueDictKeyError:
            raise LegalServiceException(code="invalid_request", detail="invalid request", status_code=status.HTTP_400_BAD_REQUEST)
        else:
            if token is not None:
                token = activate_user_account(token, request.data)
        return Response(data=token)
    
class EmergencyView(APIView):
    """Create emergency"""
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        print(request.data)
        serializer = EmergencySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logger.info("Emergency service created")
        return Response(data={"message":"OK"},status=status.HTTP_201_CREATED)