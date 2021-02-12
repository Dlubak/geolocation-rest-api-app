from rest_framework import serializers
from core.models import GeoLocation


class GeoLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoLocation
        fields = '__all__'