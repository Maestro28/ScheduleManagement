from rest_framework import serializers

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
        user = CustomUser.objects.create_user(**validated_data)
        user.save()

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'password', 'specs', 'role']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['appointments', 'all_appointments', 'schedules']


class SpecializationSerializer(serializers.HyperlinkedModelSerializer):
    """
        This class represents a serializer which designed for Specialization objects serialization/deserialization.
    """
    users = serializers.HyperlinkedIdentityField(view_name='accounting:user_detail_mail',
                                                 many=True,
                                                 read_only=True,
                                                 lookup_field='email')

    class Meta:
        model = Specialization
        fields = ['id', 'name', 'users']


class UserListBySpec(serializers.Serializer):
    """
        This class represents a serializer which designed for show all specialists on that specialization.
    """
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    users = serializers.ListField(
        child=serializers.IntegerField()
    )

    def validate(self, data):
        """
        Check that start is before finish.
        """
        users = []
        for user_id in data['users']:
            user = CustomUser.objects.get(pk=user_id)
            d = {}
            d['id'] = user_id
            d['email'] = user.email
            d['first name'] = user.first_name
            d['last name'] = user.last_name
            d['phone'] = user.phone
            users.append(d)
        data['users'] = users
        return data

    class Meta:
        fields = ['id', 'name', 'users']



