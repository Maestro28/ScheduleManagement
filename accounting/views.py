from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .serializers import UserSerializer, SpecializationSerializer
from .models.specialization_model import Specialization
from .models.user_model import CustomUser

# Create your views here.


class UserCreateList(APIView):
    """
    List all users, or create a new User.
    """
    def get(self, request, format=None):
        user = CustomUser.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete a User instance.
    """
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpecializationCreateList(APIView):
    """
    List all specializations, or create a new Specialization.
    """
    def get(self, request, format=None):
        spec = Specialization.objects.all()
        serializer = SpecializationSerializer(spec, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpecializationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecializationDetail(APIView):
    """
    Retrieve, update or delete a Specialization instance.
    """
    def get_object(self, pk):
        try:
            return Specialization.objects.get(pk=pk)
        except Specialization.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        spec = self.get_object(pk)
        serializer = SpecializationSerializer(spec)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        spec = self.get_object(pk)
        serializer = SpecializationSerializer(spec, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        spec = self.get_object(pk)
        spec.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


