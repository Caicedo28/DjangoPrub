from django.db import models

class Usuario(models.Model):
    idUsu = models.AutoField(primary_key=True)
    apellidoUsuario = models.TextField(max_length=250)
    nombreUsuario = models.TextField(max_length=250)
    correoUsuario = models.EmailField()
    rolUsuario = models.TextField(max_length=250)

    def __str__(self):
        return self.nombreUsuario


class Espacio(models.Model):
    idEsp = models.AutoField(primary_key=True)
    nombreEspacio = models.TextField(max_length=250)
    ubicacionEspacio = models.TextField(max_length=250)
    capacidadEspacio = models.CharField(max_length=3)

    def __str__(self):
        return self.nombreEspacio


class Horario(models.Model):
    idHor = models.AutoField(primary_key=True)
    diaHorario = models.TextField(max_length=250)
    horario = models.TextField(max_length=250)

    # Clave foránea hacia Espacio con un related_name único
    espacio = models.ForeignKey('Espacio', on_delete=models.CASCADE, related_name='horarios')

    def __str__(self):
        return f"{self.diaHorario} - {self.horario}"


class Reserva(models.Model):
    idRes = models.AutoField(primary_key=True)
    fechaReserva = models.DateField()
    horaInicio = models.TextField(max_length=250)
    horaFinal = models.TextField(max_length=250)
    estadoReserva = models.TextField(max_length=250)

    # Clave foránea hacia Usuario con un related_name único
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='reservas')

    # Clave foránea hacia Espacio con un related_name único
    espacio = models.ForeignKey('Espacio', on_delete=models.CASCADE, related_name='reservas')

    def __str__(self):
        return f"Reserva {self.idRes} - {self.usuario.nombreUsuario} - {self.espacio.nombreEspacio}"
