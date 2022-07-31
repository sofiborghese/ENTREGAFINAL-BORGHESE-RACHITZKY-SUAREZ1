from django.shortcuts import render
from django.http import HttpResponse
from .models import paises 
from django.template import loader

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