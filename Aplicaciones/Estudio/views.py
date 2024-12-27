from django.shortcuts import redirect,render

#Importar modulos de Usuario,Espacio,Horario,Reserva
from .models import Usuario
from .models import Espacio
from .models import Horario
from .models import Reserva

#importando django.countrib para mensajes de confirmacion 
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

#-----------------------------------------------------------------Usuario------------------------------------------------------------------------------------

#Presentando en pantalla el formulario de nuevo Usuario
def nuevoUsuario(request):
    return render(request,'nuevoUsuario.html')

#Presentando en pantalla el listado de Usuario
def listadoUsuario(request):
    usuarioBdd=Usuario.objects.all()
    return render(request,'listadoUsuario.html',{'usuario':usuarioBdd})

#Capturando datos del formulario e insertando en la Bdd
def guardarUsuario(request):
    nombreUsuario=request.POST['txt_nombreUsuario']
    apellidoUsuario=request.POST['txt_apellidoUsuario']
    correoUsuario=request.POST['txt_correoUsuario']
    rolUsuario=request.POST['txt_rolUsuario']
    nuevoUsuario=Usuario.objects.create(nombreUsuario=nombreUsuario,apellidoUsuario=apellidoUsuario,
                                        correoUsuario=correoUsuario,rolUsuario=rolUsuario,)
    messages.success(request,"Usuario Insertado Exitosamente")
    return redirect('/listadoUsuario')

#funcion para eliminar a Usuario por ID
def eliminarUsuario(request,idUsu):
    eliminarUsuario=Usuario.objects.get(idUsu=idUsu)
    eliminarUsuario.delete()
    messages.success(request,"Usuario Eliminado")
    return redirect('/listadoUsuario')

#funcion para mostrar el formulario de edicion
def editarUsuario(request,idUsu):
    editarUsuario=Usuario.objects.get(idUsu=idUsu)
    return render(request,"editarUsuario.html", {'usuario':editarUsuario})

#funcion para combinar cambios de Usuario en la bdd
def procesarEdicionUsuario(request):
    usuario=Usuario.objects.get(idUsu=request.POST['idUsu'])
    nombreUsuario=request.POST['txt_nombreUsuario']
    apellidoUsuario=request.POST['txt_apellidoUsuario']
    correoUsuario=request.POST['txt_correoUsuario']
    rolUsuario=request.POST['txt_rolUsuario']

    usuario.nombreUsuario=nombreUsuario
    usuario.apellidoUsuario=apellidoUsuario
    usuario.correoUsuario=correoUsuario
    usuario.rolUsuario=rolUsuario
    usuario.save()
    messages.success(request,"Usuario Editado Exitosamente")
    return redirect('/listadoUsuario')

#-----------------------------------------------------------------Espacio------------------------------------------------------------------------------------

#Presentando en pantalla el formulario de nuevo Espacio
def nuevoEspacio(request):
    return render(request,'nuevoEspacio.html')

#Presentando en pantalla el listado de Espacio
def listadoEspacio(request):
    espacioBdd=Espacio.objects.all()
    return render(request,'listadoEspacio.html',{'espacio':espacioBdd})

#Capturando datos del formulario e insertando en la Bdd
def guardarEspacio(request):
    nombreEspacio=request.POST['txt_nombreEspacio']
    ubicacionEspacio=request.POST['txt_ubicacionEspacio']
    capacidadEspacio=request.POST['txt_capacidadEspacio']
    nuevoEspacio=Espacio.objects.create(nombreEspacio=nombreEspacio,ubicacionEspacio=ubicacionEspacio,
                                        capacidadEspacio=capacidadEspacio)
    messages.success(request,"Espacio Insertado Exitosamente")
    return redirect('/listadoEspacio')

#funcion para eliminar a Usuario por ID
def eliminarEspacio(request,idEsp):
    eliminarEspacio=Espacio.objects.get(idEsp=idEsp)
    eliminarEspacio.delete()
    messages.success(request,"Espacio Eliminado")
    return redirect('/listadoEspacio')

#funcion para mostrar el formulario de edicion
def editarEspacio(request,idEsp):
    editarEspacio=Espacio.objects.get(idEsp=idEsp)
    return render(request,"editarEspacio.html", {'espacio':editarEspacio})

#funcion para combinar cambios de Usuario en la bdd
def procesarEdicionEspacio(request):
    espacio=Espacio.objects.get(idEsp=request.POST['idEsp'])
    nombreEspacio=request.POST['txt_nombreEspacio']
    ubicacionEspacio=request.POST['txt_ubicacionEspacio']
    capacidadEspacio=request.POST['txt_capacidadEspacio']

    espacio.nombreEspacio=nombreEspacio
    espacio.ubicacionEspacio=ubicacionEspacio
    espacio.capacidadEspacio=capacidadEspacio
    espacio.save()
    messages.success(request,"Espacio Editado Exitosamente")
    return redirect('/listadoEspacio')

#-----------------------------------------------------------------Horario------------------------------------------------------------------------------------

#Presentando en pantalla el formulario de nuevo Horario
def nuevoHorario(request):
    espacio=Espacio.objects.all()
    # Renderizar el template con los datos
    return render(request,'nuevoHorario.html',{
        'espacio':espacio})

#Presentando en pantalla el listado de Usuario
def listadoHorario(request):
    horarioBdd=Horario.objects.all()
    return render(request,'listadoHorario.html',{'horario':horarioBdd})

#Capturando datos del formulario e insertando en la Bdd
def guardarHorario(request):
    espacio_id=request.POST['txt_nombreEspacio']
    diaHorario=request.POST['txt_diaHorario']
    horario=request.POST['txt_horario']
    espacio=Espacio.objects.get(idEsp=espacio_id)
    nuevoHorario=Horario.objects.create(diaHorario=diaHorario,horario=horario,
                                        espacio=espacio,)
    messages.success(request,"Horario Insertado Exitosamente")
    return redirect('/listadoHorario')

#funcion para eliminar a Horario por ID
def eliminarHorario(request,idHor):
    eliminarHorario=Horario.objects.get(idHor=idHor)
    eliminarHorario.delete()
    messages.success(request,"Horario Eliminado")
    return redirect('/listadoHorario')

#-----------------------------------------------------------------Reserva------------------------------------------------------------------------------------

#Presentando en pantalla el formulario de nuevo Reserva
def nuevoReserva(request):
    usuario=Usuario.objects.all()
    espacio=Espacio.objects.all()
    # Renderizar el template con los datos
    return render(request,'nuevoReserva.html',{
        'usuario':usuario,
        'espacio':espacio})

#Presentando en pantalla el listado de Reserva
def listadoReserva(request):
    reservaBdd=Reserva.objects.all()
    return render(request,'listadoReserva.html',{'reserva':reservaBdd})

#Capturando datos del formulario e insertando en la Bdd
def guardarReserva(request):
    usuario_id=request.POST['txt_nombreUsuario']
    espacio_id=request.POST['txt_nombreEspacio']
    fechaReserva=request.POST['txt_fechaReserva']
    horaInicio=request.POST['txt_horaInicio']
    horaFinal=request.POST['txt_horaFinal']
    estadoReserva=request.POST['txt_estadoReserva']
    usuario=Usuario.objects.get(idUsu=usuario_id)
    espacio=Espacio.objects.get(idEsp=espacio_id)
    nuevoReserva=Reserva.objects.create(fechaReserva=fechaReserva,horaInicio=horaInicio,
                                        horaFinal=horaFinal,estadoReserva=estadoReserva,
                                        espacio=espacio,usuario=usuario)
    messages.success(request,"Reserva Insertado Exitosamente")
    return redirect('/listadoReserva')

#funcion para eliminar a Reserva por ID
def eliminarReserva(request,idRes):
    eliminarReserva=Reserva.objects.get(idRes=idRes)
    eliminarReserva.delete()
    messages.success(request,"Reserva Eliminado")
    return redirect('/listadoReserva')

#funcion para mostrar el formulario de edicion
def editarReserva(request,idRes):
    editarReserva=Reserva.objects.get(idRes=idRes)
    usuario=Usuario.objects.all()
    espacio=Espacio.objects.all()
    return render(request,"editarReserva.html", {
        'reserva':editarReserva,
        'usuario':usuario,
        'espacio':espacio,
        })

#funcion para combinar cambios de Reserva en la bdd
def procesarEdicionReserva(request):
    reserva=Reserva.objects.get(idRes=request.POST['idRes'])
    usuario_id=request.POST['txt_nombreUsuario']
    espacio_id=request.POST['txt_nombreEspacio']
    fechaReserva=request.POST['txt_fechaReserva']
    horaInicio=request.POST['txt_horaInicio']
    horaFinal=request.POST['txt_horaFinal']
    estadoReserva=request.POST['txt_estadoReserva']

    reserva.usuario_id=usuario_id
    reserva.espacio_id=espacio_id
    reserva.fechaReserva=fechaReserva
    reserva.horaInicio=horaInicio
    reserva.horaFinal=horaFinal
    reserva.estadoReserva=estadoReserva
    reserva.save()
    messages.success(request,"Reserva Editado Exitosamente")
    return redirect('/listadoReserva')