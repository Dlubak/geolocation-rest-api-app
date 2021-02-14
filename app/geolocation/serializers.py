from rest_framework import serializers
from core.models import GeoLocationData


class GeoLocationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoLocationData
        fields = '__all__'
    

class IpAddressSerializer(serializers.Serializer):
    ip = serializers.IPAddressField()
