from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny, IsAdminUser


from django.http import Http404

from accounting.models.user_model import CustomUser
from accounting.permissions import IsAdmOrIsOwnerOrReadOnly, SpecialistsOnlyPermission, SpecialistOrAdminPermission

from .models.schedule_model import Schedule
from .models.location_model import Location
from .models.procedure_model import Procedure
from .models.appointment_model import Appointment

from .serializers import ScheduleSerializer, LocationSerializer, ProcedureSerializer, AppointmentSerializer, \
    SpecialistFreeTimeSerializer, FreeSpecialistsSerializer, CustomersListSerializer

# Create your views here.


class ScheduleCreateList(APIView):
    """
    List all schedules, or create a new Schedule.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        schedule = Schedule.objects.all()
        serializer = ScheduleSerializer(schedule, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.user.role == 2:
            request.data['user'] = request.user.id
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScheduleDetail(APIView):
    """
    Retrieve, update or delete a Specialization instance.
    """
    permission_classes = [IsAdmOrIsOwnerOrReadOnly]

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
    permission_classes = [SpecialistOrAdminPermission]
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
    permission_classes = [IsAdmOrIsOwnerOrReadOnly]

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
    permission_classes = [SpecialistOrAdminPermission]
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
    Retrieve, update or delete a Procedure instance.
    """
    permission_classes = [IsAdmOrIsOwnerOrReadOnly]

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


class AppointmentCreateList(APIView):
    """
    List all locations, or create a new Appointment.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        appointment = Appointment.objects.all()
        serializer = AppointmentSerializer(appointment, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.user.role == 2:
            request.data['specialist'] = request.user.id
        elif request.user.role == 0:
            request.data['customer'] = request.user.id
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentDetail(APIView):
    """
    Retrieve, update or delete a Procedure instance.
    """
    permission_classes = [IsAdmOrIsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        appointment = self.get_object(pk)
        serializer_context = {
            'request': request,
        }
        serializer = AppointmentSerializer(appointment, context=serializer_context)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        appointment = self.get_object(pk)
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        appointment = self.get_object(pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpecialistFreeTimeGET(APIView):
    """
    Show specialist free time intervals in direct day.
    :param id dspecialist identifier
    :param daytime direct day
    example: http://127.0.0.1:8000/api/v1/scheduling/spec_free_time/?daytime=2022-07-06&id=45
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        if 'daytime' not in request.GET:
            return Response({'Empty input error': 'U need to add "daytime" param'}, status=status.HTTP_400_BAD_REQUEST)
        data = dict(id=request.GET.get('id'), daytime=request.GET.get('daytime'), intervals=[])
        serializer = SpecialistFreeTimeSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FreeSpecialists(APIView):
    """
    Show free specialist in direct datetime.
    :param id procedure identifier
    :param datetime direct date and time
    example: http://127.0.0.1:8000/api/v1/scheduling/free_specs/?id=1&datetime=06-07-2022 11:10
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        if 'datetime' not in request.GET:
            return Response({'Empty input error': "U need to add 'datetime' param"}, status=status.HTTP_400_BAD_REQUEST)
        data = dict(id=request.GET.get('id'), datetime=request.GET.get('datetime'), specialists=[])
        serializer = FreeSpecialistsSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListCustomers(APIView):
    """
    Show list customers in direct day for authorized specialist.
    example: http://127.0.0.1:8000/api/v1/scheduling/free_specs/?id=1&datetime=06-07-2022 11:10
    """
    permission_classes = [SpecialistOrAdminPermission]

    def get(self, request, format=None):
        if 'daytime' not in request.GET:
            return Response({'Empty input error': 'U need to add "daytime" param'}, status=status.HTTP_400_BAD_REQUEST)
        data = dict(id=request.user.id, daytime=request.GET.get('daytime'), customers=[])
        serializer = CustomersListSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)