from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateUserSerializer, CreateDraftingAffidavtiSerializer, CreateFamilyMatterSerializer, CreateDraftingAgreementSerializer, CreateLabourLawSerializer, CreateLandMatterSerializer, CreateLegalAdviceSerializer, CreateOtherMatterSerializer, CreateEmergencySerializer
from utilities.utils import otp_generator
from rest_framework.exceptions import APIException
from django.utils.datastructures import MultiValueDictKeyError
from utilities.exceptions import LegalServiceException
from .crud import activate_user_account, validate_otp_code, search_user_profile
import logging
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTTokenUserAuthentication

logger = logging.getLogger(__name__)
class CreateUserView(APIView):

    permission_classes = []
    authentication_classes = []


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

    """Activate user account"""

    authentication_classes = []

    def post(self, request, format=None):
        """
        Return user token
        """
        # send query params
        try:
            gid = request.query_params["token"]
        except MultiValueDictKeyError:
            raise LegalServiceException(code="invalid_request", detail="invalid request", status_code=status.HTTP_400_BAD_REQUEST)
        else:
            if gid is not None:
                validate_otp_code(gid, request.data)
                user_payload = activate_user_account(gid)
        return Response(data=user_payload)

class UserInformationView(APIView):
    """Fetch user information"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass
class EmergencyView(APIView):
    """Create emergency"""
   
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CreateEmergencySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_profile = search_user_profile(serializer.validated_data["user_id"],serializer.validated_data["user_type"])
            serializer.save(owner=user_profile)
            logger.info("Emergency service created") 
        return Response(data={"message":"Case submiitted successfully","status":"success","results":serializer.validated_data},status=status.HTTP_201_CREATED)
    
class DraftingAffidavitView(APIView):

    """Create draffting affidavit"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CreateDraftingAffidavtiSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_profile = search_user_profile(serializer.validated_data["user_id"],serializer.validated_data["user_type"])
            serializer.save(owner=user_profile)
            logger.info("Drafting affidavit service created") 
        return Response(data={"message":"Case submiitted successfully","status":"success","results":serializer.validated_data},status=status.HTTP_201_CREATED)


class DraftingAgreementView(APIView):

    """Create draffting affidavit"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CreateDraftingAgreementSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_profile = search_user_profile(serializer.validated_data["user_id"],serializer.validated_data["user_type"])
            serializer.save(owner=user_profile)
            logger.info("Drafting agreement service created") 
        return Response(data={"message":"Case submiitted successfully","status":"success","results":serializer.validated_data},status=status.HTTP_201_CREATED)


class FamilyMatterView(APIView):

    """Create draffting affidavit"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CreateFamilyMatterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_profile = search_user_profile(serializer.validated_data["user_id"],serializer.validated_data["user_type"])
            serializer.save(owner=user_profile)
            logger.info("Family service created") 
        return Response(data={"message":"Case submiitted successfully","status":"success","results":serializer.validated_data},status=status.HTTP_201_CREATED)


class LabourLawView(APIView):

    """Create labour laws"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CreateLabourLawSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_profile = search_user_profile(serializer.validated_data["user_id"],serializer.validated_data["user_type"])
            serializer.save(owner=user_profile)
            logger.info("Labour law service created") 
        return Response(data={"message":"Case submiitted successfully","status":"success","results":serializer.validated_data},status=status.HTTP_201_CREATED)

class LandMatterView(APIView):

    """Create draffting affidavit"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CreateLandMatterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_profile = search_user_profile(serializer.validated_data["user_id"],serializer.validated_data["user_type"])
            serializer.save(owner=user_profile)
            logger.info("Emergency service created") 
        return Response(data={"message":"Case submiitted successfully","status":"success","results":serializer.validated_data},status=status.HTTP_201_CREATED)


class LegalAdviceView(APIView):

    """Create draffting affidavit"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CreateLegalAdviceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_profile = search_user_profile(serializer.validated_data["user_id"],serializer.validated_data["user_type"])
            serializer.save(owner=user_profile)
            logger.info("Emergency service created") 
        return Response(data={"message":"Case submiitted successfully","status":"success","results":serializer.validated_data},status=status.HTTP_201_CREATED)


class OtherMatterView(APIView):

    """Create draffting affidavit"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CreateOtherMatterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_profile = search_user_profile(serializer.validated_data["user_id"],serializer.validated_data["user_type"])
            serializer.save(owner=user_profile)
            logger.info("Other matter service created") 
        return Response(data={"message":"Case submiitted successfully","status":"success","results":serializer.validated_data},status=status.HTTP_201_CREATED)


class OtherMatterView(APIView):

    """Create draffting affidavit"""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CreateOtherMatterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_profile = search_user_profile(serializer.validated_data["user_id"],serializer.validated_data["user_type"])
            serializer.save(owner=user_profile)
            logger.info("Other matter service created") 
        return Response(data={"message":"Case submiitted successfully","status":"success","results":serializer.validated_data},status=status.HTTP_201_CREATED)
