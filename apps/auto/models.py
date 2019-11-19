from django.db import models
from apps.compra.models import Persona



class Auto(models.Model): 
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    anno = models.IntegerField()
    tipo = models.CharField(max_length=50)
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)

    