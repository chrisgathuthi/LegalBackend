from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateUserSerializer
from utilities.utils import otp_generator
from rest_framework.exceptions import APIException
from django.utils.datastructures import MultiValueDictKeyError
from utilities.exceptions import LegalServiceException
class CreateUserView(APIView):

    def post(self, request, format=None):
        """
        Return user token
        """
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(verification_code= otp_generator())
        return Response(data={"message":"success today"})
    

class ActivateUserView(APIView):

    """Activate user account"""
    def post(self, request, format=None):
        """
        Return user token
        """
        # send query params
        try:
            token = request.query_params["token"]
        except MultiValueDictKeyError:
            raise LegalServiceException(code="invalid_request", detail="invalid request", status_code=400)
        else:
            if token is not None:
                print(token)
                print(request.data)
        return Response(data={'message':"Hello world"})