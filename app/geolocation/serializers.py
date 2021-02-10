from rest_framework import serializers

class GeoLocationSerializer(serializers.Serializer):
    ip = serializers.CharField()
    continent_name = serializers.CharField()
    country_code = serializers.CharField()