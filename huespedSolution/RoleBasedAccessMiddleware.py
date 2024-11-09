from django.shortcuts import redirect
from django.urls import reverse

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            rol = request.user.profesional.rol
            path = request.path

            # Redirigir según el rol de usuario y la URL
            if rol == 'recepcion' and not path.startswith(reverse('turno')):
                return redirect('turno_list')
            elif rol == 'medico' and not path.startswith(reverse('consulta')):
                return redirect('consulta_list')
            elif rol == 'investigador' and not path.startswith(reverse('investigacion')):
                return redirect('investigacion_list')
       
        response = self.get_response(request)
        return response