from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from inicio import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include('inicio.urls')),
    path('colaboradores/', include('colaboradores.urls')),
    path('departamentos/', include('departamentos.urls')),
    path('documentos/', include('documentos.urls')),
    path('empresa/', include('empresas.urls')),
    path('horas-extras/', include('registro_hora_extra.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
