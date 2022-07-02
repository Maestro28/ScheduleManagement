from rest_framework import serializers
from django.contrib.auth.models import User

from .models.specialization_model import Specialization
from .models.user_model import CustomUser
from scheduling.models.appointment_model import Appointment
from scheduling.models.schedule_model import Schedule


class UserSerializer(serializers.ModelSerializer):
    """
        This class represents a serializer which designed for Users objects serialization/deserialization.
    """
    # appointments = serializers.PrimaryKeyRelatedField(many=True, queryset=Appointment.objects.all())
    # all_appointments = serializers.PrimaryKeyRelatedField(many=True, queryset=Appointment.objects.all())
    # schedules = serializers.PrimaryKeyRelatedField(many=True, queryset=Schedule.objects.all())
    specs = serializers.SlugRelatedField(many=True,  # U should comment than field to work with id instead names
                                         queryset=Specialization.objects.all(),
                                         slug_field='name',
                                         allow_null=True,
                                         required=False,
                                         read_only=False
                                         )

    def create(self, validated_data):
        print(f'validated data==============={validated_data}')
        user = CustomUser.objects.create_user(**validated_data)
        user.save()

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'password', 'specs', 'role']
        extra_kwargs = {'password': {'write_only': True}}
        # write_only_fields = ['password']
        read_only_fields = ['appointments', 'all_appointments', 'schedules']


class SpecializationSerializer(serializers.HyperlinkedModelSerializer):
    """
        This class represents a serializer which designed for Specialization objects serialization/deserialization.
    """
    # users = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all())
    # users = serializers.SlugRelatedField(many=True, read_only=True, slug_field='first_name')
    users = serializers.HyperlinkedIdentityField(view_name='accounting:user_detail_mail',
                                                 many=True,
                                                 read_only=True,
                                                 lookup_field='email')

    class Meta:
        model = Specialization
        fields = ['id', 'name', 'users']




