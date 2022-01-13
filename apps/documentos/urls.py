from django.contrib import admin
from django.urls import path
from .views import DocumentosCreate
    # , DocumentosDelete
urlpatterns = [
    path('novo/<int:id_funcionario>/', DocumentosCreate.as_view(), name='criar_documentos'),

]