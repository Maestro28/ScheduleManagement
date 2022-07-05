from datetime import timedelta

from django.utils import timezone

from rest_framework import serializers

from .models.schedule_model import Schedule
from .models.location_model import Location
from .models.procedure_model import Procedure
from .models.appointment_model import Appointment


class ScheduleSerializer(serializers.ModelSerializer):
    """
        This class represents a serializer which designed for Schedule objects serialization/deserialization.
    """
    start_datetime = serializers.DateTimeField(
        required=True, allow_null=True,
        format="%d-%m-%Y %H:%M",
        input_formats=["%Y-%m-%d %H:%M", "%d-%m-%Y %H:%M"]
    )

    end_datetime = serializers.DateTimeField(
        required=True, allow_null=True,
        format="%d-%m-%Y %H:%M",
        input_formats=["%Y-%m-%d %H:%M", "%d-%m-%Y %H:%M"]
    )

    def validate(self, data):
        if data['start_datetime'] > data['end_datetime']:
            raise serializers.ValidationError("finish must occur after start")

        if data['start_datetime'] < timezone.now():
            raise serializers.ValidationError("It is already too late")

        schedules_by_users = Schedule.objects.filter(user=data['user'])
        for schedule in schedules_by_users:
            if schedule.start_datetime < data['start_datetime'] < schedule.end_datetime or \
                    schedule.start_datetime < data['start_datetime'] < schedule.end_datetime:
                raise serializers.ValidationError("That specialist already beasy in that time")

        schedules_by_locations = Schedule.objects.filter(location=data['location'])
        for schedule in schedules_by_locations:
            if schedule.start_datetime < data['start_datetime'] < schedule.end_datetime or \
                    schedule.start_datetime < data['start_datetime'] < schedule.end_datetime:
                raise serializers.ValidationError("This location is already in use at this time")

        return data

    class Meta:
        model = Schedule
        fields = ['id', 'start_datetime', 'end_datetime', 'user', 'location']


class LocationSerializer(serializers.ModelSerializer):
    """
        This class represents a serializer which designed for Location objects serialization/deserialization.
    """

    class Meta:
        model = Location
        fields = ['id', 'name']


class ProcedureSerializer(serializers.ModelSerializer):
    """
        This class represents a serializer which designed for Procedure objects serialization/deserialization.
    """
    duration = serializers.DurationField(max_value=timedelta(hours=5),
                                         min_value=timedelta(minutes=30),
                                         )

    class Meta:
        model = Procedure
        fields = ['id', 'name', 'duration', 'spec']


class AppointmentSerializer(serializers.ModelSerializer):
    """
        This class represents a serializer which designed for Appointment objects serialization/deserialization.
    """
    start_datetime = serializers.DateTimeField(
        required=True, allow_null=True,
        format="%d-%m-%Y %H:%M",
        input_formats=["%Y-%m-%d %H:%M", "%d-%m-%Y %H:%M"]
    )

    def validate(self, data):

        if data['start_datetime'] < timezone.now():
            raise serializers.ValidationError("It is already too late")

        # it should be really good validation here

        return data


    class Meta:
        model = Appointment
        fields = ['id', 'name', 'customer', 'specialist', 'procedure', 'start_datetime']