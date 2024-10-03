"""Proyecto_Pinturas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pinturas import views
from django.shortcuts import render


# Importa la vista personalizada para el error 404
from django.conf.urls import handler404

# Define tu vista personalizada
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.mostrarIndex, name='index'),
    path('login', views.iniciarSesion, name='login'),
    path('logout', views.cerrarSesion),

    path('menu_admin', views.mostrarMenuAdmin),

    path('form_registrar_estilos', views.mostrarFormRegistrarEstilo),
    path('registrar_estilo', views.registrarEstilo),
    path('form_actualizar_estilo/<int:id>', views.mostrarFormActualizarEstilo),
    path('actualizar_estilo/<int:id>', views.actualizarEstilo),
    path('eliminar_estilo/<int:id>', views.eliminarEstilo),

    path('listar_historial', views.mostrarListarHistorial),

    path('menu_usuario', views.mostrarMenuUsuario),
    path('form_registrar_pinturas', views.mostrarFormRegistrarPinturas),
    path('registrar_pintura', views.registrarPintura),
    path('form_actualizar_pintura/<int:id>', views.mostrarFormActualizarPintura),
    path('actualizar_pintura/<int:id>', views.actualizarPintura),
    path('listar_pinturas', views.mostrarListarPinturas),
    path('eliminar_pintura/<int:id>', views.eliminarPintura),

]
handler404 = views.custom_404_view
