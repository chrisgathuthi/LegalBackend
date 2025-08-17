from django.urls import path
from legalservice import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path("auth/user/",views.CreateUserView.as_view(), name="create-users"),
    path('auth/user/activate',views.ActivateUserView.as_view(),name="activate-user"),
    path('auth/login/', views.LegalTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('emergency/',views.EmergencyView.as_view(),name="emergencies"),
    path("drafting-affidavits/",views.DraftingAffidavitView.as_view(),name="drafting-affidavits"),
    path("drafting-agreements/",views.DraftingAgreementView.as_view(),name="drafting-agreements"),
    path("family-matters/",views.FamilyMatterView.as_view(),name="family-matters"),
    path("labour-laws/",views.LabourLawView.as_view(),name="labour-laws"),
    path("legal-advice/",views.LegalAdviceView.as_view(),name="legal-advice"),
    path("land-matters/",views.LandMatterView.as_view(),name="land-matters"),
    path("other-matters/",views.OtherMatterView.as_view(),name="other-matters"),
    path("profiles/<str:gid>/me/",views.UserInformationView.as_view(),name="user-profile"),
    path("cases/",views.AdminInboxView.as_view(),name="admin-inbox")
]