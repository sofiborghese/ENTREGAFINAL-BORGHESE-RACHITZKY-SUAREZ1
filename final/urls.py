from django.contrib import admin
from django.urls import path
from .views import  inicio, vistapaises,buscar,sobremi, so, ju, vic 

urlpatterns = [
    path('admin/', admin.site.urls),
    path ("", inicio, name="inicio"), 
    path ("paisess/", vistapaises, name="paisess"),
    path ("busqueda/", buscar, name="buscar" ),
    path ("nosotros/", sobremi, name= "nosotros"),
    path ("sofi/", so, name= "sofi"),
    path ("julian/", ju, name="juli"),
    path ("victor/", vic, name= "vict")
]