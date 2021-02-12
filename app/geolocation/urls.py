from django.urls import path
from geolocation import views

urlpatterns = [
    path(r'loc', views.IPStackGeoLocationView.as_view()),
    path(r'create', views.CreateGeoLocationView.as_view()),
    path(r'manage', views.RetrieveDestroyAPIView.as_view()),
]
