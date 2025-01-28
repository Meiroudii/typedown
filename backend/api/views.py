from django.shortcuts import render
from django.contrib.author.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permission import IsAuthenticated, AllowAny

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
