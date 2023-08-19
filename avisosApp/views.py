from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from avisosApp import models
import datetime

# Create your views here.


def index(request):
    date = datetime.datetime.now()

    fecha = date.strftime("%d %m %Y").replace(" ", "/")
    subject = request.GET.get("asunto", False)
    mesage = request.GET.get("mensaje", False)

    datos = reversed(models.Aviso.objects.all())
    contexto = {
        "datos": datos,
        "fecha": fecha,
    }

    if request.method == "GET" and mesage != False:
        models.Aviso(asunto=subject, mensaje=mesage).save()

        return HttpResponseRedirect("/ok")
    return render(request, "index.html", contexto)


def ok(request):
    return HttpResponseRedirect("/")
