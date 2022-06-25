from django.shortcuts import render
from rest_framework import generics
from .serializers import SpecializationSerializer

# Create your views here.

class SpecializationCreateView(generics.CreateAPIView):
    serializer_class = SpecializationSerializer