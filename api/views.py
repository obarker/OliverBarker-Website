from django.shortcuts import render
from .models import Users
from rest_framework import generics, status
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class UserView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
