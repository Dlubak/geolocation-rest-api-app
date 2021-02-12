from django.contrib.auth.models import User
from user.serializers import UserSerializer
from rest_framework import generics


class CreateUserView(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer
