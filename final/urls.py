from django.contrib import admin
from django.urls import path
from .views import  inicio, vistapaises,buscar,sobremi, so, ju, vic, login, registro, editar_perfiles, perfiles
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path ("", inicio, name="inicio"), 
    path ("paisess/", vistapaises, name="paisess"),
    path ("busqueda/", buscar, name="buscar" ),
    path ("nosotros/", sobremi, name= "nosotros"),
    path ("sofi/", so, name= "sofi"),
    path ("julian/", ju, name="juli"),
    path ("victor/", vic, name= "vict"), 
    path ("login/", login, name="login"),
    path ("registro/", registro, name="registro"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='salir'),
    path('perfil/', perfiles, name='perfil'),
    path('perfil/editar/', editar_perfiles, name='editar_perfil'),
   
]