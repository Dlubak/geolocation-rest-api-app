from django.urls import path
from . import views

urlpatterns = [
    path(r'loc', views.TestView.as_view()),
]
