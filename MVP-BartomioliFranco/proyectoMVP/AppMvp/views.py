from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse
from django.template import Template,Context, loader

# Create your views here.
def flia(request):
    persona1=Familia(nombre = "Franco",apellido="Bartomioli",dni=1234, nac="1995-11-23")
    persona1.save()
    persona1=Familia(nombre = "Marcos",apellido="Bartomioli",dni=1234, nac="1995-12-23")
    persona1.save()
    persona1=Familia(nombre = "Norma",apellido="Bartomioli",dni=1234, nac="1980-11-23")
    persona1.save()

    return HttpResponse()

def mostrar_familia(request):
    lista= Familia.objects.all()
    return render(request, "Templ1.html", {"lista":lista})

