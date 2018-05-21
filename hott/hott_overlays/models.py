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
