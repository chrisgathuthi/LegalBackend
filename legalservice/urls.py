from django.urls import path
from .apis import GoogleLoginApi, GoogleLoginRedirectApi
urlpatterns = [
    path('api/oauth2/callback/', GoogleLoginApi.as_view(),name="callbakc-sdk" ),
    path('api/oauth2/redirect/',GoogleLoginRedirectApi.as_view(),name="redirect-sdk")
]