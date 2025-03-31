from django.shortcuts import render
from Lessons.models import Leccion, ParteLeccion, Ejercicio, Concepto, ExamenDGT

# Create your views here.

def show_lessons(request):
    lecciones = Leccion.objects.order_by('id')
    # Extrae los títulos de las lecciones
    titulos_lecciones = [leccion.titulo for leccion in lecciones]

    return render(request, 'home.html', {'titulos_lecciones': titulos_lecciones})

def show_exercises(request):
    partes_leccion = ParteLeccion.objects.all()

    context = {'partes_leccion': []}

    for parte_leccion in partes_leccion:
        definiciones = Concepto.objects.filter(parte_leccion=parte_leccion)
        ejercicios = Ejercicio.objects.filter(parte_leccion=parte_leccion)

        # Puedes agregar más datos según sea necesario
        context['partes_leccion'].append({
            'parte_leccion': parte_leccion,
            'definiciones': definiciones,
            'ejercicios': ejercicios,
        })

    return render(request, 'home.html', context)
