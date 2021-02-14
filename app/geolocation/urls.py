from django.urls import path
from geolocation import views


app_name = 'geolocation'
urlpatterns = [
    path(r'create', views.CreateGeoLocationView.as_view(), name="create"),
    path(r'list', views.ListGeoLocationView.as_view(), name="list"),
    path(r'retrieve', views.RetrieveDestroyAPIView.as_view(), name="retrieve"),
]
