from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import FormularioCursos
from .models import Cursos
from django.contrib.auth.decorators import login_required

# Create your views here.


def inicio(request):
    return render(request, "index.html")


def registro(request):

    if request.method == "GET":
        return render(request, "registro.html", {
            'formulario': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                usuario = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                usuario.save()
                login(request, usuario)
                return redirect('ver_cursos')
            except IntegrityError:
                return render(request, "registro.html", {
                    'formulario': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, "registro.html", {
            'formulario': UserCreationForm,
            'error': 'Las constraseñas no coinciden'
        })


def ver_cursos(request):
    if User.is_authenticated == True:
        try:
            lista_cursos = Cursos.objects.filter(usuario=request.user)
            return render(request, 'ver_cursos.html', {
                "lista_de_cursos": lista_cursos
            })
        except:
            return render(request, 'ver_cursos.html', {
                "lista_de_cursos": lista_cursos,
                "error": "Ha Ocurrido un error"
            })
    elif request.user == "administradors":
        try:
            lista_cursos = Cursos.objects.all()
            return render(request, 'ver_cursos.html', {
                "lista_de_cursos": lista_cursos
            })
        except:
            return render(request, 'ver_cursos.html', {
                "lista_de_cursos": lista_cursos,
                "error": "Ha Ocurrido un error"
            })
    else:
        try:
            lista_cursos = Cursos.objects.all()
            return render(request, 'ver_cursos.html', {
                "lista_de_cursos": lista_cursos
            })
        except:
            return render(request, 'ver_cursos.html', {
                "lista_de_cursos": lista_cursos,
                "error": "Ha Ocurrido un error"
            })


@login_required
def detalles_cursos(request, id):
    if request.method == "GET":
        informacion_curso = get_object_or_404(
            Cursos, pk=id, usuario=request.user)
        fomulario = FormularioCursos(instance=informacion_curso)
        return render(request, 'detalles_cursos.html', {
            'informacion_curso': informacion_curso,
            "formulario": fomulario
        })
    else:
        try:
            informacion_curso = get_object_or_404(
                Cursos, pk=id, usuario=request.user)
            fomulario = FormularioCursos(
                request.POST, instance=informacion_curso)
            fomulario.save()
            return redirect("ver_cursos")
        except:
            return render(request, 'detalles_cursos.html', {
                'informacion_curso': informacion_curso,
                "formulario": fomulario,
                "error": "Error al actualizar el curso"
            })


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect("inicio")


def inicio_sesion(request):
    if request.method == "GET":
        return render(request, "inicio_sesion.html", {
            'formulario': AuthenticationForm,
        })
    else:
        usuario = authenticate(
            request, username=request.POST["username"], password=request.POST['password'])
        if usuario is None:
            return render(request, "inicio_sesion.html", {
                'formulario': AuthenticationForm,
                'error': "Usuario o Contraseña incorrecta",
            })
        else:
            login(request, usuario)
            return redirect("ver_cursos")


@login_required
def crear_cursos(request):

    if request.method == "GET":
        return render(request, "crear_cursos.html", {
            'formulario': FormularioCursos
        })
    else:
        try:
            formulario = FormularioCursos(request.POST)
            nuevo_curso = formulario.save(commit=False)
            nuevo_curso.usuario = request.user
            nuevo_curso.save()
            return redirect("ver_cursos")
        except:
            return render(request, "crear_cursos.html", {
                'formulario': FormularioCursos,
                'error': "Informacion Invalida"
            })


@login_required
def eliminar_cursos(request, id):
    informacion_curso = get_object_or_404(Cursos, pk=id, usuario=request.user)
    if request.method == "POST":
        informacion_curso.delete()
        return redirect("ver_cursos")
