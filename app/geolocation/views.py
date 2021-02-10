import json

import requests
from django.conf import settings
from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from .serializers import GeoLocationSerializer

# Create your views here.
class TestView(views.APIView):
    
    def call_api(self, request, *args, **kwargs):
        method_map = {
            'get': requests.get
        }
        method = request.method.lower()
        url = settings.IP_STACK_SETTINGS.get('API_URL')
        access_key = settings.IP_STACK_SETTINGS.get('API_ACCESS_KEY')
        ip_address = request.GET.get('ip', None)
        # 37.8.230.235
        request_url = f"{url}/{ip_address}?access_key={access_key}"
        response_data = requests.get(request_url)
        print(response_data.json(), flush=True)
        serializer = GeoLocationSerializer(data=response_data.json())
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(data=None)
        # serialized_data = GeoLocationSerializer(data=response_data)
        # print(serialized_data.initial_data, flush=True)
        # return Response(data=serialized_data.initial_data)
        # serialized_data = serializers.GeoLocationSerializer(data=data)
        # serialized_data.is_valid(True)
        # return Response(serialized_data.data)

    def get(self, request, *args, **kwargs):
        return self.call_api(request, *args, **kwargs)