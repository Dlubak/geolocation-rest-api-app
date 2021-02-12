from django.urls import path
from user import views

urlpatterns = [
    path(r'create', views.CreateUserView.as_view()),
]
