from django.shortcuts import render
from django.views.generic import ListView
from .models import Departamento

class DepartamentosList(ListView):
    model = Departamento