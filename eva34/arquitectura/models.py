# Create your models here.
from django.db import models

class raw_data(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.DateField()

    def nombre_completo_edad(self):
        return f'{self.nombre} {self.apellido} {self.edad} años'
