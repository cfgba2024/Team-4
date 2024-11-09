# huesped/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Rutas para recepción
    path('recepcion/', views.RecepcionDashboardView.as_view(), name='recepcion_dashboard'),
    path('recepcion/crear_turno/', views.CrearTurnoView.as_view(), name='crear_turno'),
    path('recepcion/modificar_turno/<int:turno_id>/', views.ModificarTurnoView.as_view(), name='modificar_turno'),
    path('recepcion/eliminar_turno/<int:turno_id>/', views.EliminarTurnoView.as_view(), name='eliminar_turno'),

    # Rutas para profesional
    path('profesional/', views.ProfesionalDashboardView.as_view(), name='profesional_dashboard'),
    path('profesional/detalle_paciente/<int:paciente_id>/', views.DerivarPacienteView.as_view(), name='detalle_paciente'),
    path('profesional/agregar_nota/<int:paciente_id>/', views.AgregarNotaView.as_view(), name='agregar_nota'),

    # Rutas para investigación
    path('investigacion/', views.InvestigacionDashboardView.as_view(), name='investigacion_dashboard'),
    path('investigacion/derivar_paciente/<int:paciente_id>/<int:profesional_id>/', views.DerivarPacienteView.as_view(), name='derivar_paciente'),

    # Rutas para métricas
    path('metricas/', views.MetricasView.as_view(), name='metricas_dashboard'),
]
