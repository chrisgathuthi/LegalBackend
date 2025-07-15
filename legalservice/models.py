
from random import randint
import uuid
import time
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

def generate_ref_number():
    current_time = time.time()
    return int(current_time)
class User(AbstractUser):

    """User model"""
    class UserType(models.TextChoices):
        INTERNAL = "INT", _("Internal")
        INDIVIDUAL = "IND", _("Individual")
        ORGANISATION = "ORG", _("Organisation")

    username = None
    gid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    email = models.EmailField(verbose_name="E-mail",unique=True)
    verification_code = models.CharField(verbose_name="otp",max_length=6,unique=True)
    otp_created_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(verbose_name="verified",default=False)
    user_type= models.CharField(max_length=3, choices=UserType, default=UserType.INDIVIDUAL)
    is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name","user_type"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def otp_generator():
        return (str(randint(100000,999999)))
    
    def reset_otp_code(self):
        now = time.time()
        elapsed = now - self.otp_created_at.timestamp()
        if elapsed > 3600:
            self.verification_code = self.otp_generator()
            self.otp_created_at = now
            self.save()
        return self.verification_code

class OrganisationProfile(models.Model):
    """Common profile"""
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="organisation_profile")
    company_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    address = models.TextField()
    contact_email = models.EmailField()
    gid = models.UUIDField(default=uuid.uuid4(), unique=True, editable=False, db_index=True)


class IndividualProfile(models.Model):
    """Individual user profile name"""
    class IdentificationDocument(models.TextChoices):
        PASSPORT = "PASSPORT", _("Passport")
        NATIONALIDENTIFICATION = "NATIONALID", _("National ID")
        BIRTHCERTIFICATE = "BIRTHCERT", _("Birth Certificate")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='individual_profile')
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    identification_type = models.CharField(max_length=15, choices=IdentificationDocument)
    identification_number = models.CharField(max_length=15)
    gid = models.UUIDField(default=uuid.uuid4(), unique=True, editable=False, db_index=True)

class CaseTray(models.Model):
    """Tray to hold incoming cases"""
    created_at = models.DateTimeField(auto_now=True)
    acknowledged = models.BooleanField(default=False)
class FirmStaffProfile(models.Model):
    """staff profile"""
    gid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='legal_staff_profile')
    
class CaseCommon(models.Model):
    """Common attrubutes for all cases"""
    tray = models.ForeignKey(to=CaseTray,on_delete=models.CASCADE, related_name="inbox", null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    case_summary = models.TextField()
    is_closed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    gid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, db_index=True)
    ref_number = models.CharField(max_length=10, unique=True, default=generate_ref_number)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    owner = GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True
class Emergency(CaseCommon):
    class EmergencyType(models.TextChoices):
        EVICTION = "EVC", _("Eviction")
        ARREST = "ARR", _("Arrest")
        EXTORTION = "EXT", _("Extortion")

    emergency_type = models.CharField(max_length=3, choices=EmergencyType)

class DraftingAffidavit(CaseCommon):
    """Drafting affidavit"""
    pass

class DraftingAgreement(CaseCommon):
    """Drafting agreement"""
    pass

class FamilyMatter(CaseCommon):
    """Family matters"""
    pass

class LabourLaw(CaseCommon):
    """Labour laws"""
    pass

class LandMatter(CaseCommon):
    """Land matter"""
    pass

class LegalAdvice(CaseCommon):
    """Legal advice"""
    pass

class OtherMatter(CaseCommon):
    """Other matter"""
    pass