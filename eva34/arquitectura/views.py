from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import raw_data
from .serializers import personas

class Personas(generics.ListCreateAPIView):
    queryset = raw_data.objects.all()
    serializer_class = personas

class Personas_lista(generics.RetrieveUpdateDestroyAPIView):
    queryset = raw_data.objects.all()
    serializer_class = personas
