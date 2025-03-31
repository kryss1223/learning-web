    #view.py
from django.shortcuts import render, redirect
from .models import Concepto
import random


def ejercicio_espacios(request):
     # Obtén una instancia de Definicions (puedes usar .get() o .filter() según tus necesidades)
    concepto = random.choice(Concepto.objects.all()) #El problema esta aqui porque elige entre todos sin filtrar por parte de leccion
    claveConc = concepto.clave
    defIni = concepto.def_inicial
    defSol = concepto.def_solucion

    defOpc = defSol
    while defOpc == defSol:
        opcion = random.choice(Concepto.objects.all())
        defOpc = opcion.def_solucion

    # Ahora puedes usar clave y defIni en tu contexto o hacer lo que necesites con ellos
    context = {
        'clave': claveConc,
        'definicial': defIni,
        'defsolucion': defSol,
        'defopcion': defOpc,
        # ... otros datos que desees agregar al contexto
    }
    return render(request, 'ejercicio_espacios.html', context)
