from django.urls import path
from .views import EmpresaCreate, EmpresaEdit


urlpatterns = [
    path('novo', EmpresaCreate.as_view(), name='criar_empresa'),
    path('editar/<int:pk>', EmpresaEdit.as_view(), name='editar_empresa')
]