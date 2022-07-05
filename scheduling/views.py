from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models.schedule_model import Schedule
from .models.location_model import Location
from .models.procedure_model import Procedure
from .models.appointment_model import Appointment

from .serializers import ScheduleSerializer, LocationSerializer, ProcedureSerializer

# Create your views here.


class ScheduleCreateList(APIView):
    """
    List all schedules, or create a new Schedule.
    """
    # permission_classes = [AllowAny]
    def get(self, request, format=None):
        schedule = Schedule.objects.all()
        serializer = ScheduleSerializer(schedule, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScheduleDetail(APIView):
    """
    Retrieve, update or delete a Specialization instance.
    """
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Schedule.objects.get(pk=pk)
        except Schedule.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        schedule = self.get_object(pk)
        serializer_context = {
            'request': request,
        }
        serializer = ScheduleSerializer(schedule, context=serializer_context)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        schedule = self.get_object(pk)
        serializer = ScheduleSerializer(schedule, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        schedule = self.get_object(pk)
        schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LocationCreateList(APIView):
    """
    List all locations, or create a new Location.
    """
    # permission_classes = [AllowAny]
    def get(self, request, format=None):
        location = Location.objects.all()
        serializer = LocationSerializer(location, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationDetail(APIView):
    """
    Retrieve, update or delete a Location instance.
    """
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer_context = {
            'request': request,
        }
        serializer = LocationSerializer(location, context=serializer_context)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_object(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProcedureCreateList(APIView):
    """
    List all locations, or create a new Procedure.
    """
    # permission_classes = [AllowAny]
    def get(self, request, format=None):
        procedure = Procedure.objects.all()
        serializer = ProcedureSerializer(procedure, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProcedureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProcedureDetail(APIView):
    """
    Retrieve, update or delete a Location instance.
    """
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Procedure.objects.get(pk=pk)
        except Procedure.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        procedure = self.get_object(pk)
        serializer_context = {
            'request': request,
        }
        serializer = ProcedureSerializer(procedure, context=serializer_context)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        procedure = self.get_object(pk)
        serializer = ProcedureSerializer(procedure, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        procedure = self.get_object(pk)
        procedure.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)