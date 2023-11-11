from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from .models import Alumno
from . import forms


def index(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos":alumnos}
    return render(request, "appuni/index.html", context)


def alumno(request, nombre):
    try:
        alumno = Alumno.objects.get(nombre=nombre)
    except Alumno.DoesNotExist:
        raise Http404
    context = {"alumno":alumno}
    return render(request, "appuni/alumno.html", context)


def nuevo_alumno(request):
    if request.method == "POST":
        form = forms.AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = forms.AlumnoForm()
    context = {"form":form}
    return render(request, "appuni/nuevo_alumno.html", context)


#PLUS OPCIONAL (actualizar y eliminar alumno)

def actualizar_alumno(request, pk):
    alumno_actual = Alumno.objects.get(pk=pk)
    if request.method == "POST":
        form = forms.AlumnoForm(request.POST, instance=alumno_actual)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = forms.AlumnoForm(instance=alumno_actual)
    return render(request, "appuni/actualizar_alumno.html", {"form":form})


def eliminar_alumno(request, pk):
    eliminar_alumno = Alumno.objects.get(pk=pk)
    eliminar_alumno.delete()
    return HttpResponseRedirect(reverse("index"))