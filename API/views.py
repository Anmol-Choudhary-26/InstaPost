from django.shortcuts import render
from .models import Ipost, InstagramUser
from .serializers import PostSerializer, UserSerializer
from rest_framework import viewsets


class UserviewSet(viewsets.ModelViewSet):
    queryset=InstagramUser.objects.all()
    serializer_class=UserSerializer


class PostviewSet(viewsets.ModelViewSet):
    queryset=Ipost.objects.all()
    serializer_class=PostSerializer
