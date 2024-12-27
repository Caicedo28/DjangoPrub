from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.inicio),
    path('listadoUsuario/',views.listadoUsuario),
    path('nuevoUsuario/',views.nuevoUsuario),
    path('guardarUsuario/',views.guardarUsuario),
    path('eliminarUsuario/<idUsu>',views.eliminarUsuario),
    path('editarUsuario/<idUsu>',views.editarUsuario),
    path('procesarEdicionUsuario/',views.procesarEdicionUsuario),

    path('listadoEspacio/',views.listadoEspacio),
    path('nuevoEspacio/',views.nuevoEspacio),
    path('guardarEspacio/',views.guardarEspacio),
    path('eliminarEspacio/<idEsp>',views.eliminarEspacio),
    path('editarEspacio/<idEsp>',views.editarEspacio),
    path('procesarEdicionEspacio/',views.procesarEdicionEspacio),

    path('listadoHorario/',views.listadoHorario),
    path('nuevoHorario/',views.nuevoHorario),
    path('guardarHorario/',views.guardarHorario),
    path('eliminarHorario/<idHor>',views.eliminarHorario),

    path('listadoReserva/',views.listadoReserva),
    path('nuevoReserva/',views.nuevoReserva),
    path('guardarReserva/',views.guardarReserva),
    path('eliminarReserva/<idRes>',views.eliminarReserva),
    path('editarReserva/<idRes>',views.editarReserva),
    path('procesarEdicionReserva/',views.procesarEdicionReserva),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
