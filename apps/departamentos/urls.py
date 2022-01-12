from django.urls import path
from .views import (DepartamentosList,
                    DepartamentosCreate,
                    DepartamentosDelete,
                    DepartamentosUpdate)

urlpatterns = [
    path('', DepartamentosList.as_view() , name='listar_departamentos'),
    path('novo/', DepartamentosCreate.as_view(), name='criar_departamentos'),
    path('deletar/<int:pk>', DepartamentosDelete.as_view(), name='deletar_departamentos'),
    path('editar/<int:pk>', DepartamentosUpdate.as_view(), name='editar_departamentos'),
]