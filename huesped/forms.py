# forms.py
from django import forms
from .models import Turno, Paciente, NotaAdicional

# huesped/forms.py

from django import forms
from .models import Paciente, Profesional, Turno, NotaAdicional

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'dni', 'historia_clinica', 'cobertura']
        widgets = {
            'historia_clinica': forms.Textarea(attrs={'rows': 3}),
        }


class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['paciente', 'creado_por', 'derivado_a', 'fecha', 'hora', 'motivo', 'estado']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'motivo': forms.TextInput(attrs={'placeholder': 'Motivo de la consulta'}),
            'estado': forms.Select(choices=[('pendiente', 'Pendiente'), ('completado', 'Completado')]),
        }


class NotaAdicionalForm(forms.ModelForm):
    class Meta:
        model = NotaAdicional
        fields = ['paciente', 'profesional', 'contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe una nota adicional...'}),
        }


class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = ['nombre', 'rol']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del profesional'}),
            'rol': forms.TextInput(attrs={'placeholder': 'Especialidad'}),
        }

