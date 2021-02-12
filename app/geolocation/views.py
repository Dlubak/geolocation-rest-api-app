import json
import requests
from core.models import GeoLocation
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status, views
from rest_framework.response import Response
from .serializers import GeoLocationSerializer

# 37.8.230.235
class IPStackGeoLocationView(views.APIView):

    def call_api(self, request, *args, **kwargs):
        ip_address = request.GET.get('ip', None)
        if not ip_address:
            return Response(data=None, 
                            status=status.HTTP_400_BAD_REQUEST)

        url = settings.IP_STACK_SETTINGS.get('API_URL')
        access_key = settings.IP_STACK_SETTINGS.get('API_ACCESS_KEY')

        request_url = f"{url}/{ip_address}?access_key={access_key}"
        response_data = requests.get(request_url).json()
        return Response(data=response_data)

    def get(self, request, *args, **kwargs):
        return self.call_api(request, *args, **kwargs)


class CreateGeoLocationView(generics.CreateAPIView):
    queryset = GeoLocation.objects.all()
    serializer_class = GeoLocationSerializer


class RetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = GeoLocation.objects.all()
    serializer_class = GeoLocationSerializer
    lookup_field = 'ip'

    def get_object(self):
        ip_address = self.request.query_params.get('ip', None)
        print(ip_address, flush=True)
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(GeoLocation, ip=ip_address)

        return obj
