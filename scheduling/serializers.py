from rest_framework import serializers

from .models.schedule_model import Schedule
from .models.location_model import Location


class ScheduleSerializer(serializers.ModelSerializer):
    """
        This class represents a serializer which designed for Schedule objects serialization/deserialization.
    """

    # def create(self, validated_data):
    #     user = CustomUser.objects.create_user(**validated_data)
    #     user.save()

    class Meta:
        model = Schedule
        fields = ['id', 'start_datetime', 'end_datetime', 'user', 'location']


class LocationSerializer(serializers.ModelSerializer):
    """
        This class represents a serializer which designed for Schedule objects serialization/deserialization.
    """

    # def create(self, validated_data):
    #     user = CustomUser.objects.create_user(**validated_data)
    #     user.save()

    class Meta:
        model = Location
        fields = ['id', 'name']