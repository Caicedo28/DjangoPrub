"""
URL configuration for reserva project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Aplicaciones.Estudio.urls')),
    path('listadoUsuario/', include('Aplicaciones.Estudio.urls')),
    path('agregarUsuario/', include('Aplicaciones.Estudio.urls')),

    path('listadoEspacio/', include('Aplicaciones.Estudio.urls')),
    path('agregarEspacio/', include('Aplicaciones.Estudio.urls')),

    path('listadoHorario/', include('Aplicaciones.Estudio.urls')),
    path('agregarHorario/', include('Aplicaciones.Estudio.urls')),

    path('listadoReserva/', include('Aplicaciones.Estudio.urls')),
    path('agregarReserva/', include('Aplicaciones.Estudio.urls')),
]
