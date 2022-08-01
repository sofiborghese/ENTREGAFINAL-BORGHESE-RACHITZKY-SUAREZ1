from django.shortcuts import render
from django.http import HttpResponse

from final.forms import UserRegisterForm,UserEditForm
from .models import paises 
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
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

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password = contra)
            
            if user is not None:
                login(request, user)
                return render(request, "index.html", {"mensaje": f"Bienvenido {usuario}"} )
            else:
                return render(request, "", {"mensaje": "Error, datos erróneo"} )
        else:
            
            return render(request, "", {"mensaje": "Error, formulario erróneo"} )
    form = AuthenticationForm()
    
    return render(request, "accounts/login.html", {"form":form} )

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return render(request,"index.html",{"mensaje":"Usuario creado :)"})
           
    else:
        form = UserRegisterForm()   
    
    return render(request, "accounts/register.html", {"form":form} )

@login_required
def editar_perfil(request):
    
    user = request.user
    #mas_datos_usuario, _ = MasDatosUsuario.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES)
        if form.is_valid():
           
            informacion = form.cleaned_data
            user.email = informacion['email']
            user.password1 = informacion['password1']
            user.password2 = informacion['password2']
            # if data.get('first_name'):
            #     user.first_name = data.get('first_name')
            # if data.get('last_name'):
            #     user.last_name = data.get('last_name')
                
            # user.email = data.get('email') if data.get('email') else user.email
            # #mas_datos_usuario.avatar = data.get('avatar') if data.get('avatar') else mas_datos_usuario.avatar
            
            # # if data.get('password1') and data.get('password1') == data.get('password2'):
            # #     user.set_password(data.get('password1'))
            
            # #mas_datos_usuario.save()
            user.save()
    
            return render(request, 'index.html')
        
        else:
            miFormuilario = UserEditForm(initial={'email':user.email})
    #         return render(request, 'accounts/editar_perfil.html', {'form': form})
            
    # form = UserEditForm(
    #         initial={
    #             'email': user.email,
    #             'first_name': user.first_name,
    #             'last_name': user.last_name,
    #             'avatar': mas_datos_usuario.avatar
    #         }
    #     )

    return render(request, 'accounts/editar_perfil.html', {'miFormulario': form, "usuario":user})