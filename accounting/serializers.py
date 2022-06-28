from rest_framework import serializers
from .models.specialization_model import Specialization
from .models.user_model import CustomUser
from scheduling.models.appointment_model import Appointment
from scheduling.models.schedule_model import Schedule


class UserSerializer(serializers.ModelSerializer):

    appointments = serializers.PrimaryKeyRelatedField(many=True, queryset=Appointment.objects.all())
    all_appointments = serializers.PrimaryKeyRelatedField(many=True, queryset=Appointment.objects.all())
    schedules = serializers.PrimaryKeyRelatedField(many=True, queryset=Schedule.objects.all())

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'password', 'specs', 'role',
                  'appointments', 'all_appointments', 'schedules']


class SpecializationSerializer(serializers.ModelSerializer):

    users = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all())

    class Meta:
        model = Specialization
        fields = ['name', 'users']




