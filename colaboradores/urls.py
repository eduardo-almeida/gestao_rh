from django.urls import path
from .views import ColaboradoresList, ColaboradoresEdit, ColaboradoresDelete, ColaboradoresCreate

urlpatterns = [
    path('', ColaboradoresList.as_view(), name='list_colaboradores'),
    path('editar/<int:pk>/', ColaboradoresEdit.as_view(), name='update_colaboradores'),
    path('deletar/<int:pk>/', ColaboradoresDelete.as_view(), name='delete_colaboradores'),
    path('novo/', ColaboradoresCreate.as_view(), name='create_colaboradores'),
]