"""
URL configuration for huespedSolution project.

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
# proyecto/urls.py
"""
from django.contrib import admin
from django.urls import path, include
from huesped import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('huesped.urls')),  # Incluye las URLs de la app 'huesped'
    
    
    path('', views.home, name='home'),  # Ruta para la página de inicio pública
    #path('login/', views.login_view, name='login'),  # Ejemplo de ruta para iniciar sesión
    # Otras rutas
]"""
from django.contrib import admin
from django.urls import path
from huesped import views  # Importamos las vistas de nuestra aplicación

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # Ruta para la página de login
    path('home/', views.home_view, name='home'),  # Ruta para la página de inicio
]

