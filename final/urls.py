from django.contrib import admin
from django.urls import path
from .views import  *
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
    path ("login/", login_request, name= "Login"),
    path ("register/", register, name= "Register"),
    path ("logout/", LogoutView.as_view(template_name='logout.html'), name= "Logout"),
    path ("editarPerfil/", editar_perfil, name= "EditarPerfil") 
]