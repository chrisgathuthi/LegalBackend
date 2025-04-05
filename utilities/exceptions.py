# utils.py
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException

class ApplicationError(Exception):
    def __init__(self, message, extra=None):
        super().__init__(message)

        self.message = message
        self.extra = extra or {}


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler to get the standard error response
    response = exception_handler(exc, context)

    # Customize the response data
    if response is not None:
        response.data['status_code'] = response.status_code
        response.data['error_message'] = str(exc)  # or customize with exc.detail if it's available

    # Handle any unhandled exceptions (e.g., 500 Internal Server Error)
    else:
        return Response(
            {
                "error_message": "An unexpected error occurred.",
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return response


class LegalServiceException(APIException):
    status_code = 400
    default_detail = "Oops! error occurred."
    default_code = "error"

    def __init__(self, detail=None, code=None, status_code=None):
        if detail is not None:
            self.detail = {"error_message":detail}
        if status_code is not None:
            self.status_code = status_code
        if code is not None:
            self.detail["error_code"] = code
        else:
            self.detail["error_code"] = self.default_code

        super().__init__(detail, code)
