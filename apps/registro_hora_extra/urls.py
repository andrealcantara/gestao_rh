from django.urls import path
from .views import (HoraExtraList,
                    HoraExtraUpdate,
                    HoraExtraDelete,
                    HoraExtraCreate,
                    HoraExtraUtilizadaToggle,
                    HoraExtraByFuncionarioUpdate,
                    HoraExtraByFuncionarioCreate,
                    )


urlpatterns = [
    path('', HoraExtraList.as_view(), name='listar_hora_extra'),
    path('editar/<int:pk>/', HoraExtraUpdate.as_view(), name='editar_hora_extra'),
    path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='deletar_hora_extra'),
    path('novo/', HoraExtraCreate.as_view(), name='criar_hora_extra'),
    path('toggle/<int:pk>/', HoraExtraUtilizadaToggle.as_view()),
    path('novo/funcionario/<int:funcionario_id>/', HoraExtraByFuncionarioCreate.as_view(), name='criar_hora_extra_por_funcionario'),
    path('editar/funcionario/<int:pk>/<int:funcionario_id>/', HoraExtraByFuncionarioUpdate.as_view(), name='editar_hora_extra_por_funcionario'),
]

