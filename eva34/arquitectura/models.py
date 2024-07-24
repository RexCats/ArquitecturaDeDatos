# Create your models here.
from django.db import models
from datetime import date

class raw_data(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.DateField()

    def calculate_age(self):
        today = date.today()
        return today.year - self.edad.year - ((today.month, today.day) < (self.edad.month, self.edad.day))

class persona_model(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    edad_nominal = models.IntegerField()


