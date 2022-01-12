from django.urls import path
from .views import DepartamentosList, DepartamentosCreate

urlpatterns = [
    path('', DepartamentosList.as_view() , name='listar_departamentos'),
    path('novo/', DepartamentosCreate.as_view(), name='criar_departamentos'),
]