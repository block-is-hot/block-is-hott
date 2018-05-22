"""DB models for the different overlays."""

from django.db import models


class Crimes(models.Model):
    """This is the model used to store the crime location data."""

    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.CharField(max_length=180, default='DEFAULT')

    def __str__(self):
        """Show a string representation of the crime."""
        return 'Crime of {} at {} and {}'.format(
            self.description, self.latitude, self.longitude)


class Entertainment(models.Model):
    """This is a model used to store the cultural space."""

    location = models.CharField(max_length=40, null=True)
    description = models.CharField(
        max_length=180, default='DEFAULT', null=True)

    def __str__(self):
        """Show a string representation of the entertainment."""
        return 'Cultural space of {} at {}'.format(
            self.description, self.location)
