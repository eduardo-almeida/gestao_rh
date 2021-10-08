from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('colaboradores/', include('colaboradores.urls')),
    path('admin/', admin.site.urls),
]
