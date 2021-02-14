from django.db import models
from django.db.models import JSONField


class GeoLocationData(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    continent_name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)
    region_code = models.CharField(max_length=255)
    region_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    latitude = models.FloatField(max_length=255)
    longitude = models.FloatField(max_length=255)
    location = JSONField()
