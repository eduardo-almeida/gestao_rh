from django.urls import path
from .views import DocumentoCreate
#, DocumentoEdit

urlpatterns = [
    path('novo/<int:colaborador_id>', DocumentoCreate.as_view(), name="create_documento"),
    #path('editar/<int:pk>', DocumentoEdit.as_view(), name="edit_documento"),
]
