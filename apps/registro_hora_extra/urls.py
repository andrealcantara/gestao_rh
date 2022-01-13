from django.urls import path
from .views import HoraExtraList, HoraExtraUpdate, HoraExtraDelete, HoraExtraCreate


urlpatterns = [
    path('', HoraExtraList.as_view(), name='listar_hora_extra'),
    path('editar/<int:pk>/', HoraExtraUpdate.as_view(), name='editar_hora_extra'),
    path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='deletar_hora_extra'),
    path('novo/', HoraExtraCreate.as_view(), name='criar_hora_extra'),
]

