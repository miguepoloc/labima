"""remo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path

from django.contrib.auth import views

urlpatterns = [
    path('', include('apps.main.urls')),
    path('estaciones/', include('apps.estaciones.urls')),
    path('componentes/', include('apps.componentes.urls')),
    path('sensores/', include('apps.sensores.urls')),
    path('calendario/', include('apps.calendario.urls')),
    path('salidas_de_campo/', include('apps.salidas_de_campo.urls')),
    path('graficas/', include('apps.graficas.urls')),
    path('data/', include('apps.data.urls')),
    path('api/', include('apps.api.urls')),
    path('admin/', admin.site.urls),
]

admin.site.site_header = 'Administración de REMO'