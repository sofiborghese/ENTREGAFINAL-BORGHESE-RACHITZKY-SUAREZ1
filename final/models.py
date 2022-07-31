from django.db import models

class paises (models.Model):
    nombre_pais= models.CharField(max_length= 20)
    visita= models.IntegerField()
    idioma= models.CharField(max_length=20)