
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from legalservice.models import OrganisationProfile, IndividualProfile, FirmStaffProfile


User = get_user_model()
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == "IND":
            IndividualProfile.objects.create(user=instance)
        elif instance.user_type == "ORG":
            OrganisationProfile.objects.create(user=instance)
        else:
            FirmStaffProfile.objects.create(user=instance)

