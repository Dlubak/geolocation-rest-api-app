import requests
from core.models import GeoLocationData
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_ipv4_address
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import GeoLocationDataSerializer, IpAddressSerializer


class CreateGeoLocationView(generics.CreateAPIView):
    queryset = GeoLocationData.objects.all()
    serializer_class = IpAddressSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        ip_serializer = self.get_serializer(data=request.data)
        ip_serializer.is_valid(raise_exception=True)

        ip_address = request.data.get('ip', None)
        url = settings.IP_STACK_SETTINGS.get('API_URL')
        access_key = settings.IP_STACK_SETTINGS.get('API_ACCESS_KEY')

        request_url = f"{url}/{ip_address}?access_key={access_key}"
        request_response = requests.get(request_url)
        data = request_response.json()
        serializer = GeoLocationDataSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)


class RetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = GeoLocationData.objects.all()
    serializer_class = GeoLocationDataSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'ip'

    def get_object(self):
        ip_address = self.request.query_params.get('ip', None)
        try:
            validate_ipv4_address(ip_address)
        except ValidationError:
            raise Http404()
        obj = get_object_or_404(GeoLocationData, ip=ip_address)

        return obj


class ListGeoLocationView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = GeoLocationData.objects.all()
    serializer_class = GeoLocationDataSerializer
