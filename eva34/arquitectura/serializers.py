from rest_framework import serializers
from .models import raw_data, persona_model

class rawdata_serializer(serializers.ModelSerializer):
    class Meta:
        model = raw_data
        fields = ['id', 'nombre', 'apellido', 'edad']

class personas_serializer(serializers.ModelSerializer):
    class Meta:
        model = persona_model
        fields = "__all__"




