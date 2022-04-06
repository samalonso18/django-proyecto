from django.http import HttpResponse
import datetime
from datetime import date
from django.template import Template, Context
from django.template import loader

def saludo(request):   #Nuestra primera vista :) 
	return HttpResponse("Hola Django - Coder")


def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")

def diaDeHoy(request):

        dia = datetime.datetime.now()

        documentoDeTexto = f"Hoy es día: <br> {dia}"


        return HttpResponse(documentoDeTexto)

def tercera_vista(request, fecha):
    fecha_actual = date.today()

    anio = fecha_actual.year
    
    fecha = int(fecha)

    resultado = anio - fecha
    
    retorno = f"El año en que naciste es : {resultado}"
    return HttpResponse(retorno)

def miNombreEs(self, nombre):

      documentoDeTexto = f"Mi nombre es: <br><br>  {nombre}"


      return HttpResponse(documentoDeTexto)


def probandoTemplate(self):

    nom = "Samanta"
    ap = "Alonso"
    
    lista_notas = [2,2,3,7,2,5]
    
    diccionario = {"nombre": nom, "apellido": ap, "hoy": datetime.datetime.now(), "notas": lista_notas}
    
   
    plantilla = loader.get_template("template1.html") 
    
    documento = plantilla.render(diccionario) 

    return HttpResponse(documento)

def pruebaTemplate(self):
    nombre = "Samanta"
    oficio = "profesor"
    nuevo_diccionario = {"nombre": nombre, "oficio": oficio}
    nueva_plantilla = loader.get_template("template2.html")   
    
    documento = nueva_plantilla.render(nuevo_diccionario) 

    return HttpResponse(documento)