from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class ActiveHottProfileManager(models.Manager):
    """Custom manager for only active profiles."""

    def get_queryset(self):
        """Limit the queryset to only profiles with active users."""
        all_profiles = super(ActiveHottProfileManager, self).get_queryset()
        return all_profiles.filter(user__is_active=True)


class HottProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    latitude = models.FloatField(null=True)
    longitutde = models.FloatField(null=True)

    @property
    def is_active(self):
        """Whether the User of the profile is active or not."""
        return self.user.is_active

    objects = models.Manager()
    active = ActiveHottProfileManager()

    def __str__(self):
        return self.user.username


@receiver(models.signals.post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        Token.objects.create(user=kwargs['instance'])
        profile = HottProfile(user=kwargs['instance'])
        profile.save()
