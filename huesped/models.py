from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    iniciales = models.CharField(max_length=5)
    historia_clinica = models.TextField()
    dni = models.CharField(max_length=15, unique=True)
    cobertura = models.CharField(max_length=100)
    notas_adicionales = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.dni}"
class Profesional(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=50, choices=[('medico', 'Médico'), ('psicologo', 'Psicólogo'), ('abogado', 'Abogado'), ('recepcionista', 'Recepción'), ('investigador', 'Investigador')])
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} - {self.rol}"

class Turno(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    creado_por = models.ForeignKey(
        Profesional,
        on_delete=models.CASCADE,
        related_name='turnos_creados'
    )
    derivado_a = models.ForeignKey(
        Profesional,
        on_delete=models.CASCADE,
        related_name='turnos_derivados'
    )
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=255)
    estado = models.CharField(max_length=50, choices=[('pendiente', 'Pendiente'), ('completado', 'Completado')])

    def __str__(self):
        return f"{self.paciente} - {self.fecha} {self.hora}"
    

class Metrica(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_consulta = models.DateTimeField()
    duracion_consulta = models.DurationField()
    derivaciones_adicionales = models.IntegerField()
    
    def __str__(self):
        return f"Métrica de {self.profesional.nombre} para {self.paciente.nombre} - {self.fecha_consulta}"
    
class Receta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    
    def __str__(self):
        return f"Receta para {self.paciente.nombre} emitida por {self.profesional.nombre}"

class NotaAdicional(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="notas")
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name="notas")
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Nota de {self.profesional} sobre {self.paciente}"
