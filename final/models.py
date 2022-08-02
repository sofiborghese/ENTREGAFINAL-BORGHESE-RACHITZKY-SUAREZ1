from django.db import models
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


class paises (models.Model):
    nombre_pais= models.CharField(max_length= 20)
    visita= models.IntegerField()
    idioma= models.CharField(max_length=20)
    

class MasDatosUsuario(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)