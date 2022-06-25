from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .serializers import SpecializationSerializer, SpecializationSerializerLink
from .models.specialization_model import Specialization

# Create your views here.

class SpecializationCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = SpecializationSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to create specializations.
    """
    queryset = Specialization.objects.all().order_by('name')
    serializer_class = SpecializationSerializerLink
    permission_classes = [IsAuthenticated]