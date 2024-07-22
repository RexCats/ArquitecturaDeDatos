from rest_framework import serializers, viewsets
from .models import raw_data
from datetime import date

class personas(serializers.ModelSerializer):
    nombre_completo_edad = serializers.SerializerMethodField()
    class Meta:
        model = raw_data
        fields = ['id','nombre_completo_edad']
    def get_nombre_completo_edad(self, obj):
        return f'{obj.nombre} {obj.apellido} {date.today().year - obj.edad.year} años'

class raw_data_write(serializers.ModelSerializer):
    class Meta:
        model = raw_data
        fields = ['nombre', 'apellido', 'edad']

class raw_data_post(viewsets.ModelViewSet):
    queryset = raw_data.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return raw_data_write
        return personas