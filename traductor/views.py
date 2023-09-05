from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import TraduccionForm, BusquedaForm
from .models import Traduccion, HistorialTraduccion, Busqueda


def inicio(request):
    return render(request, 'inicio.html')

def index(request):
    mensaje = "Bienvenido al traductor de inglés a español."
    return render(request, 'index.html', {'mensaje': mensaje})


def registro(request):
    if request.method == 'POST':
        registro_form = UserCreationForm(request.POST)
        if registro_form.is_valid():
            user = registro_form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            return redirect('traductor_view')  # Redirigir a la página del traductor después del registro
    else:
        registro_form = UserCreationForm()
    return render(request, 'registration/registro.html', {'registro_form': registro_form})


def iniciar_sesion(request):
    if request.method == 'POST':
        inicio_sesion_form = AuthenticationForm(request, request.POST)
        if inicio_sesion_form.is_valid():
            user = authenticate(username=inicio_sesion_form.cleaned_data['username'], password=inicio_sesion_form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('traductor_view')  # Redirigir a la página del traductor después del inicio de sesión
            else:
                messages.error(request, 'Inicio de sesión fallido. Por favor, verifica tus credenciales.')
    else:
        inicio_sesion_form = AuthenticationForm()
    return render(request, 'registration/iniciar_sesion.html', {'inicio_sesion_form': inicio_sesion_form})


def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Cierre de sesión exitoso.')
    return redirect('inicio')  # Redirigir a la página de inicio después del cierre de sesión
def traductor_view(request):
    if request.method == 'POST':
        traduccion_form = TraduccionForm(request.POST)
        if traduccion_form.is_valid():
            # Guardar la traducción en la base de datos
            traduccion = traduccion_form.save()
            # Agregar la traducción al historial de traducciones
            HistorialTraduccion.objects.create(
                texto_original=traduccion.texto_ingles,
                texto_traducido=traduccion.texto_espanol,
            )
            # Redirigir para ingresar otra traducción
            return redirect('traductor_view')
    else:
        traduccion_form = TraduccionForm()

    # Obtener todas las traducciones almacenadas en la base de datos
    traducciones = Traduccion.objects.all()
    historial_traducciones = HistorialTraduccion.objects.all()

    return render(request, 'traductor.html', {
        'traduccion_form': traduccion_form,
        'traducciones': traducciones,
        'historial_traducciones': historial_traducciones,
    })


def busqueda_view(request):
    if request.method == 'POST':
        busqueda_form = BusquedaForm(request.POST)
        if busqueda_form.is_valid():
            consulta = busqueda_form.cleaned_data['consulta']
            # Realizar una búsqueda en la base de datos
            resultados = Traduccion.objects.filter(texto_ingles__icontains=consulta)
        else:
            resultados = []

        return render(request, 'busqueda.html', {
            'busqueda_form': busqueda_form,
            'resultados': resultados,
        })
    else:
        busqueda_form = BusquedaForm()

    return render(request, 'busqueda.html', {
        'busqueda_form': busqueda_form,
    })
