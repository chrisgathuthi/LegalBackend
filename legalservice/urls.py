from django.urls import path
from .apis import GoogleLoginApi, GoogleLoginRedirectApi
from legalservice import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('oauth2/callback/', GoogleLoginApi.as_view(),name="callbakc-sdk" ),
    path('oauth2/redirect/',GoogleLoginRedirectApi.as_view(),name="redirect-sdk"),
    path("auth/user/",views.CreateUserView.as_view(), name="create-users"),
    path('auth/user/activate',views.ActivateUserView.as_view(),name="activate-user"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('emergency/',views.EmergencyView.as_view(),name="emergencies")
]