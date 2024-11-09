from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Turno, Paciente, Profesional, Metrica
from .forms import TurnoForm, PacienteForm, NotaAdicionalForm

# --- Vistas para Recepción ---
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')




#class RecepcionDashboardView(LoginRequiredMixin, View):
class RecepcionDashboardView(View):
    """Dashboard principal de recepción para ver y gestionar turnos y pacientes."""
    def get(self, request):
        turnos = Turno.objects.all()
        pacientes = Paciente.objects.all()
        return render(request, 'recepcion/dashboard.html', {'turnos': turnos, 'pacientes': pacientes})

class CrearTurnoView(LoginRequiredMixin, View):
    def get(self, request):
        form = TurnoForm()
        return render(request, 'recepcion/crear_turno.html', {'form': form})

    def post(self, request):
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recepcion_dashboard')
        return render(request, 'recepcion/crear_turno.html', {'form': form})

class ModificarTurnoView(LoginRequiredMixin, View):
    def get(self, request, turno_id):
        turno = get_object_or_404(Turno, id=turno_id)
        form = TurnoForm(instance=turno)
        return render(request, 'recepcion/modificar_turno.html', {'form': form})

    def post(self, request, turno_id):
        turno = get_object_or_404(Turno, id=turno_id)
        form = TurnoForm(request.POST, instance=turno)
        if form.is_valid():
            form.save()
            return redirect('recepcion_dashboard')
        return render(request, 'recepcion/modificar_turno.html', {'form': form})

class EliminarTurnoView(LoginRequiredMixin, View):
    def post(self, request, turno_id):
        turno = get_object_or_404(Turno, id=turno_id)
        turno.delete()
        return redirect('recepcion_dashboard')

# --- Vistas para Profesionales (Médicos, Psicólogos, Abogados, etc.) ---

class ProfesionalDashboardView(LoginRequiredMixin, View):
    """Dashboard para profesionales, donde pueden ver la lista de pacientes y sus detalles."""
    def get(self, request):
        turnos = Turno.objects.filter(derivado_a=request.user.profesional, estado='pendiente')
        return render(request, 'profesional/dashboard.html', {'turnos': turnos})

class DetallePacienteView(LoginRequiredMixin, View):
    """Vista para ver detalles de un paciente específico."""
    def get(self, request, paciente_id):
        paciente = get_object_or_404(Paciente, id=paciente_id)
        return render(request, 'profesional/detalle_paciente.html', {'paciente': paciente})

class AgregarNotaView(LoginRequiredMixin, View):
    def get(self, request, paciente_id):
        form = NotaAdicionalForm()
        return render(request, 'profesional/agregar_nota.html', {'form': form})

    def post(self, request, paciente_id):
        form = NotaAdicionalForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.paciente_id = paciente_id
            nota.profesional = request.user.profesional
            nota.save()
            return redirect('profesional_dashboard')
        return render(request, 'profesional/agregar_nota.html', {'form': form})

# --- Vistas para Investigación/Asistentes ---

class InvestigacionDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        pacientes = Paciente.objects.all()
        return render(request, 'investigacion/dashboard.html', {'pacientes': pacientes})

class DerivarPacienteView(LoginRequiredMixin, View):
    """Vista para derivar un paciente a otra área o profesional."""
    def post(self, request, paciente_id, nuevo_profesional_id):
        paciente = get_object_or_404(Paciente, id=paciente_id)
        paciente.derivado_a_id = nuevo_profesional_id
        paciente.save()
        return redirect('investigacion_dashboard')

# --- Vistas para Métricas ---

class MetricasView(LoginRequiredMixin, View):
    """Vista para ver métricas de atención y estadísticas."""
    def get(self, request):
        metricas = Metrica.objects.all()
        # Se pueden calcular más métricas o agrupar según sea necesario.
        return render(request, 'metricas/dashboard.html', {'metricas': metricas})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# Vista para la página de login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Autenticar al usuario
            return redirect('home')  # Redirigir a la página de inicio
        else:
            # Si las credenciales son incorrectas
            return render(request, 'login.html', {'form': form, 'error': 'Credenciales incorrectas.'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Vista para la página de inicio (después del login)
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Si no está autenticado, redirigir al login
    return render(request, 'home.html')