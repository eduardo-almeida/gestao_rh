from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('inicio.urls')),
    path('colaboradores/', include('colaboradores.urls')),
    path('departamentos/', include('departamentos.urls')),
    path('empresa/', include('empresas.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
