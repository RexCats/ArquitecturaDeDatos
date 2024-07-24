from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import raw_data, persona_model
from .serializers import rawdata_serializer, personas_serializer


class ETLView(APIView):
    def post(self, request):
        all_objects = raw_data.objects.all()
        for obj in all_objects:
            objeto_procesado = persona_model()
            objeto_procesado.nombre_completo = f"{obj.nombre}  {obj.apellido}"
            objeto_procesado.edad_nominal = obj.calculate_age()
            objeto_procesado.save()
        return Response("Datos procesados...")


    def get(self, request):
        datos_procesados = persona_model.objects.all()
        serializados = personas_serializer(datos_procesados, many=True)
        return Response(serializados.data)


