from rest_framework import serializers
from .models.specialization_model import Specialization

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'
