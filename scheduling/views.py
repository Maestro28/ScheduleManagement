from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models.schedule_model import Schedule
from .serializers import ScheduleSerializer

# Create your views here.


class ScheduleCreateList(APIView):
    """
    List all users, or create a new User.
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