from django.urls import path
from .views import (FuncionariosList,
                    FuncionariosEdit,
                    FuncionariosDelete,
                    FuncionariosCreate)

urlpatterns = [
    path('', FuncionariosList.as_view(), name='listar_funcionarios'),
    path('editar/<int:pk>/', FuncionariosEdit.as_view(), name='editar_funcionarios'),
    path('deletar/<int:pk>/', FuncionariosDelete.as_view(), name='deletar_funcionarios'),
    path('novo/', FuncionariosCreate.as_view(), name='criar_funcionarios'),
]

