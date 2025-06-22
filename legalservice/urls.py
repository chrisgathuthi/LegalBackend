from django.urls import path
from legalservice import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("auth/user/",views.CreateUserView.as_view(), name="create-users"),
    path('auth/user/activate',views.ActivateUserView.as_view(),name="activate-user"),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('emergency/',views.EmergencyView.as_view(),name="emergencies")
]