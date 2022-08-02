
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from final.forms import UserRegisterForm
from .models import paises 
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login
from .models import MasDatosUsuario
from .forms import MyUserEditForm, MyUserEditForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def inicio (request):
    return render (request, "index.html")


def sobremi (request):
    return render (request, "nosotros.html")

def so (request): 
    return render (request,"sofia.html" )

def ju (request):
    return render (request,  "julian.html")

def vic (request):
    return render (request, "victor.html" )


def listado(request):
    objeto= paises (nombre_pais= "Italia", visita= 2015, idioma="Italiano" )
    objeto.save()
 
    return HttpResponse("EAT AND TRAVEL")

def vistapaises (request):
    if request.GET:
        nombrepais = str( request.GET['nombre_pais'] )
        visitar = int( request.GET['visita'] )
        idiomas = str( request.GET['idioma'] )
        objeto2 = paises( nombre_pais= nombrepais , visita= visitar , idioma= idiomas)
        objeto2.save()
        
    info= paises.objects.all()
    contexto= {"final" : info }
    plantilla=loader.get_template("html1.html")
    documento= plantilla.render(contexto) 
    
    
    return HttpResponse( documento )

    
def buscar(request):
    contexto2= {}

    if request.GET:
        var2 = request.GET["buscar"]
        buscador = paises.objects.filter(nombre_pais__icontains = var2)
        contexto2= {"buscados": buscador}        

    
    plantilla = loader.get_template("buscados.html")
    documento2 = plantilla.render( contexto2 )

    return HttpResponse( documento2 )

def registro (request):
    
    if request.method == 'POST':
        
        #form=UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username= form.cleaned_data["username"]
            form.save()
            return render (request, "Logueo.html" , {"mensaje": "Usuario Creado "})

    else:
        #form=UserCreationForm()
        form = UserRegisterForm()
    return render (request, "registro.html" , {"form": form})




@login_required
def perfiles(request):
    return render(request, 'perfil.html')

@login_required
def editar_perfiles(request):
    
    user = request.user
    mas_datos_usuario, _ = MasDatosUsuario.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        form = MyUserEditForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('first_name'):
                user.first_name = data.get('first_name')
            if data.get('last_name'):
                user.last_name = data.get('last_name')
                
            user.email = data.get('email') if data.get('email') else user.email
            mas_datos_usuario.avatar = data.get('avatares') if data.get('avatares') else mas_datos_usuario.avatar 
            
            mas_datos_usuario.save()
            user.save()
            
    
            return redirect ('perfil')
        
        else:
            return render(request, 'registro.html', {'form': form})
            
    form = MyUserEditForm(
            initial={
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'avatar': mas_datos_usuario.avatar
                }
        )

    return render(request, 'registro.html', {'form': form})





def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                django_login(request, user)
                return redirect('inicio')
            else:
                return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})
        
    
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
    


